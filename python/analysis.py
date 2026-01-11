import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="projeto_sales"
)
'''
Analise 1: faturamento por cidade 
query = """
SELECT city, SUM(total_price) AS faturamento
FROM sales
GROUP BY city;
"""


df = pd.read_sql(query, conn)

df.plot(
    x='city',
    y='faturamento',
    kind='bar',
    title='Faturamento por Cidade'
)

plt.tight_layout()
plt.show()


'''
'''Analise 2: Faturamento por categoria 

query = """
SELECT product_category, SUM(total_price) AS faturamento
FROM sales
GROUP BY product_category
ORDER BY faturamento desc
"""

df = pd.read_sql(query, conn)

df.plot(
    x='product_category',
    y='faturamento',
    kind='bar',
    title='Faturamento por Categoria'
)

plt.tight_layout()
plt.show()

'''
'''Analise 3: Quantidade Vendida por produto '''

query = """
SELECT product_name, SUM(quantity) AS total_vendido
FROM sales
GROUP BY product_name

"""

df = pd.read_sql(query, conn)

df.plot(
    x='product_name',
    y='total_vendido',
    kind='bar',
    title='Quantidade Vendida por produto'
)

plt.tight_layout()
plt.show()



conn.close()

