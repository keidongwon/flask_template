CREATE DATABASE project;
CREATE USER 'user'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON project.* TO 'user'@'localhost';
FLUSH PRIVILEGES
