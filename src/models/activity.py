from .connection import connect


def get_a_activity(act_id):
    con = connect()
    cursor = con.cursor()

    cursor.execute('select * from activityes where id = "{}"'.format(act_id))
    records = cursor.fetchall()
    return records


def create_activity(data, code):

    con = connect()
    cursor = con.cursor()
    body = data['body']
    headers = data['headers']
    sql = 'INSERT INTO activityes(subject, matter, 	series, qtds_groups, show_author,punctuation_type, teacher_id, code) values("%s","%s","%s","%s","%s","%s","%s","%s")'
    cursor.execute(sql, (body['subject'], body['matter'], body['series'],
                   body['qtds_groups'], body['show_author'], body['punctuation_type'], headers['id'], code[0]))
    con.commit()

    created = get_a_activity(cursor.lastrowid)
    cursor.close()
    con.close()

    return created


def get_a_activity_from_code(code):
    con = connect()
    cursor = con.cursor()

    cursor.execute('select * from activityes where code = "{}"'.format(code))
    records = cursor.fetchall()
    return records
