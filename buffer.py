import sqlite3
 
sqliteconnection = sqlite3.connect('main_database.db')
cursor = sqliteconnection.cursor()
query = 'select sqlite_version();'
cursor.execute(query)
result = cursor.fetchall()
print('SQLite Version is {}'.format(result))

sqlform = """insert into User(user_name,contact) values (?,?);"""
data = ("raju",5678)
cursor.execute(sqlform,data)

sqliteconnection.commit()
sqliteconnection.close()


