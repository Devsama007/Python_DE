SELECT * FROM employees


SELECT * FROM employees
WHERE department = 'IT'  
AND salary > 50000

SELECT * FROM employees
WHERE salary BETWEEN 40000 AND 70000

SELECT * FROM employees
WHERE experience BETWEEN 2 AND 5


SELECT * FROM employees
WHERE department IN ('Finance', 'IT')

SELECT * FROM employees
WHERE salary NOT BETWEEN 40000 AND 70000

SELECT * FROM employees
WHERE department NOT IN ('Finance', 'IT')

SELECT * FROM employees
WHERE department NOT IN ('HR')
AND (
    experience BETWEEN 3 AND 5
    OR
    salary >= 50000
)


SELECT * FROM orders


SELECT * FROM orders
WHERE order_date >= '2026-01-01' AND order_date < '2026-02-28'
AND region IN ('North', 'South', 'East')
AND status NOT IN ('cancelled', 'refunded')
AND amount BETWEEN 1000 AND 20000
AND NOT (status = 'pending' AND amount < 5000)


SELECT * FROM orders
WHERE region IN ('North', 'South')
AND (amount BETWEEN 10000 AND 30000 
    OR (status = 'completed' AND amount > 5000)
    )
AND status NOT IN ('refunded', 'cancelled')
AND order_date < '2026-02-01' OR order_date >= '2026-03-01'


SELECT * FROM orders
WHERE amount BETWEEN 100 AND 100000
AND status IN ('completed', 'pending', 'processing')
AND region NOT IN ('Test', 'Unknown')
AND order_date >= '2026-02-01' OR order_date < '2025-12-01'
AND customer_id BETWEEN 500 AND 600



-- new concept
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    city VARCHAR(100)
);

INSERT INTO customers (customer_id, name, email, city) VALUES
(101, 'Amit', 'amit@gmail.com', 'Mumbai'),
(102, 'Ankit', 'ankit@yahoo.com', 'Pune'),
(103, 'Priya', 'priya@gmail.com', 'Delhi'),
(104, 'Rahul', 'rahul@outlook.com', 'Mumbai'),
(105, 'John', 'john@gmail.com', 'Chennai'),
(106, 'Alice', 'alice@yahoo.com', 'Bangalore'),
(107, 'Aman', 'aman@gmail.com', 'Pune');

SELECT * FROM customers

SELECT * FROM customers
WHERE name LIKE 'A%'

SELECT * FROM customers
WHERE email LIKE '%gmail.com'

SELECT * FROM customers
WHERE name ILIKE '%an%'

SELECT * FROM customers
WHERE name LIKE '____'

SELECT * FROM customers
WHERE name LIKE 'A___'

SELECT * FROM customers
WHERE name LIKE '_o%'

SELECT * FROM customers
WHERE email NOT LIKE '%gmail.com'

SELECT * FROM customers
WHERE name NOT LIKE 'A%'

SELECT * FROM customers
WHERE name LIKE 'A%'
AND email NOT LIKE '%gmail.com'

SELECT * FROM customers
WHERE email LIKE '%gmail.com'
  OR email LIKE '%yahoo.com'

SELECT * FROM customers
WHERE name LIKE 'A%'
  AND name LIKE '%i%'


SELECT * FROM customers
WHERE city IN ('Mumbai', 'Pune')
AND (
    name LIKE 'A%' 
     OR name  LIKE 'J'
     )
AND email NOT LIKE '%yahoo.com'


--- ****** Challenge 2 ***** ---
CREATE TABLE logs (
    log_id INT PRIMARY KEY,
    user_id INT,
    event_type VARCHAR(50),
    source VARCHAR(50),
    message VARCHAR(255)
);

INSERT INTO logs (log_id, user_id, event_type, source, message) VALUES
(1, 501, 'LOGIN', 'WEB', 'User logged in'),
(2, 502, 'PAYMENT', 'API', 'Payment successful'),
(3, 503, 'ERROR', 'API', 'Database connection failed'),
(4, 504, 'LOGIN', 'MOBILE', 'Invalid password'),
(5, 505, 'PAYMENT', 'WEB', 'Payment failed'),
(6, 506, 'ERROR', 'SERVER', 'Timeout occurred'),
(7, 507, 'LOGIN', 'API', 'Login successful'),
(8, 508, 'PAYMENT', 'MOBILE', 'Transaction pending');

SELECT * FROM logs


SELECT * FROM logs
WHERE (message ILIKE '%failed%' 
       OR message ILIKE '%error%')
AND message NOT LIKE '%password%'
AND source IN ('API', 'SERVER')


SELECT * FROM customers
WHERE (
      email LIKE '%gmail.com' 
      OR email LIKE '%yahoo.com'
      )
AND (
     name LIKE 'A%' 
     OR name LIKE 'S%' 
     OR name LIKE 'R%'
    )
AND (
   name NOT LIKE '%0%'
  AND name NOT LIKE '%1%'
  AND name NOT LIKE '%2%'
  AND name NOT LIKE '%3%'
  AND name NOT LIKE '%4%'
  AND name NOT LIKE '%5%'  --Will get easy with REGEX
  AND name NOT LIKE '%6%'
  AND name NOT LIKE '%7%'
  AND name NOT LIKE '%8%'
  AND name NOT LIKE '%9%'
)
AND email NOT LIKE '%test%'


CREATE TABLE transactions (
    transaction_id INT PRIMARY KEY,
    description VARCHAR(255),
    status VARCHAR(50),
    amount NUMERIC(10, 2),
    source VARCHAR(50)
);

INSERT INTO transactions (transaction_id, description, status, amount, source) VALUES
(1, 'UPI payment received', 'success', 5000, 'MOBILE'),
(2, 'Card payment failed', 'failed', 12000, 'WEB'),
(3, 'Refund initiated', 'pending', 3000, 'API'),
(4, 'International wire transfer', 'success', 50000, 'API'),
(5, 'Suspicious login payment', 'failed', 90000, 'WEB'),
(6, 'UPI refund processed', 'success', 1500, 'MOBILE'),
(7, 'Card transaction pending', 'pending', 8000, 'WEB'),
(8, 'Test payment failed', 'failed', 100, 'API');

SELECT * FROM transactions


SELECT *
FROM transactions
WHERE (
        description ILIKE '%payment%'
        OR description ILIKE '%transfer%'
    )
AND NOT (
        description ILIKE '%test%'
        OR description ILIKE '%suspicious%'
    )
AND status IN ('failed', 'pending')
AND amount BETWEEN 1000 AND 50000
AND source != 'MOBILE'

