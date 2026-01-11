import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="projeto_sales"
)
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


conn.close()