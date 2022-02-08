from .connection import connect
from mysql.connector import Error


def get_question(_id):
    print(_id)
    con = connect()
    cursor = con.cursor()

    cursor.execute('select * from questions where id = "{}"'.format(_id))
    records = cursor.fetchall()
    return records


def create_a_question(data, _id):
    con = connect()
    cursor = con.cursor()

    sql = 'INSERT INTO questions (question, answer_1, answer_2, answer_3, correct,activitye_key) VALUES ("%s","%s","%s","%s","%s", "%s")'
    cursor.execute(sql, (data['question'], data['answer_1'],
                   data['answer_2'], data['answer_3'], data['correct'], _id[0]))
    con.commit()
    created = get_question(cursor.lastrowid)
    cursor.close()
    con.close()

    return created
