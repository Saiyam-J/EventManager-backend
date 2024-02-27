import pymysql
import os
connection = pymysql.connect(
    host='localhost',
    user=os.environ['DB_USER'],
    password=os.environ['DB_PASS'],
    database=os.environ['DB_NAME']
)
cursor = connection.cursor()
cursor.execute('UPDATE events SET isCompleted = 1 WHERE enddatetime < NOW() + INTERVAL 5 HOUR + INTERVAL 30 MINUTE;')
connection.commit()
cursor.close()
connection.close()