import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	password = 'root_password'
	)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE CRMdatabase")