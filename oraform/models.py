from django.db import models
import cx_Oracle as ora
import pandas as pd

database = 'kosmorpa/test00@192.168.0.68:1521/orcl'

# 메소드 실행 전에 DB에 member_table 테이블이 만들어져 있어야 됨


def memberinsert(addr_list):
    print(addr_list)
    conn = ora.connect(database)
    cursor = conn.cursor()  # Oracle DB 접속한 객체의 주소값 cursor()
    sql = "insert into member_table " \
          "values(member_table_seq.nextVal,:1,:2,:3,:4,:5,:6,0,sysdate)"
    cursor.execute(sql, addr_list)
    cursor.close()
    conn.commit()
    conn.close()


def getMemberData():
    conn = ora.connect(database)
    cursor = conn.cursor()
    sql_select = "select * from member_table order by 1 desc"
    cursor.execute(sql_select)
    datas = cursor.fetchall()
    conn.close()
    return datas
