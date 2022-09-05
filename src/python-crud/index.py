import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='chanchitohappy',
)

cursor = conexao.cursor()

#product_choosed = 'coca cola'
#price_choosed = 5

# CREATE
#command = f'INSERT INTO vendas (name_product, price) VALUES ("{product_choosed}", {price_choosed})'
# cursor.execute(command)

# conexao.commit()

# READ
#command = f'SELECT * FROM vendas'
# cursor.execute(command)
#resultado = cursor.fetchall()
# print(resultado)

# UPDATE
#product_choosed = 'coca cola'
#price_choosed = 3

#command = f'UPDATE vendas SET price = {price_choosed} WHERE name_product = "{product_choosed}"'
# cursor.execute(command)
# conexao.commit()

# DELETE

product_choosed = 'coca cola'
command = f'DELETE FROM vendas WHERE name_product = "{product_choosed}"'
cursor.execute(command)
conexao.commit()

cursor.close()
conexao.close()
