import pymysql

conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='Imiss@1996',
    db='python_study',
    charset='utf8'
)
cursor = conn.cursor()

print conn
print cursor

cursor.close()
conn.close()
