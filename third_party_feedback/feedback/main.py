# coding:utf8
from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
import sqlite3
import os
import readexcel
import json
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'xls', 'xlsx'}
UPLOAD_PATH = os.path.join(os.path.dirname(__file__), 'uploadfiles')
app.config['UPLOAD_PATH'] = UPLOAD_PATH

# 跨域设置
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/initdb', methods=['POST', 'GET'])
def init_db():
    if request.method == 'GET':
        return '''<form action="/initdb" method="post">
  密码: <input type="password" name="pwd" />
  <input type="submit" value="初始化" />
</form>'''

    password = request.form.get("pwd")

    if not password or password != 'abelit':
        return jsonify({"status": 400, "msg": "请输入密码"})

    os.remove('question.db')

    # 连接数据库
    conn = sqlite3.connect('question.db', check_same_thread=False)

    all_table_text = "SELECT lower(name),sql FROM sqlite_master WHERE type='table' ORDER BY 1"
    cursor = conn.cursor()

    result = cursor.execute(all_table_text)

    for table in result:
        conn.execute("drop table {0}".format(table[0]))

    # create tables
    SQL_TEXT = ["create table tto_question(id integer primary key autoincrement, presentation text,type text, name text,block integer,source_text text,version text,created_timestamp timestamp current_timestamp)",
                "create table interviewer(id integer, name text)",
                "create table dce_question(id integer primary key autoincrement,presentation text,name integer,block integer,answer text,source_text text, version text,created_timestamp timestamp current_timestamp)",
                "create table opened_question(id integer primary key autoincrement,presentation text,name text,block text,source_text text, version text, created_timestamp timestamp current_timestamp)",
                "create table dce_answer(id integer primary key autoincrement,questionid integer,participant integer,interviewer text,item integer, position_of_item integer,selected_state text,dce_reversal text,block integer, version text,created_timestamp timestamp current_timestamp)",
                "create table tto_answer(id integer primary key autoincrement,questionid integer, participant integer, interviewer text,item text,position_of_item integer,tto_value real,used_time text,composite_switches interger,resets integer,number_of_moves integer,block text,version text,created_timestamp timestamp current_timestamp)",
                "create table opened_answer(id integer primary key autoincrement,questionid integer, participant integer,interviewer text,item text,position_of_item integer,participant_answer text,block text, version text,created_timestamp timestamp current_timestamp)"]

    for sql in SQL_TEXT:
        conn.execute(sql)

    # Insert Data
    # interviewer Question
    for data in readexcel.read('./data/questions.xlsx', 'interviewers', True):
        cursor.execute(
            "insert into interviewer(id, name) values({0},'{1}')".format(data[0], data[1]))
    conn.commit()

    # TTO & TTO-Feedback Question
    for data in readexcel.read('./data/questions.xlsx', 'TTO & TTO-Feedback', True):
        cursor.execute("insert into tto_question(presentation,type,name,block,source_text,version) values('{0}','{1}','{2}','{3}','{4}','{5}')".format(
            data[0], data[1], data[2], data[3], data[4], data[5]))
    conn.commit()

    # DCE Question
    for data in readexcel.read('./data/questions.xlsx', 'DCE', True):
        cursor.execute("insert into dce_question(presentation,name,block,answer,source_text,version) values('{0}','{1}','{2}','{3}','{4}','{5}')".format(
            data[0], data[1], data[2], data[3], data[4], data[5]))
    conn.commit()

    # Open ended Question
    for data in readexcel.read('./data/questions.xlsx', 'Open ended questions', True):
        cursor.execute("insert into opened_question(presentation,name,block,source_text,version) values('{0}','{1}','{2}','{3}','{4}')".format(
            data[0], data[1], data[2], data[3], data[4]))
    conn.commit()

    result = cursor.execute(all_table_text)
    table_list = []

    for table in result:
        table_list.append({"name": table[0], "sql": table[1]})

    cursor.close()
    conn.close()
    return jsonify({"status": 200, "msg": "Reinit database successfully!", "tables": table_list})


@app.route("/api/interviewer")
def get_interviewer():
    conn = sqlite3.connect('question.db', check_same_thread=False)
    cursor = conn.cursor()

    SQL_TEXT = "select id, name from interviewer"

    result = cursor.execute(SQL_TEXT)

    data = []

    for row in result:
        data.append({
            "id": row[0],
            "name": row[1]
        })

    return jsonify(data)


@app.route("/api/question/tto")
def get_tto_question():
    block = request.args.get('block')
    version = request.args.get('version')
    print("-----")
    print(version == "")
    print("******")
    # 连接数据库
    conn = sqlite3.connect('question.db', check_same_thread=False)
    cursor = conn.cursor()

    SQL_TEXT = "select id,presentation,type,name,block,source_text,version from tto_question where (block='-' or block='{0}') and version='{1}'".format(
        block, version)

    if block == "all":
        if version == "all" or version == "":
            SQL_TEXT = "select id,presentation,type,name,block,source_text,version from tto_question"
        else:
            SQL_TEXT = "select id,presentation,type,name,block,source_text,version from tto_question where version='{0}'".format(
                version)

    result = cursor.execute(SQL_TEXT)

    data = []

    for row in result:
        data.append({"id": row[0], "presentation": row[1], "type": row[2],
                     "name": row[3], "block": row[4], "source_text": row[5], "version": row[6]})

    return jsonify(data)


@app.route("/api/question/dce")
def get_dce_question():
    block = request.args.get('block')
    # 连接数据库
    conn = sqlite3.connect('question.db', check_same_thread=False)
    cursor = conn.cursor()

    SQL_TEXT = "select id,presentation,name,block,answer,source_text,version from dce_question where block='{0}'".format(
        block)

    if block == "all":
        SQL_TEXT = "select id,presentation,name,block,answer,source_text,version from dce_question"

    result = cursor.execute(SQL_TEXT)

    data = []

    for row in result:
        data.append({"id": row[0], "presentation": row[1], "name": row[2],
                     "block": row[3], "answer": row[4], "source_text": row[5], "version": row[6]})

    return jsonify(data)


@app.route("/api/question/open")
def get_open_question():
    block = request.args.get('block')
    # 连接数据库
    conn = sqlite3.connect('question.db', check_same_thread=False)
    cursor = conn.cursor()

    SQL_TEXT = "select id,presentation,name,block,source_text,version from opened_question where block='{0}'".format(
        block)

    if block == "all":
        SQL_TEXT = "select id,presentation,name,block,source_text,version from opened_question"

    result = cursor.execute(SQL_TEXT)

    data = []

    for row in result:
        data.append({"id": row[0], "presentation": row[1], "name": row[2],
                     "block": row[3], "source_text": row[4], "version": row[5]})

    return jsonify(data)


@app.route("/api/question/blocks")
def get_question_blocks():
    block_type = str(request.args.get('type'))
    # 连接数据库
    conn = sqlite3.connect('question.db', check_same_thread=False)
    cursor = conn.cursor()
    table_name = ""

    if block_type == "1":
        table_name = "dce_question"
    elif block_type == "2":
        table_name = "tto_question"
    elif block_type == "3":
        table_name = "tto_question"
    elif block_type == "4":
        table_name = "opened_question"
    else:
        return "table not exists."

    SQL_TEXT = "select distinct block from {0} where block<>'-'".format(
        table_name)
    result = cursor.execute(SQL_TEXT)

    blocks = []

    for row in result:
        blocks.append(row[0])

    return jsonify(blocks)


@app.route("/api/answer/tto/addall", methods=['POST'])
def add_tto_answer():
    # 连接数据库
    conn = sqlite3.connect('question.db', check_same_thread=False)
    cursor = conn.cursor()

    content = request.get_json()

    status = None
    msg = None

    try:
        cursor = conn.cursor()
        for row in content:
            SQL_TEXT = "insert into tto_answer(questionid,participant,interviewer,item,position_of_item,tto_value,used_time,composite_switches,resets,number_of_moves,block,version) values('{0}', '{1}', '{2}', '{3}', {4}, {5}, '{6}', '{7}', '{8}', '{9}', '{10}', '{11}')".format(
                row['questionid'], row['participant'], row['interviewer'], row['item'], row['position_of_item'], row['tto_value'], row['used_time'], row['composite_switches'], row['resets'], row['number_of_moves'], row['block'], row['version'])
            cursor.execute(SQL_TEXT)
            print(SQL_TEXT)
        conn.commit()
        conn.close()
        status = 200
        msg = "成功"
    except Exception as err:
        msg = err
        status = 600

    return jsonify({"msg": msg, "status": status})
    # return jsonify(request.get_json())


@app.route("/api/answer/tto")
def get_tto_answer():
    # 连接数据库
    conn = sqlite3.connect('question.db', check_same_thread=False)
    cursor = conn.cursor()

    SQL_TEXT = "select * from tto_answer"
    print(SQL_TEXT)
    result = cursor.execute(SQL_TEXT)
    data = []
    for row in result:
        data.append({"id": row[0], "questionid": row[1], "participant": row[2], "interviewer": row[3], "item": row[4], "position_of_item": row[5], "tto_value": row[6],
                     "used_time": row[7], "composite_switches": row[8], "resets": row[9], "number_of_moves": row[10], "block": row[11], "version": row[12], "created_timestamp": row[13]})

    return jsonify(data)


@app.route("/api/answer/dce/addall", methods=['POST'])
def add_dce_answer():
    # 连接数据库
    conn = sqlite3.connect('question.db', check_same_thread=False)
    cursor = conn.cursor()

    content = request.get_json()

    status = None
    msg = None

    try:
        cursor = conn.cursor()
        for row in content:
            SQL_TEXT = "insert into dce_answer(questionid,participant,interviewer,item,position_of_item,selected_state,dce_reversal,block,version) values('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}')".format(
                row['questionid'], row['participant'], row['interviewer'], row['item'], row['position_of_item'], row['selected_state'], row['dce_reversal'], row['block'], row['version'])
            cursor.execute(SQL_TEXT)
            print(SQL_TEXT)
        conn.commit()
        conn.close()
        status = 200
        msg = "成功"
    except Exception as err:
        msg = err
        status = 600

    return jsonify({"msg": msg, "status": status})
    # return jsonify(request.get_json())


@app.route("/api/answer/dce")
def get_dce_answer():
    # 连接数据库
    conn = sqlite3.connect('question.db', check_same_thread=False)
    cursor = conn.cursor()

    SQL_TEXT = "select * from dce_answer"
    print(SQL_TEXT)
    result = cursor.execute(SQL_TEXT)
    data = []
    for row in result:
        print(row)
        data.append({"id": row[0], "questionid": row[1], "participant": row[2], "interviewer": row[3], "item": row[4], "position_of_item": row[5],
                     "selected_state": row[6], "dce_reversal": row[7], "block": row[8], "version": row[9], "created_timestamp": row[10]})

    return jsonify(data)


@app.route("/api/answer/open/addall", methods=['POST'])
def add_open_answer():
    # 连接数据库
    conn = sqlite3.connect('question.db', check_same_thread=False)
    cursor = conn.cursor()

    content = request.get_json()

    status = None
    msg = None

    try:
        cursor = conn.cursor()
        for row in content:
            SQL_TEXT = "insert into opened_answer(questionid,participant,interviewer,item,position_of_item,participant_answer,block,version) values('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}')".format(
                row['questionid'], row['participant'], row['interviewer'], row['item'], row['position_of_item'], row['participant_answer'], row['block'], row['version'])
            cursor.execute(SQL_TEXT)
            print(SQL_TEXT)
        conn.commit()
        conn.close()
        status = 200
        msg = "成功"
    except Exception as err:
        msg = err
        status = 600

    return jsonify({"msg": msg, "status": status})
    # return jsonify(request.get_json())


@app.route("/api/answer/open")
def get_open_answer():
    # 连接数据库
    conn = sqlite3.connect('question.db', check_same_thread=False)
    cursor = conn.cursor()

    SQL_TEXT = "select * from opened_answer"
    print(SQL_TEXT)
    result = cursor.execute(SQL_TEXT)
    data = []
    for row in result:
        print(row)
        data.append({"id": row[0], "questionid": row[1], "participant": row[2], "interviewer": row[3], "item": row[4],
                     "position_of_item": row[5], "participant_answer": row[6], "block": row[7], "version": row[8], "created_timestamp": row[9]})

    return jsonify(data)


@app.route("/api/upload", methods=["POST"])
def upload_file():
    if request.method == 'POST':
        file = request.files.get('file')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
    return jsonify({
        "status": 200,
        "filename": filename
    })


# 访问上传的文件
# http://localhost:5000/uploadfiles/<filename>.jpg/png/pdf
@app.route('/uploadfiles/<filename>/', methods=['GET', 'POST'])
def get_file(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


if __name__ == "__main__":
    # init_db()
    app.run(host="0.0.0.0", debug=True)
