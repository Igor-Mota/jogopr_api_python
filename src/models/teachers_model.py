import json
from .connection import connect
from mysql.connector import Error

def create_new_teacher(values):
    con  = connect()
    cursor = con.cursor()
    sql = 'INSERT INTO teachers_table (id,name,matter,permission) VALUES (%s,%s,%s,%s)'
    values = (24,values['name'] , values['matter'],1)
    try:
        cursor.execute(sql,values)
        con.commit()
        cursor.close()
        con.close()
        return 'Sucess'
    except Error as error:
        return 'Error' + error

def get_all_teachers():
    con  = connect()
    cursor = con.cursor()
    teachers = []
    try:
        cursor.execute('select * from teachers_table')
        records = cursor.fetchall()
        cursor.close()
        con.close()
        for record in records:
            json = '{"id":"'+str(record[0])+'","name":"'+record[1]+'","materia":"'+record[2]+'","type":"'+str(record[3])+'"}'
            teachers.append(json)
        return teachers
    except Error as error:
        return 'Error' + error