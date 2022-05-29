#Single Table SQL

CREATE TABLE Ages ( 
  name VARCHAR(128), 
  age INTEGER
)

DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Moad', 16);
INSERT INTO Ages (name, age) VALUES ('Danniel', 28);
INSERT INTO Ages (name, age) VALUES ('Lucy', 37);
INSERT INTO Ages (name, age) VALUES ('Cadance', 21);


SELECT hex(name || age) AS X FROM Ages ORDER BY X