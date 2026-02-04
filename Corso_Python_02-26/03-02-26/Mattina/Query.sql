SELECT first_name Nome, last_name Cognome
FROM actor;

SELECT * FROM film
WHERE rating='G';

SELECT * FROM customer
WHERE first_name LIKE 'A%' AND last_name LIKE '%S';

SELECT * FROM film
WHERE length > 150 AND rental_rate < 1.00 ORDER BY length;

-- ---------------------------------------------------
SELECT * FROM film
ORDER BY length DESC 
LIMIT 10;

SELECT count(rental_rate) "Conteggio", sum(rental_rate) "Totale", avg(rental_rate) "Prezzo medio noleggio"
FROM film;

SELECT count(title) "Totale film", rental_duration
FROM film
GROUP BY rental_duration;

SELECT staff_id, count(staff_id) "Pagamenti staff id"
FROM payment
GROUP BY staff_id;

SELECT min(amount) "Pagamento minimo", max(amount) "Pagamento massimo"
FROM payment;
