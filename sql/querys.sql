--- Analise 1: faturamento por cidade

SELECT city, SUM(total_price) AS faturamento
FROM sales
GROUP BY city;

--- Analise 2: Faturamento por categoria 

SELECT product_category, SUM(total_price) AS faturamento
FROM sales
GROUP BY product_category
ORDER BY desc


--- Analise 3: Quantidade Vendida por produto 

SELECT product_name, SUM(quantity) AS total_vendido
FROM sales
GROUP BY product_name