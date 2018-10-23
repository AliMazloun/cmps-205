import pyodbc
name = open("new 1.html","w")
server = 'alexasql.database.windows.net'
database = 'AdventureWorks2016'
username = 'cmps253'
password = 'Cmps205!'
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("SELECT top 10 * from Person.Person")
row = cursor.fetchone()
name.write("<!DOCTYPE html>")
name.write("<html>")
name.write("<style>")
name.write("</style>")
name.write("<body>")
name.write("<table>")
while row:
   b =("<tr><td>" + row[4] + "</td><td>" + row[6] + "</tr>")
   name.write(b)
   row = cursor.fetchone()
name.write("</table>")
name.write("</body>")
name.write("</html>")

name.close()