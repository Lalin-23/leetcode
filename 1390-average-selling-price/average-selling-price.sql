# Write your MySQL query statement below
select x.product_id,round(ifnull(sum(x.price*y.units)/sum(units),0),2) as average_price
from Prices as x
left join UnitsSold as y
on x.product_id=y.product_id
and y.purchase_date between x.start_date and x.end_date
group by x.product_id;