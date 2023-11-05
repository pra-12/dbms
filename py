!python -m pip install mysql-connector-python
import mysql.connector

conn = mysql.connector.connect(
      user='root',
      password='pranav',
      host='localhost',
      database='pratikkutra',
      auth_plugin='mysql_native_password'
)

cursor = conn.cursor()

c_query = "CREATE TABLE student (name varchar(200), age int(3), address varchar(200)) "


cursor.execute(c_query)
conn.commit()

insert_query = "INSERT INTO student (name, age, address) VALUES (%s, %s, %s)"
values = ("rohit",19,"Pune")

cursor.execute(insert_query,values)
conn.commit()

update_query = "UPDATE student SET age = %s WHERE name = %s"
new_age = 20
name_to_update = "rohit"

cursor.execute(update_query, (new_age, name_to_update))
conn.commit()

select_query = "SELECT * FROM student WHERE name = %s"
name_to_select = "rohit"

cursor.execute(select_query, (name_to_select,))
result = cursor.fetchall()

if result:
    for row in result:
        print(row)
else:
    print("No matching records found.")

delete_query = "DELETE FROM student WHERE name = %s"
name_to_delete = "rohit"

cursor.execute(delete_query, (name_to_delete,))
conn.commit()

cursor.close()
conn.close()
