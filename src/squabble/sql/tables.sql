-- create users table
CREATE TABLE IF NOT EXISTS users
(
  id integer PRIMARY KEY,
  username character varying(256) UNIQUE,
  password character varying(256) NOT NULL,
  disabled boolean NOT NULL DEFAULT false
);
