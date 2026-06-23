CREATE TABLE users(user_id SERIAL PRIMARY KEY, 
				   user_name VARCHAR(50) NOT NULL,
				   age INTEGER NOT NULL,
                   email VARCHAR(60) UNIQUE NOT NULL,
				   created_at TIMESTAMPTZ DEFAULT NOW(),
				   updated_at TIMESTAMPTZ DEFAULT NOW());

CREATE TABLE posts(post_id SERIAL PRIMARY KEY,
				   title VARCHAR(200) NOT NULL,
				   description TEXT,
				   user_id INTEGER,
				   created_at TIMESTAMPTZ DEFAULT NOW(),
				   updated_at TIMESTAMPTZ DEFAULT NOW(),
				   FOREIGN KEY (user_id) REFERENCES users(user_id));

INSERT INTO users(user_name,age,email) VALUES ('kiran',22,'kiran246@gmail.com'),
											  ('rohith',21,'rohith21@gmail.com'),
											  ('yagami',29,'dnote111@gmail.com'),
											  ('luffy',17,'piking777@gmail.com'),
											  ('Gon',17,'hunter01@gmail.com');

ALTER TABLE posts
ALTER COLUMN user_id SET NOT NULL;

INSERT INTO posts(title, description, user_id) VALUES
('Learning SQL',
 'Started learning SQL joins and constraints.',
 1),
('PostgreSQL Basics',
 'Practiced creating tables and inserting records.',
 3),
('Python Tips',
 'Shared some useful Python tricks.',
 1),
('FastAPI CRUD',
 'Built CRUD APIs using FastAPI and Pydantic.',
 2),
('Docker Guide',
 'Containerized my FastAPI application.',
 5),
('Death Note Analysis',
 'Thoughts on the strategy used by Light Yagami.',
 3),
('King of Pirates',
 'My journey to becoming the Pirate King.',
 2),
('Hunter Exam',
 'Experiences from the Hunter Exam.',
 5),
('Nen Training',
 'Learning the basics of Nen abilities.',
 3);

SELECT * FROM users;
SELECT * FROM posts;

SELECT user_name,title,description 
FROM users INNER JOIN posts ON users.user_id = posts.user_id ORDER BY user_name;

SELECT user_name,title,description 
FROM users LEFT JOIN posts ON users.user_id = posts.user_id ORDER BY user_name;

SELECT user_name
FROM users FULL JOIN posts ON users.user_id = posts.user_id WHERE title IS NULL;

SELECT count(user_name) AS "post count", user_name 
FROM users INNER JOIN posts ON users.user_id = posts.user_id GROUP BY user_name;

DELETE FROM posts WHERE user_id = 1;

SELECT user_name FROM users WHERE user_name ILIKE '_a%i';