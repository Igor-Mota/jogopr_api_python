import json
from .connection import connect
from mysql.connector import Error


def get_a_teacher(name):
    con = connect()
    cursor = con.cursor()
    sql__check = str('select * from teachers where name = "{}"').format(name)
    cursor.execute(sql__check)
    records = cursor.fetchall()

    return records


def create_new_teacher(name, password_hash):
    con = connect()
    cursor = con.cursor()

    sql_insert = 'INSERT INTO teachers (name, password) VALUES (%s, %s)'
    values = (name, password_hash)
    try:
        verify = get_a_teacher(name)
        if len(verify) > 0:
            return 'Usuario ja existe'
        else:
            cursor.execute(sql_insert, values)
            con.commit()
            cursor.close()
            con.close()
            return get_a_teacher(name)
    except Error as error:
        return 'Error' + error


def get_all_teachers():
    con = connect()
    cursor = con.cursor()
    teachers = []
    try:
        cursor.execute('select * from teachers')
        records = cursor.fetchall()
        cursor.close()
        con.close()
        for record in records:
            json = '{"id":"'+str(record[0])+'","name":"'+record[1] + \
                '","materia":"'+record[2]+'","type":"'+str(record[3])+'"}'
            teachers.append(json)
        return teachers
    except Error as error:
        return 'Error' + error
