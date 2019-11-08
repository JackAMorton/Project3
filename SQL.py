import pyodbc


server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

docker_northwind = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)

cursor = docker_northwind.cursor()
cursor.execute("SELECT @@version;")
row = cursor.fetchone()
print(row)

# FOR ALL CUSTOMERS
all_customers = cursor.execute("SELECT * FROM Customers;").fetchall()
# print(all_customers)
# print(type(all_customers))

# for row in all_customers:
#     print(row.ContactName, row.Fax)

all_products = cursor.execute("SELECT * FROM products")
while True:
    row_record = all_products.fetchone()
    if row_record is None:
        break
    print(row_record.UnitPrice)

