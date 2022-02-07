import json
from .connection import connect
from mysql.connector import Error


def get_a_teacher(email):
    con = connect()
    cursor = con.cursor()
    sql__check = str('select * from teachers where email = "{}"').format(email)
    cursor.execute(sql__check)
    records = cursor.fetchall()

    return records


def create_new_teacher(name, password_hash, email):
    con = connect()
    cursor = con.cursor()

    sql_insert = 'INSERT INTO teachers (name, password, email) VALUES (%s, %s, %s)'
    values = (name, password_hash, email)
    try:
        verify = get_a_teacher(email)
        if len(verify) > 0:
            return 'Usuario ja existe'
        else:
            cursor.execute(sql_insert, values)
            con.commit()
            cursor.close()
            con.close()
            return get_a_teacher(email)
    except Error as error:
        return 'Error' + error


def get_all_teachers():
    con = connect()
    cursor = con.cursor()
    try:
        cursor.execute('select * from teachers')
        records = cursor.fetchall()
        cursor.close()
        con.close()

        return records
    except Error as error:
        return 'Error' + error
