CREATE TABLE users(id SERIAL PRIMARY KEY, 
				   name varchar(50) NOT NULL, 
                   email varchar(60) UNIQUE NOT NULL,
				   created_at TIMESTAMPTZ DEFAULT NOW(),
				   updated_at TIMESTAMPTZ DEFAULT NOW());

INSERT INTO users(name,email) VALUES ('kiran','kiran246@gamail.com'),
									 ('rohith','rohith21@gmail.com'),
									 ('pavan','pavanpp@gmail.com'),
									 ('surendra','surendrardy23@gmail.com'),
									 ('babu','babu7007@gmail.com');

SELECT * FROM users; 
SELECT email FROM users WHERE name = 'kiran';
SELECT name,email FROM users WHERE name ILIKE '%a%';
SELECT COUNT(name), name FROM users GROUP BY name HAVING COUNT(name) > 1 ORDER BY name;
SELECT name FROM users WHERE name IN ('surendra','kiran','raghu');
UPDATE users set email = 'pavan650@gmail.com', updated_at = CURRENT_TIMESTAMP WHERE name = 'pavan';
DROP TABLE users;