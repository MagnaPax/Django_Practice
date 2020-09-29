from django.db import models
import cx_Oracle as ora

database = 'kosmorpa/test00@192.168.0.68:1521/orcl'

def getLoginChk(**kwargs):
    con = ora.connect(database)
    cursor = con.cursor()
    # name, id 값을 select
    sql_select="select count(*) cnt,name from member_table where id=:id and pwd=:pwd group by name"
    cursor.execute(sql_select, id=kwargs['id'], pwd=kwargs['pwd'])
    datas = cursor.fetchall()
    con.close()
    return datas