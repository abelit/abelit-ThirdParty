# coding:utf8
from flask import Flask, request, jsonify, render_template, send_from_directory, send_file, make_response
from flask_cors import CORS
# import sqlite3
import pymysql
import os
import re
import readexcel
import json
import time
from werkzeug.utils import secure_filename

# # Import module cx_Oracle to connect oracle using python
# try:
#     import cx_Oracle
# except ImportError:
#     cx_oracle_exists = False
# else:
#     cx_oracle_exists = True


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

ALLOWED_EXTENSIONS = {'xls', 'xlsx'}
UPLOAD_PATH = os.path.join(os.path.dirname(__file__), 'data')
app.config['UPLOAD_PATH'] = UPLOAD_PATH

app.config['adminpwd'] = "Passw0rd123!"

app.config['JSON_SORT_KEYS'] = False

# DB Settings
DBHOST="{DBHOST}"
DBUSER="{DBUSER}"
DBPASS="{DBPASS}"
DBNAME="{DBNAME}"

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

    # os.remove('question.db')

    # 连接数据库
    # conn = sqlite3.connect('question.db', check_same_thread=False)
    conn = pymysql.connect(DBHOST,DBUSER,DBPASS,DBNAME)

    # all_table_text = "SELECT lower(name),sql FROM sqlite_master WHERE type='table' ORDER BY 1"
    # all_table_text = "select table_name from information_schema.tables where table_schema='eqdb'"
    cursor = conn.cursor()

    # result = cursor.execute(all_table_text)
    # print(result)
    result = ["interviewer","eq_question_version","eq_label","tto_question","newtto_question","nstptto_question",
    "ttofeedback_question","dce_question","opened_question","dce_answer","tto_answer","newtto_answer","nstptto_answer","ttofeedback_answer","opened_answer"]

    for table in result:
        cursor.execute("drop table if exists {0}".format(table))

    # # create tables
    # SQL_TEXT = ["create table interviewer(id integer, name text,version text, created_timestamp timestamp default (datetime(current_timestamp, 'localtime')))",
    #             "create table eq_question_version(id integer primary key autoincrement, version text, created_timestamp timestamp default (datetime(current_timestamp, 'localtime')))",
    #             "create table eq_label(id integer primary key autoincrement,questionid integer, reference_id text,slide text,presentation text,en_source_text text,zh_source_text text,version text,created_timestamp timestamp default  current_timestamp)",
    #             "create table tto_question(id integer primary key autoincrement,questionid integer, presentation text,type text, name text,block text,source_text text,version text,created_timestamp timestamp default (datetime(current_timestamp, 'localtime')))",
    #             "create table newtto_question(id integer primary key autoincrement,questionid integer, presentation text,type text, name text,block text,source_text text,version text,created_timestamp timestamp default (datetime(current_timestamp, 'localtime')))",
    #             "create table nstptto_question(id integer primary key autoincrement,questionid integer, presentation text,type text, name text,block text,source_text text,version text,created_timestamp timestamp default (datetime(current_timestamp, 'localtime')))",
    #             "create table ttofeedback_question(id integer primary key autoincrement,questionid integer, presentation text,type text, name text,block text,source_text text,version text,created_timestamp timestamp default (datetime(current_timestamp, 'localtime')))",
    #             "create table dce_question(id integer primary key autoincrement,questionid integer,presentation text,name integer,block text,answer text,source_text text, version text,created_timestamp timestamp default (datetime(current_timestamp, 'localtime')))",
    #             "create table opened_question(id integer primary key autoincrement,questionid integer,presentation text,name text,block text,source_text text, version text, created_timestamp timestamp default (datetime(current_timestamp, 'localtime')))",
    #             "create table dce_answer(id integer primary key autoincrement,questionid integer,participant text,interviewer text,item integer, position_of_item integer,selected_state text,dce_reversal text,block text,used_time text, version text,created_timestamp timestamp default (datetime(current_timestamp, 'localtime')))",
    #             "create table tto_answer(id integer primary key autoincrement,questionid integer, participant text, interviewer text,item text,position_of_item integer,tto_value real,used_time text,composite_switches integer,resets integer,number_of_moves integer,block text,version text,created_timestamp timestamp default (datetime(current_timestamp, 'localtime')))",
    #             "create table newtto_answer(id integer primary key autoincrement,questionid integer, participant text, interviewer text,item text,position_of_item integer,start_year_random text,select1 text,select2 text,select3 text,select4 text,open_select text,end_year_random text,block text,reset text,used_time text,version text,created_timestamp timestamp default (datetime(current_timestamp, 'localtime')))",
    #             "create table nstptto_answer(id integer primary key autoincrement,questionid integer, participant text, interviewer text,item text,position_of_item integer,select_order integer,select_value text,page integer,block text,reset text,used_time text,version text,created_timestamp timestamp default (datetime(current_timestamp, 'localtime')))",
    #             "create table ttofeedback_answer(id integer primary key autoincrement,questionid integer, participant text, interviewer text,item text,position_of_item integer,tto_value real,used_time text,composite_switches integer,resets integer,number_of_moves integer,block text,version text,created_timestamp timestamp default (datetime(current_timestamp, 'localtime')))",
    #             "create table opened_answer(id integer primary key autoincrement,questionid integer, participant text,interviewer text,item text,position_of_item integer,participant_answer text,block text, version text,created_timestamp timestamp default (datetime(current_timestamp, 'localtime')))"]

       # create tables
    SQL_TEXT = ["create table interviewer(id integer, name varchar(200),version varchar(200), created_timestamp timestamp default now())",
                "create table eq_question_version(id integer primary key auto_increment, version varchar(200), created_timestamp timestamp default now())",
                "create table eq_label(id integer primary key auto_increment,questionid integer, reference_id varchar(200),slide varchar(200),presentation varchar(200),en_source_text varchar(4000),zh_source_text varchar(4000),version varchar(200),created_timestamp timestamp default  current_timestamp)",
                "create table tto_question(id integer primary key auto_increment,questionid integer, presentation varchar(200),type varchar(200), name varchar(200),block varchar(200),source_text varchar(200),version varchar(200),created_timestamp timestamp default now())",
                "create table newtto_question(id integer primary key auto_increment,questionid integer, presentation varchar(200),type varchar(200), name varchar(200),block varchar(200),source_text varchar(200),version varchar(200),created_timestamp timestamp default now())",
                "create table nstptto_question(id integer primary key auto_increment,questionid integer, presentation varchar(200),type varchar(200), name varchar(200),block varchar(200),source_text varchar(200),version varchar(200),created_timestamp timestamp default now())",
                "create table ttofeedback_question(id integer primary key auto_increment,questionid integer, presentation varchar(200),type varchar(200), name varchar(200),block varchar(200),source_text varchar(200),version varchar(200),created_timestamp timestamp default now())",
                "create table dce_question(id integer primary key auto_increment,questionid integer,presentation varchar(200),name integer,block varchar(200),answer varchar(200),source_text varchar(200), version varchar(200),created_timestamp timestamp default now())",
                "create table opened_question(id integer primary key auto_increment,questionid integer,presentation varchar(200),name varchar(200),block varchar(200),source_text varchar(200), version varchar(200), created_timestamp timestamp default now())",
                "create table dce_answer(id integer primary key auto_increment,questionid integer,participant varchar(200),interviewer varchar(200),item integer, position_of_item integer,selected_state varchar(200),dce_reversal varchar(200),block varchar(200),used_time varchar(200), version varchar(200),created_timestamp timestamp default now())",
                "create table tto_answer(id integer primary key auto_increment,questionid integer, participant varchar(200), interviewer varchar(200),item varchar(200),position_of_item integer,tto_value float,used_time varchar(200),composite_switches integer,resets integer,number_of_moves integer,block varchar(200),version varchar(200),created_timestamp timestamp default now())",
                "create table newtto_answer(id integer primary key auto_increment,questionid integer, participant varchar(200), interviewer varchar(200),item varchar(200),position_of_item integer,start_year_random varchar(200),select1 varchar(200),select2 varchar(200),select3 varchar(200),select4 varchar(200),open_select varchar(200),end_year_random varchar(200),block varchar(200),reset varchar(200),used_time varchar(200),version varchar(200),created_timestamp timestamp default now())",
                "create table nstptto_answer(id integer primary key auto_increment,questionid integer, participant varchar(200), interviewer varchar(200),item varchar(200),position_of_item integer,select_order integer,select_value varchar(200),page integer,block varchar(200),reset varchar(200),used_time varchar(200),version varchar(200),created_timestamp timestamp default now())",
                "create table ttofeedback_answer(id integer primary key auto_increment,questionid integer, participant varchar(200), interviewer varchar(200),item varchar(200),position_of_item integer,tto_value float,used_time varchar(200),composite_switches integer,resets integer,number_of_moves integer,block varchar(200),version varchar(200),created_timestamp timestamp default now())",
                "create table opened_answer(id integer primary key auto_increment,questionid integer, participant varchar(200),interviewer varchar(200),item varchar(200),position_of_item integer,participant_answer varchar(200),block varchar(200), version varchar(200),created_timestamp timestamp default now())"]

    for sql in SQL_TEXT:
        cursor.execute(sql)

    # Insert Data
    # interviewer Question
    # for data in readexcel.read('./data/questions.xlsx', 'interviewers', True):
    #     cursor.execute(
    #         "insert into interviewer(id, name,version) values({0},'{1}','{2}')".format(data[0], data[1],data[2]))
    # conn.commit()

    # EQ Label
    for item in ["TTO", "TTO-Feedback", "DCE", "Background Questions", "Non-Stopping TTO", "Open TTO"]:
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

    # result = cursor.execute(all_table_text)
    # table_list = []

    # for table in result:
    #     table_list.append({"name": table[0], "sql": table[1]})

    # cursor.close()
    # conn.close()
    return jsonify({"status": 200, "msg": "Reinit database successfully!", "tables": result})


@app.route("/api/question/version")
def get_question_version():
    # conn = sqlite3.connect('question.db', check_same_thread=False)
    conn = pymysql.connect(DBHOST,DBUSER,DBPASS,DBNAME)
    cursor = conn.cursor()

    SQL_TEXT = "select distinct version from dce_question union select distinct version from tto_question union select distinct version from opened_question union select distinct version from nstptto_question union select distinct version from newtto_question"
    cursor.execute(SQL_TEXT)
    result = cursor.fetchall() 

    data = []

    for row in result:
        data.append({
            "version": row[0]
        })

    return jsonify(data)


@app.route("/api/answer/version")
def get_answer_version():
    # conn = sqlite3.connect('question.db', check_same_thread=False)
    conn = pymysql.connect(DBHOST,DBUSER,DBPASS,DBNAME)
    cursor = conn.cursor()

    SQL_TEXT = """select distinct version from dce_answer
    union select distinct version from tto_answer
    union select distinct version from opened_answer
    union select distinct version from ttofeedback_answer
    union select distinct version from nstptto_answer
    union select distinct version from newtto_answer"""

    cursor.execute(SQL_TEXT)
    result = cursor.fetchall() 

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
#         msg = str(err)
#         status = 600

#     return jsonify({"msg": msg, "status": status})


@app.route("/api/interviewer")
def get_interviewer():
    version = request.args.get('version')

    # conn = sqlite3.connect('question.db', check_same_thread=False)
    conn = pymysql.connect(DBHOST,DBUSER,DBPASS,DBNAME)
    cursor = conn.cursor()

    SQL_TEXT = "select id, name,version,created_timestamp from interviewer"

    if version is not None and version != "all":
        SQL_TEXT = SQL_TEXT + " " + "where version='{0}'".format(version)

    cursor.execute(SQL_TEXT)
    result = cursor.fetchall() 

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

    # conn = sqlite3.connect('question.db', check_same_thread=False)
    conn = pymysql.connect(DBHOST,DBUSER,DBPASS,DBNAME)
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

    cursor.execute(SQL_TEXT)
    result = cursor.fetchall() 

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
    # conn = sqlite3.connect('question.db', check_same_thread=False)
    conn = pymysql.connect(DBHOST,DBUSER,DBPASS,DBNAME)
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
    cursor.execute(SQL_TEXT)
    result = cursor.fetchall() 

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
    # conn = sqlite3.connect('question.db', check_same_thread=False)
    conn = pymysql.connect(DBHOST,DBUSER,DBPASS,DBNAME)
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

    cursor.execute(SQL_TEXT)
    result = cursor.fetchall() 

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
    # conn = sqlite3.connect('question.db', check_same_thread=False)
    conn = pymysql.connect(DBHOST,DBUSER,DBPASS,DBNAME)
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
    cursor.execute(SQL_TEXT)
    result = cursor.fetchall() 

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
    # conn = sqlite3.connect('question.db', check_same_thread=False)
    conn = pymysql.connect(DBHOST,DBUSER,DBPASS,DBNAME)
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

    cursor.execute(SQL_TEXT)
    result = cursor.fetchall() 

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
    # conn = sqlite3.connect('question.db', check_same_thread=False)
    conn = pymysql.connect(DBHOST,DBUSER,DBPASS,DBNAME)
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
    cursor.execute(SQL_TEXT)
    result = cursor.fetchall() 

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
    # conn = sqlite3.connect('question.db', check_same_thread=False)
    conn = pymysql.connect(DBHOST,DBUSER,DBPASS,DBNAME)
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

    cursor.execute(SQL_TEXT)
    result = cursor.fetchall() 

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
    # conn = sqlite3.connect('question.db', check_same_thread=False)
    conn = pymysql.connect(DBHOST,DBUSER,DBPASS,DBNAME)
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

    SQL_TEXT += ' order by 1'

    cursor.execute(SQL_TEXT)
    result = cursor.fetchall() 

    blocks = []

    for row in result:
        blocks.append(row[0])

    return jsonify(blocks)


@app.route("/api/answer/tto/addall", methods=['POST'])
def add_tto_answer():
    # 连接数据库
    # conn = sqlite3.connect('question.db', check_same_thread=False)
    conn = pymysql.connect(DBHOST,DBUSER,DBPASS,DBNAME)
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
        msg = str(err)
        status = 600

    return jsonify({"msg": msg, "status": status})
    # return jsonify(request.get_json())


@app.route("/api/answer/newtto/addall", methods=['POST'])
def add_newtto_answer():
    # 连接数据库
    # conn = sqlite3.connect('question.db', check_same_thread=False)
    conn = pymysql.connect(DBHOST,DBUSER,DBPASS,DBNAME)
    cursor = conn.cursor()

    content = request.get_json()

    print(content)

    status = None
    msg = None

    try:
        cursor = conn.cursor()
        for row in content:
            SQL_TEXT = "insert into newtto_answer(questionid,participant,interviewer,item,position_of_item,start_year_random,select1,select2,select3,select4,end_year_random,open_select,block,reset,used_time,version) values('{0}', '{1}', '{2}', '{3}', {4}, {5}, '{6}', '{7}', '{8}', '{9}', '{10}', '{11}','{12}','{13}','{14}','{15}')".format(
                row['questionid'], row['participant'], row['interviewer'], row['item'], row['position_of_item'], row['start_year_random'], row['select1'], row['select2'], row['select3'], row['select4'], row['end_year_random'], row['open_select'], row['block'],row['reset'], row['used_time'], row['version'])
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
    # conn = sqlite3.connect('question.db', check_same_thread=False)
    conn = pymysql.connect(DBHOST,DBUSER,DBPASS,DBNAME)
    cursor = conn.cursor()

    content = request.get_json()

    status = None
    msg = None

    try:
        cursor = conn.cursor()
        for row in content:
            SQL_TEXT = "insert into nstptto_answer(questionid,participant,interviewer,item,position_of_item,select_order,select_value,page,block,reset,used_time,version) values('{0}', '{1}', '{2}', '{3}', {4}, {5}, '{6}', '{7}', '{8}', '{9}','{10}','{11}')".format(
                row['questionid'], row['participant'], row['interviewer'], row['item'], row['position_of_item'], row['select_order'], row['select_value'], row['page'], row['block'],row['reset'], row['used_time'], row['version'])
            cursor.execute(SQL_TEXT)
        conn.commit()
        conn.close()
        status = 200
        msg = "成功"
    except Exception as err:
        msg = str(err)
        status = 600

    return jsonify({"msg": msg, "status": status})
    # return jsonify(request.get_json())


@app.route("/api/answer/tto")
def get_tto_answer():
    version = request.args.get('version')
    participant = request.args.get('participant')
    # 连接数据库
    # conn = sqlite3.connect('question.db', check_same_thread=False)
    conn = pymysql.connect(DBHOST,DBUSER,DBPASS,DBNAME)
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

    cursor.execute(SQL_TEXT)
    result = cursor.fetchall() 
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
    # conn = sqlite3.connect('question.db', check_same_thread=False)
    conn = pymysql.connect(DBHOST,DBUSER,DBPASS,DBNAME)
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

    cursor.execute(SQL_TEXT)
    result = cursor.fetchall() 
    data = []
    for row in result:
        data.append({"id": row[0], "questionid": row[1], "participant": row[2], "interviewer": row[3], "item": row[4], "position_of_item": row[5], "start_year_random": row[6],
                     "select1": row[7], "select2": row[8], "select3": row[9], "select4": row[10], "open_select": row[11], "end_year_random": row[12], "block": row[13],"reset": row[14],"used_time": row[15], "version": row[16], "created_timestamp": row[17]})

    return jsonify(data)


@app.route("/api/answer/nstptto")
def get_nstptto_answer():
    version = request.args.get('version')
    participant = request.args.get('participant')
    # 连接数据库
    # conn = sqlite3.connect('question.db', check_same_thread=False)
    conn = pymysql.connect(DBHOST,DBUSER,DBPASS,DBNAME)
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

    cursor.execute(SQL_TEXT)
    result = cursor.fetchall() 
    data = []
    for row in result:
        data.append({"id": row[0], "questionid": row[1], "participant": row[2], "interviewer": row[3], "item": row[4], "position_of_item": row[5], "select_order": row[6],
                     "select_value": row[7], "page": row[8], "block": row[9],"reset": row[10],"used_time": row[11], "version": row[12], "created_timestamp": row[13]})

    return jsonify(data)


@app.route("/api/answer/dce/addall", methods=['POST'])
def add_dce_answer():
    # 连接数据库
    # conn = sqlite3.connect('question.db', check_same_thread=False)
    conn = pymysql.connect(DBHOST,DBUSER,DBPASS,DBNAME)
    cursor = conn.cursor()

    content = request.get_json()

    status = None
    msg = None

    print(content)

    try:
        cursor = conn.cursor()
        for row in content:
            SQL_TEXT = "insert into dce_answer(questionid,participant,interviewer,item,position_of_item,selected_state,dce_reversal,block,used_time,version) values('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}','{9}')".format(
                row['questionid'], row['participant'], row['interviewer'], row['item'], row['position_of_item'], row['selected_state'], row['dce_reversal'], row['block'],row['used_time'], row['version'])
            cursor.execute(SQL_TEXT)
            print(SQL_TEXT)
        conn.commit()
        conn.close()
        status = 200
        msg = "成功"
    except Exception as err:
        msg = str(err)
        status = 600

    return jsonify({"msg": msg, "status": status})
    # return jsonify(request.get_json())


@app.route("/api/answer/dce")
def get_dce_answer():
    version = request.args.get('version')
    participant = request.args.get('participant')
    # 连接数据库
    # conn = sqlite3.connect('question.db', check_same_thread=False)
    conn = pymysql.connect(DBHOST,DBUSER,DBPASS,DBNAME)
    cursor = conn.cursor()

    SQL_TEXT = "select * from dce_answer"


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
    cursor.execute(SQL_TEXT)
    result = cursor.fetchall() 
    data = []
    for row in result:
        print(row)
        data.append({"id": row[0], "questionid": row[1], "participant": row[2], "interviewer": row[3], "item": row[4], "position_of_item": row[5],
                     "selected_state": row[6], "dce_reversal": row[7], "block": row[8], "used_time": row[9], "version": row[10], "created_timestamp": row[11]})

    return jsonify(data)


@app.route("/api/answer/open/addall", methods=['POST'])
def add_open_answer():
    # 连接数据库
    # conn = sqlite3.connect('question.db', check_same_thread=False)
    conn = pymysql.connect(DBHOST,DBUSER,DBPASS,DBNAME)
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
        msg = str(err)
        status = 600

    return jsonify({"msg": msg, "status": status})
    # return jsonify(request.get_json())


@app.route("/api/answer/open")
def get_open_answer():
    version = request.args.get('version')
    participant = request.args.get('participant')
    # 连接数据库
    # conn = sqlite3.connect('question.db', check_same_thread=False)
    conn = pymysql.connect(DBHOST,DBUSER,DBPASS,DBNAME)
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

    cursor.execute(SQL_TEXT)
    result = cursor.fetchall() 
    data = []
    for row in result:
        print(row)
        data.append({"id": row[0], "questionid": row[1], "participant": row[2], "interviewer": row[3], "item": row[4],
                     "position_of_item": row[5], "participant_answer": row[6], "block": row[7], "version": row[8], "created_timestamp": row[9]})

    return jsonify(data)


@app.route("/api/participant")
def get_all_participant():
    version = request.args.get('version')
    # conn = sqlite3.connect('question.db', check_same_thread=False)
    conn = pymysql.connect(DBHOST,DBUSER,DBPASS,DBNAME)
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

    cursor.execute(SQL_TEXT)
    result = cursor.fetchall() 
    data = []

    for row in result:
        data.append({"participant": row[0], "DCE": row[1],
                     "TTO": row[2], "TTO_Feedback": row[3], "Background_Questions": row[4], "NonStopping_TTO": row[5], "Open_TTO": row[6]})

    return jsonify(data)


@app.route("/api/question/delete", methods=['POST'])
def delete_question():
    # 连接数据库
    # conn = sqlite3.connect('question.db', check_same_thread=False)
    conn = pymysql.connect(DBHOST,DBUSER,DBPASS,DBNAME)
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
            # conn = sqlite3.connect('question.db', check_same_thread=False)
            conn = pymysql.connect(DBHOST,DBUSER,DBPASS,DBNAME)
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
                        data[6], data[0], data[1], data[2], str(data[3]), data[4], data[5]))

                # New TTO
                for data in readexcel.read(filepath, 'Open TTO', True):
                    cursor.execute("insert into newtto_question(questionid,presentation,type,name,block,source_text,version) values({0},'{1}','{2}','{3}','{4}','{5}','{6}')".format(
                        data[6], data[0], data[1], data[2], str(data[3]), data[4], data[5]))

                # Non-Stopping TTO
                for data in readexcel.read(filepath, 'Non-Stopping TTO', True):
                    cursor.execute("insert into nstptto_question(questionid,presentation,type,name,block,source_text,version) values({0},'{1}','{2}','{3}','{4}','{5}','{6}')".format(
                        data[6], data[0], data[1], data[2], str(data[3]), data[4], data[5]))

                # TTO-Feedback Question
                for data in readexcel.read(filepath, 'TTO & TTO-Feedback', True):
                    cursor.execute("insert into ttofeedback_question(questionid,presentation,type,name,block,source_text,version) values({0},'{1}','{2}','{3}','{4}','{5}','{6}')".format(
                        data[6], data[0], data[1], data[2], str(data[3]), data[4], data[5]))

                # DCE Question
                for data in readexcel.read(filepath, 'DCE', True):
                    print(data[2])
                    cursor.execute("insert into dce_question(questionid,presentation,name,block,answer,source_text,version) values({0},'{1}','{2}','{3}','{4}','{5}','{6}')".format(
                        data[6], data[0], data[1], str(data[2]), data[3], data[4], data[5]))

                # Open ended Question
                for data in readexcel.read(filepath, 'Background Questions', True):
                    cursor.execute("insert into opened_question(questionid,presentation,name,block,source_text,version) values({0},'{1}','{2}','{3}','{4}','{5}')".format(
                        data[5], data[0], data[1], str(data[2]), data[3], data[4]))
                conn.commit()
                msg = "ok"
                status = 200
            except Exception as err:
                print(err)
                conn.rollback()
                if os.path.exists(filepath):
                    os.remove(filepath)
                msg = "failed"
                status = 500

    return jsonify({
        "status": status,
        "msg": msg
    }), status


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


if __name__ == "__main__":
    # init_db()
    app.run(host="0.0.0.0", debug=True)
