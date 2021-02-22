CREATE TABLE feedback (
    id SERIAL PRIMARY KEY,
    content TEXT,
    sent_at TIMESTAMP
);


CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
    );
CREATE TABLE accounts (
    id SERIAL,
    user_id INTEGER REFERENCES users,
    username TEXT,
    account_number INTEGER UNIQUE PRIMARY KEY,
    account_balance INTEGER
    );
CREATE TABLE deposits (
    id SERIAL ,
    user_id INTEGER REFERENCES users,
    account_number INTEGER REFERENCES accounts,
    sum INTEGER,
    account_balance INTEGER,
    sent_at TIMESTAMP,
    transaction_type TEXT
    );
CREATE TABLE transfers (
    id SERIAL,
    account_number INTEGER REFERENCES accounts,
    sum INTEGER,
    to_account INTEGER,
    sent_at TIMESTAMP,
    transaction_type TEXT
);
CREATE TABLE withdrawals (
 id SERIAL PRIMARY KEY ,
account_number INTEGER REFERENCES accounts,
sum INTEGER,
account_balance INTEGER,
sent_at TIMESTAMP,
transaction_type TEXT );




