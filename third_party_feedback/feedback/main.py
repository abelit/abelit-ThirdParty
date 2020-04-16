# coding:utf8
from flask import Flask, request, jsonify, render_template, send_from_directory, send_file, make_response
from flask_cors import CORS
import sqlite3
import os
import re
import readexcel
import json
import time
from werkzeug.utils import secure_filename

# Import module cx_Oracle to connect oracle using python
try:
    import cx_Oracle
except ImportError:
    cx_oracle_exists = False
else:
    cx_oracle_exists = True


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

ALLOWED_EXTENSIONS = {'xls', 'xlsx'}
UPLOAD_PATH = os.path.join(os.path.dirname(__file__), 'data')
app.config['UPLOAD_PATH'] = UPLOAD_PATH

app.config['adminpwd'] = "Passw0rd123!"

app.config['JSON_SORT_KEYS'] = False

# 跨域设置
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/admin/initdb', methods=['POST', 'GET'])
def init_db():
    if request.method == 'GET':
        return '''<form action="/admin/initdb" method="post">
  密码: <input type="password" name="pwd" />
  <input type="submit" value="初始化" />
</form>'''

    password = request.get_json()['adminpwd']

    if not password or password != app.config['adminpwd']:
        return jsonify({"status": 400, "msg": "密码错误"}), 520

    os.remove('question.db')

    # 连接数据库
    conn = sqlite3.connect('question.db', check_same_thread=False)

    all_table_text = "SELECT lower(name),sql FROM sqlite_master WHERE type='table' ORDER BY 1"
    cursor = conn.cursor()

    result = cursor.execute(all_table_text)

    for table in result:
        conn.execute("drop table {0}".format(table[0]))

    # create tables
    SQL_TEXT = ["create table interviewer(id integer, name text,version text, created_timestamp timestamp default (datetime(current_timestamp, 'localtime')))",
                "create table eq_question_version(id integer primary key autoincrement, version text, created_timestamp timestamp default (datetime(current_timestamp, 'localtime')))",
                "create table eq_label(id integer primary key autoincrement,questionid integer, reference_id text,slide text,presentation text,en_source_text text,zh_source_text text,version text,created_timestamp timestamp default  current_timestamp)",
                "create table tto_question(id integer primary key autoincrement,questionid integer, presentation text,type text, name text,block integer,source_text text,version text,created_timestamp timestamp default (datetime(current_timestamp, 'localtime')))",
                "create table newtto_question(id integer primary key autoincrement,questionid integer, presentation text,type text, name text,block integer,source_text text,version text,created_timestamp timestamp default (datetime(current_timestamp, 'localtime')))",
                "create table nstptto_question(id integer primary key autoincrement,questionid integer, presentation text,type text, name text,block integer,source_text text,version text,created_timestamp timestamp default (datetime(current_timestamp, 'localtime')))",
                "create table ttofeedback_question(id integer primary key autoincrement,questionid integer, presentation text,type text, name text,block integer,source_text text,version text,created_timestamp timestamp default (datetime(current_timestamp, 'localtime')))",
                "create table dce_question(id integer primary key autoincrement,questionid integer,presentation text,name integer,block integer,answer text,source_text text, version text,created_timestamp timestamp default (datetime(current_timestamp, 'localtime')))",
                "create table opened_question(id integer primary key autoincrement,questionid integer,presentation text,name text,block text,source_text text, version text, created_timestamp timestamp default (datetime(current_timestamp, 'localtime')))",
                "create table dce_answer(id integer primary key autoincrement,questionid integer,participant text,interviewer text,item integer, position_of_item integer,selected_state text,dce_reversal text,block integer, version text,created_timestamp timestamp default (datetime(current_timestamp, 'localtime')))",
                "create table tto_answer(id integer primary key autoincrement,questionid integer, participant text, interviewer text,item text,position_of_item integer,tto_value real,used_time text,composite_switches interger,resets integer,number_of_moves integer,block text,version text,created_timestamp timestamp default (datetime(current_timestamp, 'localtime')))",
                "create table newtto_answer(id integer primary key autoincrement,questionid integer, participant text, interviewer text,item text,position_of_item integer,start_year_random text,select1 text,select2 text,select3 text,select4 text,open_select text,end_year_random text,block text,reset text,version text,created_timestamp timestamp default (datetime(current_timestamp, 'localtime')))",
                "create table nstptto_answer(id integer primary key autoincrement,questionid integer, participant text, interviewer text,item text,position_of_item integer,select_order interger,select_value text,page integer,block text,version text,created_timestamp timestamp default (datetime(current_timestamp, 'localtime')))",
                "create table ttofeedback_answer(id integer primary key autoincrement,questionid integer, participant text, interviewer text,item text,position_of_item integer,tto_value real,used_time text,composite_switches interger,resets integer,number_of_moves integer,block text,version text,created_timestamp timestamp default (datetime(current_timestamp, 'localtime')))",
                "create table opened_answer(id integer primary key autoincrement,questionid integer, participant text,interviewer text,item text,position_of_item integer,participant_answer text,block text, version text,created_timestamp timestamp default (datetime(current_timestamp, 'localtime')))"]

    for sql in SQL_TEXT:
        conn.execute(sql)

    # Insert Data
    # interviewer Question
    # for data in readexcel.read('./data/questions.xlsx', 'interviewers', True):
    #     cursor.execute(
    #         "insert into interviewer(id, name,version) values({0},'{1}','{2}')".format(data[0], data[1],data[2]))
    # conn.commit()

    # EQ Label
    for item in ["TTO", "TTO-Feedback", "DCE", "Open ended questions", "Non-Stopping TTO", "New TTO"]:
        for data in readexcel.read('./data/eqlabels.xlsx', item, True):
            cursor.execute(
                "insert into eq_label(questionid,reference_id,slide,presentation,en_source_text,zh_source_text,version) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(data[5], data[0], data[1], data[2], data[3], data[4], data[6]))
        conn.commit()

    # # TTO & TTO-Feedback Question
    # for data in readexcel.read('./data/questions.xlsx', 'TTO & TTO-Feedback', True):
    #     cursor.execute("insert into tto_question(questionid,presentation,type,name,block,source_text,version) values({0},'{1}','{2}','{3}','{4}','{5}','{6}')".format(
    #         data[6],data[0], data[1], data[2], data[3], data[4], data[5]))
    # conn.commit()

    # # DCE Question
    # for data in readexcel.read('./data/questions.xlsx', 'DCE', True):
    #     cursor.execute("insert into dce_question(questionid,presentation,name,block,answer,source_text,version) values({0},'{1}','{2}','{3}','{4}','{5}','{6}')".format(
    #         data[6],data[0], data[1], data[2], data[3], data[4], data[5]))
    # conn.commit()

    # # Open ended Question
    # for data in readexcel.read('./data/questions.xlsx', 'Open ended questions', True):
    #     cursor.execute("insert into opened_question(questionid,presentation,name,block,source_text,version) values({0},'{1}','{2}','{3}','{4}','{5}')".format(
    #         data[5],data[0], data[1], data[2], data[3], data[4]))
    # conn.commit()

    result = cursor.execute(all_table_text)
    table_list = []

    for table in result:
        table_list.append({"name": table[0], "sql": table[1]})

    cursor.close()
    conn.close()
    return jsonify({"status": 200, "msg": "Reinit database successfully!", "tables": table_list})


@app.route("/api/question/version")
def get_question_version():
    conn = sqlite3.connect('question.db', check_same_thread=False)
    cursor = conn.cursor()

    SQL_TEXT = "select distinct version from dce_question union select distinct version from tto_question union select distinct version from opened_question union select distinct version from nstptto_question union select distinct version from newtto_question"

    result = cursor.execute(SQL_TEXT)

    data = []

    for row in result:
        data.append({
            "version": row[0]
        })

    return jsonify(data)


@app.route("/api/answer/version")
def get_answer_version():
    conn = sqlite3.connect('question.db', check_same_thread=False)
    cursor = conn.cursor()

    SQL_TEXT = """select distinct version from dce_answer
    union select distinct version from tto_answer
    union select distinct version from opened_answer
    union select distinct version from ttofeedback_answer
    union select distinct version from nstptto_answer
    union select distinct version from newtto_answer"""

    result = cursor.execute(SQL_TEXT)

    data = []

    for row in result:
        data.append({
            "version": row[0]
        })

    return jsonify(data)


# @app.route("/api/question/version/add", methods=['POST'])
# def add_question_version():
#     # 连接数据库
#     conn = sqlite3.connect('question.db', check_same_thread=False)
#     cursor = conn.cursor()

#     content = request.get_json()

#     status = None
#     msg = None

#     try:
#         cursor = conn.cursor()
#         for row in content:
#             SQL_TEXT = "insert into tto_answer(questionid,participant,interviewer,item,position_of_item,tto_value,used_time,composite_switches,resets,number_of_moves,block,version) values('{0}', '{1}', '{2}', '{3}', {4}, {5}, '{6}', '{7}', '{8}', '{9}', '{10}', '{11}')".format(
#                 row['questionid'], row['participant'], row['interviewer'], row['item'], row['position_of_item'], row['tto_value'], row['used_time'], row['composite_switches'], row['resets'], row['number_of_moves'], row['block'], row['version'])
#             cursor.execute(SQL_TEXT)
#         conn.commit()
#         conn.close()
#         status = 200
#         msg = "成功"
#     except Exception as err:
#         msg = err
#         status = 600

#     return jsonify({"msg": msg, "status": status})


@app.route("/api/interviewer")
def get_interviewer():
    version = request.args.get('version')

    conn = sqlite3.connect('question.db', check_same_thread=False)
    cursor = conn.cursor()

    SQL_TEXT = "select id, name,version,created_timestamp from interviewer"

    if version is not None and version != "all":
        SQL_TEXT = SQL_TEXT + " " + "where version='{0}'".format(version)

    result = cursor.execute(SQL_TEXT)

    data = []

    for row in result:
        data.append({
            "id": row[0],
            "name": row[1],
            "version": row[2],
            "created_timestamp": row[3]
        })

    return jsonify(data)


@app.route("/api/eqlabel")
def get_eqlabel():
    questionid = request.args.get('questionid')
    version = request.args.get('version')

    conn = sqlite3.connect('question.db', check_same_thread=False)
    cursor = conn.cursor()

    SQL_TEXT = "select id,questionid,reference_id,slide,presentation,en_source_text,zh_source_text,version,created_timestamp from eq_label"

    if questionid is not None:
        if questionid != "all":
            if re.search(r'select (.*) from (.*) where (.*)', SQL_TEXT.lower()) is None:
                SQL_TEXT = SQL_TEXT + " " + \
                    "where questionid='{0}'".format(questionid)
            else:
                SQL_TEXT = SQL_TEXT + " " + \
                    "and questionid='{0}'".format(questionid)
    if version is not None:
        if version != "all":
            if re.search(r'select (.*) from (.*) where (.*)', SQL_TEXT.lower()) is None:
                SQL_TEXT = SQL_TEXT + " " + \
                    "where version='{0}'".format(version)
            else:
                SQL_TEXT = SQL_TEXT + " " + "and version='{0}'".format(version)

    result = cursor.execute(SQL_TEXT)

    data = []

    for row in result:
        data.append({"id": row[0], "questionid": row[1], "reference_id": row[2], "slide": row[3], "presentation": row[4],
                     "en_source_text": row[5], "zh_source_text": row[6], "version": row[7], "created_timestamp": row[8]})

    return jsonify(data)


@app.route("/api/question/tto")
def get_tto_question():
    block = request.args.get('block')
    version = request.args.get('version')
    # 连接数据库
    conn = sqlite3.connect('question.db', check_same_thread=False)
    cursor = conn.cursor()

    SQL_TEXT = "select id,presentation,type,name,block,source_text,version,created_timestamp,questionid from tto_question"

    if block is not None:
        if block != "all":
            if re.search(r'select (.*) from (.*) where (.*)', SQL_TEXT.lower()) is None:
                SQL_TEXT = SQL_TEXT + " " + \
                    "where (block='-' or block='{0}')".format(block)
            else:
                SQL_TEXT = SQL_TEXT + " " + \
                    "and (block='-' or block='{0}')".format(block)
    if version is not None:
        if version != "all":
            if re.search(r'select (.*) from (.*) where (.*)', SQL_TEXT.lower()) is None:
                SQL_TEXT = SQL_TEXT + " " + \
                    "where version='{0}'".format(version)
            else:
                SQL_TEXT = SQL_TEXT + " " + "and version='{0}'".format(version)

    result = cursor.execute(SQL_TEXT)

    data = []

    for row in result:
        data.append({"id": row[0], "presentation": row[1], "type": row[2],
                     "name": row[3], "block": row[4], "source_text": row[5], "version": row[6], "created_timestamp": row[7], "questionid": row[8]})

    return jsonify(data)


@app.route("/api/question/newtto")
def get_newtto_question():
    block = request.args.get('block')
    version = request.args.get('version')
    # 连接数据库
    conn = sqlite3.connect('question.db', check_same_thread=False)
    cursor = conn.cursor()

    SQL_TEXT = "select id,presentation,type,name,block,source_text,version,created_timestamp,questionid from newtto_question"

    if block is not None:
        if block != "all":
            if re.search(r'select (.*) from (.*) where (.*)', SQL_TEXT.lower()) is None:
                SQL_TEXT = SQL_TEXT + " " + \
                    "where (block='-' or block='{0}')".format(block)
            else:
                SQL_TEXT = SQL_TEXT + " " + \
                    "and (block='-' or block='{0}')".format(block)
    if version is not None:
        if version != "all":
            if re.search(r'select (.*) from (.*) where (.*)', SQL_TEXT.lower()) is None:
                SQL_TEXT = SQL_TEXT + " " + \
                    "where version='{0}'".format(version)
            else:
                SQL_TEXT = SQL_TEXT + " " + "and version='{0}'".format(version)

    result = cursor.execute(SQL_TEXT)

    data = []

    for row in result:
        data.append({"id": row[0], "presentation": row[1], "type": row[2],
                     "name": row[3], "block": row[4], "source_text": row[5], "version": row[6], "created_timestamp": row[7], "questionid": row[8]})

    return jsonify(data)


@app.route("/api/question/nstptto")
def get_nstptto_question():
    block = request.args.get('block')
    version = request.args.get('version')
    # 连接数据库
    conn = sqlite3.connect('question.db', check_same_thread=False)
    cursor = conn.cursor()

    SQL_TEXT = "select id,presentation,type,name,block,source_text,version,created_timestamp,questionid from nstptto_question"

    if block is not None:
        if block != "all":
            if re.search(r'select (.*) from (.*) where (.*)', SQL_TEXT.lower()) is None:
                SQL_TEXT = SQL_TEXT + " " + \
                    "where (block='-' or block='{0}')".format(block)
            else:
                SQL_TEXT = SQL_TEXT + " " + \
                    "and (block='-' or block='{0}')".format(block)
    if version is not None:
        if version != "all":
            if re.search(r'select (.*) from (.*) where (.*)', SQL_TEXT.lower()) is None:
                SQL_TEXT = SQL_TEXT + " " + \
                    "where version='{0}'".format(version)
            else:
                SQL_TEXT = SQL_TEXT + " " + "and version='{0}'".format(version)

    result = cursor.execute(SQL_TEXT)

    data = []

    for row in result:
        data.append({"id": row[0], "presentation": row[1], "type": row[2],
                     "name": row[3], "block": row[4], "source_text": row[5], "version": row[6], "created_timestamp": row[7], "questionid": row[8]})

    return jsonify(data)


@app.route("/api/question/ttofeedback")
def get_ttofeedback_question():
    block = request.args.get('block')
    version = request.args.get('version')
    # 连接数据库
    conn = sqlite3.connect('question.db', check_same_thread=False)
    cursor = conn.cursor()

    SQL_TEXT = "select id,presentation,type,name,block,source_text,version,created_timestamp,questionid from ttofeedback_question"

    if block is not None:
        if block != "all":
            if re.search(r'select (.*) from (.*) where (.*)', SQL_TEXT.lower()) is None:
                SQL_TEXT = SQL_TEXT + " " + \
                    "where (block='-' or block='{0}')".format(block)
            else:
                SQL_TEXT = SQL_TEXT + " " + \
                    "and (block='-' or block='{0}')".format(block)
    if version is not None:
        if version != "all":
            if re.search(r'select (.*) from (.*) where (.*)', SQL_TEXT.lower()) is None:
                SQL_TEXT = SQL_TEXT + " " + \
                    "where version='{0}'".format(version)
            else:
                SQL_TEXT = SQL_TEXT + " " + "and version='{0}'".format(version)

    result = cursor.execute(SQL_TEXT)

    data = []

    for row in result:
        data.append({"id": row[0], "presentation": row[1], "type": row[2],
                     "name": row[3], "block": row[4], "source_text": row[5], "version": row[6], "created_timestamp": row[7], "questionid": row[8]})

    return jsonify(data)


@app.route("/api/question/dce")
def get_dce_question():
    block = request.args.get('block')
    version = request.args.get('version')
    # 连接数据库
    conn = sqlite3.connect('question.db', check_same_thread=False)
    cursor = conn.cursor()

    SQL_TEXT = "select id,presentation,name,block,answer,source_text,version,created_timestamp,questionid from dce_question"

    if block is not None:
        if block != "all":
            if re.search(r'select (.*) from (.*) where (.*)', SQL_TEXT.lower()) is None:
                SQL_TEXT = SQL_TEXT + " " + \
                    "where (block='-' or block='{0}')".format(block)
            else:
                SQL_TEXT = SQL_TEXT + " " + \
                    "and (block='-' or block='{0}')".format(block)
    if version is not None:
        if version != "all":
            if re.search(r'select (.*) from (.*) where (.*)', SQL_TEXT.lower()) is None:
                SQL_TEXT = SQL_TEXT + " " + \
                    "where version='{0}'".format(version)
            else:
                SQL_TEXT = SQL_TEXT + " " + "and version='{0}'".format(version)

    result = cursor.execute(SQL_TEXT)

    data = []

    for row in result:
        data.append({"id": row[0], "presentation": row[1], "name": row[2],
                     "block": row[3], "answer": row[4], "source_text": row[5], "version": row[6], "created_timestamp": row[7], "questionid": row[8]})

    return jsonify(data)


@app.route("/api/question/open")
def get_open_question():
    block = request.args.get('block')
    version = request.args.get('version')
    # 连接数据库
    conn = sqlite3.connect('question.db', check_same_thread=False)
    cursor = conn.cursor()

    SQL_TEXT = "select id,presentation,name,block,source_text,version,created_timestamp,questionid from opened_question"

    if block is not None:
        if block != "all":
            if re.search(r'select (.*) from (.*) where (.*)', SQL_TEXT.lower()) is None:
                SQL_TEXT = SQL_TEXT + " " + \
                    "where (block='-' or block='{0}')".format(block)
            else:
                SQL_TEXT = SQL_TEXT + " " + \
                    "and (block='-' or block='{0}')".format(block)
    if version is not None:
        if version != "all":
            if re.search(r'select (.*) from (.*) where (.*)', SQL_TEXT.lower()) is None:
                SQL_TEXT = SQL_TEXT + " " + \
                    "where version='{0}'".format(version)
            else:
                SQL_TEXT = SQL_TEXT + " " + "and version='{0}'".format(version)

    result = cursor.execute(SQL_TEXT)

    data = []

    for row in result:
        data.append({"id": row[0], "presentation": row[1], "name": row[2],
                     "block": row[3], "source_text": row[4], "version": row[5], "created_timestamp": row[6], "questionid": row[7]})

    return jsonify(data)


@app.route("/api/question/blocks")
def get_question_blocks():
    block_type = str(request.args.get('type'))
    version = request.args.get('version')
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
    elif block_type == "5":
        table_name = "nstptto_question"
    elif block_type == "6":
        table_name = "newtto_question"
    else:
        return "table not exists."

    SQL_TEXT = "select distinct block from {0} where block<>'-'".format(
        table_name)

    if version is not None:
        SQL_TEXT = SQL_TEXT + " " + " and version='{0}'".format(version)

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
        conn.commit()
        conn.close()
        status = 200
        msg = "成功"
    except Exception as err:
        msg = err
        status = 600

    return jsonify({"msg": msg, "status": status})
    # return jsonify(request.get_json())


@app.route("/api/answer/newtto/addall", methods=['POST'])
def add_newtto_answer():
    # 连接数据库
    conn = sqlite3.connect('question.db', check_same_thread=False)
    cursor = conn.cursor()

    content = request.get_json()

    print(content)

    status = None
    msg = None

    try:
        cursor = conn.cursor()
        for row in content:
            SQL_TEXT = "insert into newtto_answer(questionid,participant,interviewer,item,position_of_item,start_year_random,select1,select2,select3,select4,end_year_random,open_select,block,reset,version) values('{0}', '{1}', '{2}', '{3}', {4}, {5}, '{6}', '{7}', '{8}', '{9}', '{10}', '{11}','{12}','{13}','{14}')".format(
                row['questionid'], row['participant'], row['interviewer'], row['item'], row['position_of_item'], row['start_year_random'], row['select1'], row['select2'], row['select3'], row['select4'], row['end_year_random'], row['open_select'], row['block'],row['reset'], row['version'])
            cursor.execute(SQL_TEXT)
        conn.commit()
        conn.close()
        status = 200
        msg = "成功"
    except Exception as err:
        msg = str(err)
        status = 600

    return jsonify({"msg": msg, "status": status}), status
    # return jsonify(request.get_json())


@app.route("/api/answer/nstptto/addall", methods=['POST'])
def add_nstptto_answer():
    # 连接数据库
    conn = sqlite3.connect('question.db', check_same_thread=False)
    cursor = conn.cursor()

    content = request.get_json()

    status = None
    msg = None

    try:
        cursor = conn.cursor()
        for row in content:
            SQL_TEXT = "insert into nstptto_answer(questionid,participant,interviewer,item,position_of_item,select_order,select_value,page,block,version) values('{0}', '{1}', '{2}', '{3}', {4}, {5}, '{6}', '{7}', '{8}', '{9}')".format(
                row['questionid'], row['participant'], row['interviewer'], row['item'], row['position_of_item'], row['select_order'], row['select_value'], row['page'], row['block'], row['version'])
            cursor.execute(SQL_TEXT)
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
    version = request.args.get('version')
    participant = request.args.get('participant')
    # 连接数据库
    conn = sqlite3.connect('question.db', check_same_thread=False)
    cursor = conn.cursor()

    SQL_TEXT = "select * from tto_answer"
    print(SQL_TEXT)

    if version is not None and version != "all":
        SQL_TEXT = SQL_TEXT + " " + "where version='{0}'".format(version)

    if participant is not None:
        if participant != "all":
            if re.search(r'select (.*) from (.*) where (.*)', SQL_TEXT.lower()) is None:
                SQL_TEXT = SQL_TEXT + " " + \
                    "where  participant='{0}'".format(participant)
            else:
                SQL_TEXT = SQL_TEXT + " " + \
                    "and  participant='{0}'".format(participant)

    result = cursor.execute(SQL_TEXT)
    data = []
    for row in result:
        data.append({"id": row[0], "questionid": row[1], "participant": row[2], "interviewer": row[3], "item": row[4], "position_of_item": row[5], "tto_value": row[6],
                     "used_time": row[7], "composite_switches": row[8], "resets": row[9], "number_of_moves": row[10], "block": row[11], "version": row[12], "created_timestamp": row[13]})

    return jsonify(data)


@app.route("/api/answer/newtto")
def get_newtto_answer():
    version = request.args.get('version')
    participant = request.args.get('participant')
    # 连接数据库
    conn = sqlite3.connect('question.db', check_same_thread=False)
    cursor = conn.cursor()

    SQL_TEXT = "select * from newtto_answer"
    print(SQL_TEXT)

    if version is not None and version != "all":
        SQL_TEXT = SQL_TEXT + " " + "where version='{0}'".format(version)

    if participant is not None:
        if participant != "all":
            if re.search(r'select (.*) from (.*) where (.*)', SQL_TEXT.lower()) is None:
                SQL_TEXT = SQL_TEXT + " " + \
                    "where  participant='{0}'".format(participant)
            else:
                SQL_TEXT = SQL_TEXT + " " + \
                    "and  participant='{0}'".format(participant)

    result = cursor.execute(SQL_TEXT)
    data = []
    for row in result:
        data.append({"id": row[0], "questionid": row[1], "participant": row[2], "interviewer": row[3], "item": row[4], "position_of_item": row[5], "start_year_random": row[6],
                     "select1": row[7], "select2": row[8], "select3": row[9], "select4": row[10], "open_select": row[11], "end_year_random": row[12], "block": row[13],"reset": row[14], "version": row[15], "created_timestamp": row[16]})

    return jsonify(data)


@app.route("/api/answer/nstptto")
def get_nstptto_answer():
    version = request.args.get('version')
    participant = request.args.get('participant')
    # 连接数据库
    conn = sqlite3.connect('question.db', check_same_thread=False)
    cursor = conn.cursor()

    SQL_TEXT = "select * from nstptto_answer"
    print(SQL_TEXT)

    if version is not None and version != "all":
        SQL_TEXT = SQL_TEXT + " " + "where version='{0}'".format(version)

    if participant is not None:
        if participant != "all":
            if re.search(r'select (.*) from (.*) where (.*)', SQL_TEXT.lower()) is None:
                SQL_TEXT = SQL_TEXT + " " + \
                    "where  participant='{0}'".format(participant)
            else:
                SQL_TEXT = SQL_TEXT + " " + \
                    "and  participant='{0}'".format(participant)

    result = cursor.execute(SQL_TEXT)
    data = []
    for row in result:
        data.append({"id": row[0], "questionid": row[1], "participant": row[2], "interviewer": row[3], "item": row[4], "position_of_item": row[5], "select_order": row[6],
                     "select_value": row[7], "page": row[8], "block": row[9], "version": row[10], "created_timestamp": row[11]})

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
    version = request.args.get('version')
    participant = request.args.get('participant')
    # 连接数据库
    conn = sqlite3.connect('question.db', check_same_thread=False)
    cursor = conn.cursor()

    SQL_TEXT = "select * from dce_answer"
    print(SQL_TEXT)

    if version is not None and version != "all":
        SQL_TEXT = SQL_TEXT + " " + "where version='{0}'".format(version)

    if participant is not None:
        if participant != "all":
            if re.search(r'select (.*) from (.*) where (.*)', SQL_TEXT.lower()) is None:
                SQL_TEXT = SQL_TEXT + " " + \
                    "where  participant='{0}'".format(participant)
            else:
                SQL_TEXT = SQL_TEXT + " " + \
                    "and  participant='{0}'".format(participant)

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
    version = request.args.get('version')
    participant = request.args.get('participant')
    # 连接数据库
    conn = sqlite3.connect('question.db', check_same_thread=False)
    cursor = conn.cursor()

    SQL_TEXT = "select * from opened_answer"
    print(SQL_TEXT)

    if version is not None and version != "all":
        SQL_TEXT = SQL_TEXT + " " + "where version='{0}'".format(version)

    if participant is not None:
        if participant != "all":
            if re.search(r'select (.*) from (.*) where (.*)', SQL_TEXT.lower()) is None:
                SQL_TEXT = SQL_TEXT + " " + \
                    "where  participant='{0}'".format(participant)
            else:
                SQL_TEXT = SQL_TEXT + " " + \
                    "and  participant='{0}'".format(participant)

    result = cursor.execute(SQL_TEXT)
    data = []
    for row in result:
        print(row)
        data.append({"id": row[0], "questionid": row[1], "participant": row[2], "interviewer": row[3], "item": row[4],
                     "position_of_item": row[5], "participant_answer": row[6], "block": row[7], "version": row[8], "created_timestamp": row[9]})

    return jsonify(data)


@app.route("/api/participant")
def get_all_participant():
    version = request.args.get('version')
    conn = sqlite3.connect('question.db', check_same_thread=False)
    cursor = conn.cursor()

    SQL_TEXT = """select t1.participant,t2.questionid,t3.questionid,t4.questionid,t5.questionid,t6.questionid,t7.questionid from (select distinct participant from dce_answer where version='{0}' 
                union select distinct participant from tto_answer where version='{0}' 
                union select distinct participant from ttofeedback_answer where version='{0}'
                union select distinct participant from opened_answer where version='{0}'
                union select distinct participant from nstptto_answer where version='{0}'
                union select distinct participant from newtto_answer where version='{0}') t1 
                left join (select distinct questionid,participant from dce_answer where version='{0}') t2 on t1.participant=t2.participant 
                left join (select distinct questionid,participant from tto_answer where version='{0}') t3 on t1.participant=t3.participant 
                left join (select distinct questionid,participant from ttofeedback_answer where version='{0}') t4 on t1.participant=t4.participant
                left join (select distinct questionid,participant from opened_answer where version='{0}') t5 on t1.participant=t5.participant
                left join (select distinct questionid,participant from nstptto_answer where version='{0}') t6 on t1.participant=t6.participant
                left join (select distinct questionid,participant from newtto_answer where version='{0}') t7 on t1.participant=t7.participant""".format(version)

    result = cursor.execute(SQL_TEXT)
    data = []

    for row in result:
        data.append({"participant": row[0], "DCE": row[1],
                     "TTO": row[2], "TTO_Feedback": row[3], "Opened": row[4], "NonStopping_TTO": row[5], "New_TTO": row[6]})

    return jsonify(data)


@app.route("/api/question/delete", methods=['POST'])
def delete_question():
    # 连接数据库
    conn = sqlite3.connect('question.db', check_same_thread=False)
    cursor = conn.cursor()

    version = request.get_json()["version"]
    questionid = request.get_json()["questionid"]

    print(version)
    print(questionid)

    status = None
    msg = None

    TABLE_NAME = ""
    SQL_TEXT = "delete from {0} where version='{1}'"

    if questionid == 1:
        TABLE_NAME = "dce_question"
    elif questionid == 2:
        TABLE_NAME = "tto_question"
    elif questionid == 3:
        TABLE_NAME = "ttofeedback_question"
    elif questionid == 4:
        TABLE_NAME = "opened_question"
    elif questionid == 5:
        TABLE_NAME = "nstptto_question"
    elif questionid == 6:
        TABLE_NAME = "newtto_question"

    SQL_TEXT = SQL_TEXT.format(TABLE_NAME, version)

    try:
        cursor.execute(SQL_TEXT)
        conn.commit()

        status = 200
        msg = "ok"
    except Exception as err:
        msg = "error"
        status = 600
        conn.rollback()
    finally:
        conn.close()

    return jsonify({"msg": msg, "status": status})


@app.route("/api/upload", methods=["POST"])
def upload_file():
    if request.method == 'POST':
        file = request.files.get('file')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)

            # 获取文件后缀
            file_suffix = filename.rsplit('.', 1)[1].lower()
            file_realname = filename.rsplit('.', 1)[0].lower()

            filename = file_realname + \
                str(time.strftime("%Y%m%d%H%M%S", time.localtime())) + \
                '.' + file_suffix
            file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
            print(os.path.join(app.config['UPLOAD_PATH'], filename))

            filepath = os.path.join(app.config['UPLOAD_PATH'], filename)
            # 连接数据库
            conn = sqlite3.connect('question.db', check_same_thread=False)
            cursor = conn.cursor()

            msg = ""
            status = ""

            try:
                # Interviewers
                for data in readexcel.read(filepath, 'interviewers', True):
                    cursor.execute("insert into interviewer(id, name,version) values({0},'{1}','{2}')".format(
                        data[0], data[1], data[2]))

                # TTO
                for data in readexcel.read(filepath, 'TTO & TTO-Feedback', True):
                    cursor.execute("insert into tto_question(questionid,presentation,type,name,block,source_text,version) values({0},'{1}','{2}','{3}','{4}','{5}','{6}')".format(
                        data[6], data[0], data[1], data[2], data[3], data[4], data[5]))

                # New TTO
                for data in readexcel.read(filepath, 'New TTO', True):
                    cursor.execute("insert into newtto_question(questionid,presentation,type,name,block,source_text,version) values({0},'{1}','{2}','{3}','{4}','{5}','{6}')".format(
                        data[6], data[0], data[1], data[2], data[3], data[4], data[5]))

                # Non-Stopping TTO
                for data in readexcel.read(filepath, 'Non-Stopping TTO', True):
                    cursor.execute("insert into nstptto_question(questionid,presentation,type,name,block,source_text,version) values({0},'{1}','{2}','{3}','{4}','{5}','{6}')".format(
                        data[6], data[0], data[1], data[2], data[3], data[4], data[5]))

                # TTO-Feedback Question
                for data in readexcel.read(filepath, 'TTO & TTO-Feedback', True):
                    cursor.execute("insert into ttofeedback_question(questionid,presentation,type,name,block,source_text,version) values({0},'{1}','{2}','{3}','{4}','{5}','{6}')".format(
                        data[6], data[0], data[1], data[2], data[3], data[4], data[5]))

                # DCE Question
                for data in readexcel.read(filepath, 'DCE', True):
                    cursor.execute("insert into dce_question(questionid,presentation,name,block,answer,source_text,version) values({0},'{1}','{2}','{3}','{4}','{5}','{6}')".format(
                        data[6], data[0], data[1], data[2], data[3], data[4], data[5]))

                # Open ended Question
                for data in readexcel.read(filepath, 'Open ended questions', True):
                    cursor.execute("insert into opened_question(questionid,presentation,name,block,source_text,version) values({0},'{1}','{2}','{3}','{4}','{5}')".format(
                        data[5], data[0], data[1], data[2], data[3], data[4]))
                conn.commit()
                msg = "ok"
                status = 200
            except:
                conn.rollback()
                if os.path.exists(filepath):
                    os.remove(filepath)
                msg = "failed"
                status = 500

    return jsonify({
        "status": status,
        "msg": msg
    })


# 访问上传的文件
# http://localhost:5000/download/<filename>.xlsx
@app.route('/download/<filename>/')
def get_file(filename):
    filepath = os.path.join(app.config['UPLOAD_PATH'], filename)
    if os.path.isfile(filepath):
        response = make_response(send_from_directory(
            app.config['UPLOAD_PATH'], filename, as_attachment=True))
        response.headers["content-disposition"] = "attachment; filename={}".format(
            filename)

        return response

# @app.after_request
# def after_request(response):
#     if str(request.path).startswith('/download/'):
#         response.headers['Content-Disposition'] = 'attachment'
#     return response


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


class Oracle:
    def __init__(self, username, password, host, port, instance, mode):
        """
        Function: __init__
        Summary: InsertHere
        Examples: InsertHere
        Attributes:
            @param (self):InsertHere
            @param (*args):InsertHere
            username: oracle user,
            password: oracle user's password,
            mod:  "normal, sysdba, sysoper",defaut is normal,
            host: the oracle database locates
            port: the port listen oracle database service, config is 1521
            insrance: the service name of the oracle database instance
        Returns: InsertHere
        """
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.instance = instance
        self.mode = mode

    def __connect(self):
        """
        Function: __connect
        Summary: InsertHere
        Examples: self.__connect()
        Attributes:
            @param (self):Call __connect metod Oracle.__connect()
        Returns: connection
        """
        if not cx_oracle_exists:
            msg = """The cx_Oracle module is required. 'pip install cx_Oracle' \
                should do the trick. If cx_Oracle is installed, make sure ORACLE_HOME \
                & LD_LIBRARY_PATH is set"""

        dsn = cx_Oracle.makedsn(
            host=self.host, port=self.port, service_name=self.instance)

        try:
            if self.mode == 'sysdba' or self.username == 'sys':
                self.connection = cx_Oracle.connect(self.username, self.password, dsn,
                                                    mode=cx_Oracle.SYSDBA)
            else:
                self.connection = cx_Oracle.connect(
                    self.username, self.password, dsn)

        except cx_Oracle.DatabaseError as cx_msg:
            msg = 'Could not connect to database: %s, dsn: %s ' % (cx_msg, dsn)
        return self.connection

    def __disconnect(self):
        try:
            self.cursor.close()
            self.connection.close()
        except cx_Oracle.DatabaseError as cx_msg:
            print(cx_msg)

    def select(self, sql, bindvars=''):
        """
        Given a valid SELECT statement, return the results from the database
        """

        results = None

        try:
            self.__connect()
            self.cursor = self.connection.cursor()
            self.cursor.execute(sql, bindvars)
            results = self.cursor.fetchall()
        except cx_Oracle.DatabaseError as cx_msg:
            print(cx_msg)
        finally:
            self.__disconnect()
        return results

    def execute(self, sql, bindvars='', commit=True):
        """
        Function: execute
        Summary: Execute whatever SQL statements are passed to the method;
            commit if specified. Do not specify fetchall() in here as
            the SQL statement may not be a select.
            bindvars is a dictionary of variables you pass to execute.
        Examples: Oracle().execute(...)
        Attributes:
            @param (self):class method
            @param (sql):The sql that will be excuted
            @param (bindvars) config='': The bind variables of sql
            @param (many) config=False: If set many is True, multiple sql will be excuted at the same time
            @param (commit) config=False: False is not needed commit after excuting sql, but True is needed commit, gernerally DML sql
        Returns: NO value will be returned
        """

        try:
            self.__connect()
            self.cursor = self.connection.cursor()
            self.cursor.execute(sql, bindvars)
            print(
                "The sql executing from database successfully and the sql is " + '"' + sql + '".')
        except cx_Oracle.DatabaseError as cx_msg:
            print(cx_msg)
        finally:
            # Only commit if it-s necessary.
            if commit:
                self.connection.commit()
            else:
                pass
            self.__disconnect()


@app.route("/api/ptraffic")
def get_passenger_traffic():
    starttime = request.args.get('start')
    endtime = request.args.get('end')

    if starttime is None:
        starttime = 0
    if endtime is None:
        endtime = 24
    oracle = Oracle(username='gdata', password='gdata',
                    mode="", host="10.50.0.212", port=1521, instance='gdata')
    sql_text = """select pdate,pentry,pin,pout,sysdate as gettime from (SELECT
        a.XF_DATE_TIME pdate,
        b.xf_passageway pentry,
            sum(a.xf_incount) pin,
            sum(a.xf_outcount) pout
        from 
        XF_new_TC_COUNTDATA a,
            XF_TC_PASS b 
        WHERE
        a.XF_CAMERAID=b.XF_CAMERAID and
        a.XF_CAMERAID NOT IN ('GHGY5500033011','GHGY5500033012','GHGY5500033013','GHGY5500033019','GHGY5500033020','GHGY5500033022','GHGY5500033023','GHGY5500033024','GHGY5500033025',
        'GHGY5500033033','GHGY5500033034','GHGY5500033035','GHGY5500033036','GHGY5500033040','GHGY5500033041','GHGY5500033042','GHGY5500033043','GHGY5500033046',
        'GHGY5500033047','GHGY5500033048','GHGY5500033049','GHGY5500033050','GHGY5500033051','GHGY5500033052','GHGY5500033053','GHGY5500033055','GHGY5500033056',
        'GHGY5500033057','GHGY5500033058','GHGY5500033059','GHGY5500033060','GHGY5500033061','GHGY5500033062','GHGY5500033073','GHGY5500033074','GHGY5500033076',
        'GHGY5500033077','GHGY5500033078','GHGY5500033082','GHGY5500033083','GHGY5500033084','GHGY5500033096','GHGY5500033097','GHGY5500033098','GHGY5500033099',
        'GHGY5500033100','GHGY5500033101','GHGY5500033104','GHGY5500033105','GHGY5500033106','GHGY5500033107','GHGY5500033108','GHGY5500033109','GHGY5500033110',
        'GHGY5500033111','GHGY5500033114','GHGY5500033117','GHGY5500033118','GHGY5500033119','GHGY5500033128','GHGY5500033133','GHGY5500033134','GHGY5500033135',
        'GHGY5500033138','GHGY5500033139','GHGY5500033145','GHGY5500033148','GHGY5500033149','GHGY5500033150','GHGY5500033151','GHGY5500033152','GHGY5500033153',
        'GHGY5500033162','GHGY5500033163','GHGY5500033175','GHGY5500033176','GHGY5500033177','GHGY5500033178','GHGY5500033181','GHGY5500033183','GHGY5500033184',
        'GHGY5500033185','GHGY5500033186','GHGY5500033187','GHGY5500033188','GHGY5500033189','GHGY5500033192','GHGY5500033193','GHGY5500033198','GHGY5500033199',
        'GHGY5500033200','GHGY5500033204','GHGY5500033205','GHGY5500033210','GHGY5500033211','GHGY5500033212','GHGY5500033213','GHGY5500033214','GHGY5500033215',
        'GHGY5500033216','GHGY5500033217','GHGY5500033218','GHGY5500033219','GHGY5500033220','GHGY5500033221','GHGY5500033228') AND
         to_date(a.XF_DATE_TIME,'yyyy-mm-dd') = to_date(to_char(sysdate,'yyyy-mm-dd'),'yyyy-mm-dd') and XF_STARTHOUR between {0} and {1}
        GROUP BY
        a.XF_DATE_TIME,b.xf_passageway
        order by a.XF_DATE_TIME)"""
    results = oracle.select(sql_text.format(starttime, endtime))

    data = []

    for row in results:
        print(row[1])
        data.append({
            "pdate": row[0],
            "pentry": row[1],
            "pin": row[2],
            "pout": row[3],
            "gettime": row[4]
        })

    return jsonify(data)


@app.route("/api/ptraffic/all")
def get_all_passenger_traffic():
    oracle = Oracle(username='gdata', password='gdata',
                    mode="", host="10.50.0.212", port=1521, instance='gdata')
    sql_text = """select pdate,pentry,pin,pout,sysdate as gettime from (SELECT
        a.XF_DATE_TIME pdate,
        b.xf_passageway pentry,
            sum(a.xf_incount) pin,
            sum(a.xf_outcount) pout
        from 
        XF_new_TC_COUNTDATA a,
            XF_TC_PASS b 
        WHERE
        a.XF_CAMERAID=b.XF_CAMERAID and
        a.XF_CAMERAID NOT IN ('GHGY5500033011','GHGY5500033012','GHGY5500033013','GHGY5500033019','GHGY5500033020','GHGY5500033022','GHGY5500033023','GHGY5500033024','GHGY5500033025',
        'GHGY5500033033','GHGY5500033034','GHGY5500033035','GHGY5500033036','GHGY5500033040','GHGY5500033041','GHGY5500033042','GHGY5500033043','GHGY5500033046',
        'GHGY5500033047','GHGY5500033048','GHGY5500033049','GHGY5500033050','GHGY5500033051','GHGY5500033052','GHGY5500033053','GHGY5500033055','GHGY5500033056',
        'GHGY5500033057','GHGY5500033058','GHGY5500033059','GHGY5500033060','GHGY5500033061','GHGY5500033062','GHGY5500033073','GHGY5500033074','GHGY5500033076',
        'GHGY5500033077','GHGY5500033078','GHGY5500033082','GHGY5500033083','GHGY5500033084','GHGY5500033096','GHGY5500033097','GHGY5500033098','GHGY5500033099',
        'GHGY5500033100','GHGY5500033101','GHGY5500033104','GHGY5500033105','GHGY5500033106','GHGY5500033107','GHGY5500033108','GHGY5500033109','GHGY5500033110',
        'GHGY5500033111','GHGY5500033114','GHGY5500033117','GHGY5500033118','GHGY5500033119','GHGY5500033128','GHGY5500033133','GHGY5500033134','GHGY5500033135',
        'GHGY5500033138','GHGY5500033139','GHGY5500033145','GHGY5500033148','GHGY5500033149','GHGY5500033150','GHGY5500033151','GHGY5500033152','GHGY5500033153',
        'GHGY5500033162','GHGY5500033163','GHGY5500033175','GHGY5500033176','GHGY5500033177','GHGY5500033178','GHGY5500033181','GHGY5500033183','GHGY5500033184',
        'GHGY5500033185','GHGY5500033186','GHGY5500033187','GHGY5500033188','GHGY5500033189','GHGY5500033192','GHGY5500033193','GHGY5500033198','GHGY5500033199',
        'GHGY5500033200','GHGY5500033204','GHGY5500033205','GHGY5500033210','GHGY5500033211','GHGY5500033212','GHGY5500033213','GHGY5500033214','GHGY5500033215',
        'GHGY5500033216','GHGY5500033217','GHGY5500033218','GHGY5500033219','GHGY5500033220','GHGY5500033221','GHGY5500033228') AND
         to_date(a.XF_DATE_TIME,'yyyy-mm-dd') = to_date(to_char(sysdate,'yyyy-mm-dd'),'yyyy-mm-dd')
        GROUP BY
        a.XF_DATE_TIME,b.xf_passageway
        order by a.XF_DATE_TIME)"""
    results = oracle.select(sql_text)

    data = []

    for row in results:
        print(row[1])
        data.append({
            "pdate": row[0],
            "pentry": row[1],
            "pin": row[2],
            "pout": row[3],
            "gettime": row[4]
        })

    return jsonify(data)



@app.route("/api/ptraffic/time")
def get_time_passenger_traffic():
    starttime = request.args.get('start')
    endtime = request.args.get('end')

    if starttime is None:
        starttime = 0
    if endtime is None:
        endtime = 24
    oracle = Oracle(username='gdata', password='gdata',
                    mode="", host="10.50.0.212", port=1521, instance='gdata')
    sql_text = """SELECT
        min(xf_starthour)||':'||'00'||'-'||max(xf_starthour)||':'||'00' 时间段,
        nvl(sum(case
        when XF_CAMERAID in 
            ('GHGY5500033140','GHGY5500033141','GHGY5500033142','GHGY5500033143','GHGY5500033144','GHGY5500033147',
            'GHGY5500033155','GHGY5500033156','GHGY5500033157','GHGY5500033158','GHGY5500033159',
            'GHGY5500033169','GHGY5500033170','GHGY5500033171','GHGY5500033172','GHGY5500033173','GHGY5500033174','GHGY5500033168')
            then XF_INCOUNT  
            end),0) "沿湖广场",
        nvl(sum(case
        when XF_CAMERAID in 
            ('GHGY5500033026','GHGY5500033027','GHGY5500033028','GHGY5500033029','GHGY5500033030','GHGY5500033031','GHGY5500033032',
            'GHGY5500033089','GHGY5500033090','GHGY5500033091','GHGY5500033092','GHGY5500033093','GHGY5500033094','GHGY5500033095')
            then XF_INCOUNT 
            end),0) "H&M",
        nvl(sum(case
        when XF_CAMERAID in 
            ('GHGY5500033230','GHGY5500033229','GHGY5500033196','GHGY5500033197')
            then XF_INCOUNT  
            end),0) "人行天桥",
        nvl(sum(case
        when XF_CAMERAID in 
            ('GHGY5500033002','GHGY5500033003','GHGY5500033004','GHGY5500033005','GHGY5500033006','GHGY5500033007','GHGY5500033008','GHGY5500033009','GHGY5500033010',
            'GHGY5500033014','GHGY5500033015','GHGY5500033016','GHGY5500033017','GHGY5500033018')
            then XF_INCOUNT  
            end),0) "停车场",
        nvl(sum(case
        when XF_CAMERAID in
            ('GHGY5500033002','GHGY5500033003','GHGY5500033004','GHGY5500033005','GHGY5500033006','GHGY5500033007','GHGY5500033008','GHGY5500033009','GHGY5500033010',
            'GHGY5500033014','GHGY5500033015','GHGY5500033016','GHGY5500033017','GHGY5500033018',
            'GHGY5500033026','GHGY5500033027','GHGY5500033028','GHGY5500033029','GHGY5500033030','GHGY5500033031','GHGY5500033032',
            'GHGY5500033089','GHGY5500033090','GHGY5500033091','GHGY5500033092','GHGY5500033093','GHGY5500033094','GHGY5500033095',
            'GHGY5500033140','GHGY5500033141','GHGY5500033142','GHGY5500033143','GHGY5500033144','GHGY5500033147',
            'GHGY5500033155','GHGY5500033156','GHGY5500033157','GHGY5500033158','GHGY5500033159',
            'GHGY5500033169','GHGY5500033170','GHGY5500033171','GHGY5500033172','GHGY5500033173','GHGY5500033174','GHGY5500033168',
            'GHGY5500033230','GHGY5500033229','GHGY5500033196','GHGY5500033197')
            then XF_INCOUNT  
            end),0) "共计"
        from 
        xf_tc_countdata
        WHERE
        xf_starthour between 10 and 22 and
        to_date(XF_DATE_TIME,'yyyy-mm-dd') between to_date({0},'yyyy-mm-dd') and to_Date({1},'yyyy-mm-dd')
        """
    results = oracle.select(sql_text.format(starttime, endtime))

    data = []

    for row in results:
        print(row[1])
        data.append({
            "pdate": row[0],
            "psquare": row[1],
            "phm": row[2],
            "pgateway": row[3],
            "pparking": row[4],
            "pall": row[5]
        })

    return jsonify(data)


if __name__ == "__main__":
    # init_db()
    app.run(host="0.0.0.0", debug=True)
