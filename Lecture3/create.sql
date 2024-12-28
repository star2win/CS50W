CREATE TABLE flights (
    id SERIAL PRIMARY KEY,
    origin VARCHAR NOT NULL,
    destination VARCHAR NOT NULL,
    duration INTEGER NOT NULL
);

INSERT INTO flights (origin, destination, duration) VALUES ('New York', 'London', 415);
INSERT INTO flights (origin, destination, duration) VALUES ('Shanghai', 'Paris', 760);
INSERT INTO flights (origin, destination, duration) VALUES ('Istanbul', 'Tokyo', 700);
INSERT INTO flights (origin, destination, duration) VALUES ('New York', 'Paris', 435);
INSERT INTO flights (origin, destination, duration) VALUES ('Moscow', 'Paris', 245);
INSERT INTO flights (origin, destination, duration) VALUES ('Lima', 'New York', 455);

SELECT * FROM flights;

SELECT origin, destination FROM flights;

SELECT * FROM flights WHERE id = 3;

SELECT * FROM flights WHERE origin = 'New York';

SELECT * FROM flights WHERE duration > 500;

SELECT * FROM flights WHERE destination = 'Paris' OR duration >500;

SELECT AVG(duration) FROM flights WHERE origin = 'New York';

SELECT COUNT(*) FROM flights;
SELECT MIN(duration) FROM flights;
SELECT MAX(duration) FROM flights;
SELECT * FROM flights WHERE duration = '760';

SELECT * FROM flights WHERE origin IN ('New York', 'Lima');
SELECT * FROM flights WHERE origin LIKE '%a%';

UPDATE flights SET duration = 430 WHERE origin = 'New York' AND destination = 'London';

DELETE FROM flights WHERE destination = 'Tokyo';

SELECT * FROM flights LIMIT 2;

SELECT * FROM flights ORDER BY duration ASC LIMIT 3;  /* also DESC */

SELECT origin, COUNT(*) FROM flights GROUP BY origin;

SELECT origin, COUNT(*) FROM flights GROUP BY origin HAVING COUNT(*) > 1;

ALTER TABLE flights ADD COLUMN origin_code VARCHAR(3), ADD COLUMN destination_code VARCHAR(3);

UPDATE flights SET origin_code = 'JFK', destination_code = 'LHR' WHERE id = 1;
UPDATE flights SET origin_code = 'PVG', destination_code = 'CDG' WHERE id = 2;
UPDATE flights SET origin_code = 'IST', destination_code = 'NRT' WHERE id = 3;
UPDATE flights SET origin_code = 'JFK', destination_code = 'CDG' WHERE id = 4;
UPDATE flights SET origin_code = 'SVO', destination_code = 'CDG' WHERE id = 5;
UPDATE flights SET origin_code = 'LIM', destination_code = 'JFK' WHERE id = 6;

CREATE TABLE passengers (id SERIAL PRIMARY KEY, name VARCHAR NOT NULL, flight_id INTEGER REFERENCES flights);

INSERT INTO passengers (name, flight_id) VALUES ('Alice', 1);
INSERT INTO passengers (name, flight_id) VALUES ('Bob', 1);
INSERT INTO passengers (name, flight_id) VALUES ('Charlie', 2);
INSERT INTO passengers (name, flight_id) VALUES ('Dave', 2);
INSERT INTO passengers (name, flight_id) VALUES ('Erin', 4);
INSERT INTO passengers (name, flight_id) VALUES ('Frank', 6);
INSERT INTO passengers (name, flight_id) VALUES ('Grace', 6);

SELECT origin, destination, name FROM flights JOIN passengers ON passengers.flight_id = flights.id WHERE name = 'Alice';
SELECT origin, destination, name FROM flights LEFT JOIN passengers ON passengers.flight_id = flights.id;

SELECT origin, destination, name FROM flights FULL OUTER JOIN passengers ON passengers.flight_id = flights.id;

select * FROM flights WHERE id IN (SELECT flight_id from passengers GROUP BY flight_id HAVING COUNT(*) > 1);

