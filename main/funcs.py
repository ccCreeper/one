import pymysql
import datetime


def add_client(phone, email, name, sex):
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='yhv5tgh233', port=3306, db='datademo')
        cursor = db.cursor()
        sql = "insert into main_client(phone, email, name, sex) values('%s','%s','%s','%s')" % (phone, email, name, sex)
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False


def add_order(id, pay_method, state, submit_date, check_in_date, check_out_date):
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='yhv5tgh233', port=3306, db='datademo')
        cursor = db.cursor()
        sql = "insert into main_order(id, pay_method, state, submit_date, check_in_date, check_out_date) " \
              "values('%s',%d,%d,'%s','%s','%s')" % (id, pay_method, state, submit_date, check_in_date, check_out_date)
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False


def add_room(id, kind, state):
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='yhv5tgh233', port=3306, db='datademo')
        cursor = db.cursor()
        sql = "insert into main_room(id, kind, state) values(%d,%d,%d)" % (id, kind, state)
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False


def seekclient(thephone):
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='yhv5tgh233', port=3306, db='datademo')
        cursor = db.cursor()
        sql = "select name,sex,phone,email,id,check_in_date,check_out_date from"\
                "main_order left join main_client on main_order.phone = main_client.phone where phone='%d'"%(thephone)
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            name = row[0]
            sex = row[1]
            phone = row[2]
            email = row[3]
            id = row[4]
            check_in_date = row[5]
            check_out_date = row[6]
            print(name, sex, phone, email, id, check_in_date, check_out_date)
            db.close()
    except:
        print("Error:unable to fecth data")



def seekroom(thekind):
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='yhv5tgh233', port=3306, db='datademo')
        cursor = db.cursor()
        sql = "select kind,count(id) from"\
                "main_room where ((kind='%d') and (state = 1)) group by kind" %(thekind)
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            kind = row[0]
            num = row[1]
            print(kind,num)
            db.close()
    except:
        print ("Error:unable to fecth data")



def seekorder(theid):
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='yhv5tgh233', port=3306, db='datademo')
        cursor = db.cursor()
        sql = "select phone,id,state,pay_method,submit_date,check_in_date,check_out_date from"\
                "main_order where id='%d'"%(theid)
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            phone = row[0]
            id = row[1]
            state = row[2]
            pay_method = row[3]
            submit_date = row[4]
            check_in_date = row[5]
            check_out_date = row[6]
            print(phone,id,state,pay_method,submit_date,check_in_date,check_out_date)
            db.close()
    except:
        print ("Error:unable to fecth data")