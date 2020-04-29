SELECT AVG(speed)
FROM pc;


SELECT AVG(screen) 
FROM laptop JOIN product ON product.model = laptop.model 
GROUP BY product.maker; 


SELECT * 
FROM laptop 
WHERE model = 1752;


SELECT AVG(speed) 
FROM laptop 
WHERE price > 1000;


SELECT AVG(price) 
FROM pc 
GROUP BY hd;


SELECT AVG(price) 
FROM pc 
WHERE speed > 500 
GROUP BY speed;


SELECT AVG(price) 
FROM pc c JOIN product p ON c.model = p.model 
WHERE maker = 'A';


SELECT (SUM(c.price) + SUM(l.price)) / (COUNT(c.model) + COUNT(l.model)) AS "Avg pc and laptop price" 
FROM product p LEFT JOIN pc c ON p.model = c.model LEFT JOIN laptop l ON p.model = l.model 
WHERE maker = 'B'; 


SELECT maker 
FROM product p JOIN pc c ON p.model = c.model 
GROUP BY maker 
HAVING COUNT(c.model) >= 3;


SELECT maker 
FROM product p JOIN pc c ON p.model = c.model 
WHERE price = (SELECT price 
FROM pc 
ORDER BY price 
LIMIT 1);


SELECT AVG(hd) 
FROM pc c JOIN product p ON c.model = p.model 
WHERE maker = (SELECT maker 
FROM product pr JOIN printer prin ON pr.model = prin.model);