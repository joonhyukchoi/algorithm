SHOW DATABASES;
USE DB1;

CREATE TABLE menus (id INT, name VARCHAR(100));
DROP TABLE menus;

INSERT INTO menus (id, name) VALUES (1, 'curry');
UPDATE menus SET name = 'stew' WHERE id = 1;
DELETE FROM menus WHERE id = 1;

SELECT age, COUNT(*) FROM users WHERE gender = 'man' GROUP BY age HAVING COUNT(*) >= 3;

SELECT * FROM users INNER JOIN items ON users.item_id = items.id;
SELECT * FROM users LEFT JOIN items ON users.item_id = items.id;
SELECT * FROM users FULL OUTER JOIN items ON users.item_id = items.id;

CREATE INDEX idx_menu ON menus (name);


