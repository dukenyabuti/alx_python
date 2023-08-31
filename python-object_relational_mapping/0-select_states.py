import MySQLdb

db=MySQLdb.connect(host="localhost",
                   user="admin2",
                   passwd="password",
                   db="hbtn_0e_0_usa")

cursor = db.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS states(id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, )")
states =('California', 'Arizona','Texas','New York', 'Nevada')
for state in states:
    cursor.execute('INSERT INTO states(name) VALUES(%s), state')
    print(states)
