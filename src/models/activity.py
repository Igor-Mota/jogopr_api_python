from .connection import connect


def get_a_activity(act_id):
    con = connect()
    cursor = con.cursor()

    cursor.execute('select * from activityes where id = "{}"'.format(act_id))
    records = cursor.fetchall()
    return records


def create_activity(data):

    con = connect()
    cursor = con.cursor()
    body = data['body']
    headers = data['headers']
    sql = 'INSERT INTO activityes(subject, matter, 	series, qtds_groups, show_author,punctuation_type, teacher_id) values("%s","%s","%s","%s","%s","%s","%s")'
    cursor.execute(sql, (body['subject'], body['matter'], body['series'],
                   body['qtds_groups'], body['show_author'], body['punctuation_type'], headers['id']))
    con.commit()

    created = get_a_activity(cursor.lastrowid)
    cursor.close()
    con.close()

    return created
