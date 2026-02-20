use classicmodels;
--Scrivete una query SQL che restituisca solo i record dalla tabella "products"con un prezzo superiore a 50.
select * from products
where `buyPrice` > 50
order by `buyPrice`;

--Scrivete una query SQL che elimini tutti gli ordini nella tabella "orders" con lo stato "Cancelled".
select * from orders
where status = "Cancelled";

create table orders2
select * from orders;

create table orderdetails2
select * from orderdetails;

select * from orders2
where status = "Cancelled";

delete from orders
where status = "Cancelled"; 

select * from orderdetails;

-- eliminiamo prima il figlio e poi il padre, altrimenti avremo un errore di chiave esterna

--eliminazione della tabella dove ce la chiave esterna
delete from orderdetails
where orderNumber IN (
    select orderNumber from orders where status = "Cancelled"
);

--eliminazione della tabella dove ce la chiave primaria
delete from orders
where status = "Cancelled";

select * from orders o
left join orderdetails od on o.orderNumber = od.orderNumber
where o.status = "Cancelled";

select * from orders o
left join orderdetails od on o.orderNumber = od.orderNumber
where o.status != "Cancelled";