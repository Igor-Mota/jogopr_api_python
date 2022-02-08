from .connection import connect


def create_activity(data, user):
    print(data)
    print(user)
    con = connect()
    cursor = con.cuursor()
    sql = 'INSERT INTO activityes(subject, matter, 	series, qtds_groups, show_author,punctuation_type, teacher_id) values("%s","%s","%s","%s","%s","%s","%s")'
    values = data
    # cursor.execute(sql, values)
    return ''
