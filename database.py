#pip install mysql-connector-python
import mysql.connector
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    #database="pysql"
)
#CREARE DATABASE
cursor = db.cursor()
cursor.execute("CREATE DATABASE pysql")
#EVITARE ERRORE SE DATABSE GIA' PRESENTE
# cursor.execute("SHOW DATABASES")
# for x in cursor:
#     print(x)

#CREARE TABELLE
cursor = db.cursor()
cursor.execute("CREATE TABLE clienti (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR (255))")
cursor.execute("SHOW TABLES")
for x in cursor:
    print(x)

#INSERT
cursor = db.cursor()
sql = "INSERT INTO clienti (nome, cognome) VALUES (%s, %s)"
values = ("Luca", "Rossi")
cursor.execute(sql, values)
db.commit()
print("id ultima riga inserita ", cursor.lastrowid)
#INSERT MULTIPLO
values=[
    ("Anna", "Neri"),
    ("Luca", "Rossi"),
]
cursor.executemany(sql, values)
db.commit()

#SELECT
cursor = db.cursor()
sql = "SELECT * FROM clienti WHERE nome = 'Marco'" #"SELECT id,nome FROM clienti"
cursor.execute(sql)
result = cursor.fetchall() #fetchone solo una riga
for riga in result:
    print(riga)
