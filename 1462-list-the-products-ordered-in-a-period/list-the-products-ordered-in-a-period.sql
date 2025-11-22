# Write your MySQL query statement below
select x.product_name, sum(y.unit) as unit
from Products as x
join Orders as y
on x.product_id=y.product_id
where y.order_date between '2020-02-01' and '2020-02-29'
group by x.product_id,x.product_name
having sum(y.unit)>=100;