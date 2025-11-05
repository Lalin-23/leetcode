# Write your MySQL query statement below
select x.id
from Weather as x
join Weather as y
on datediff(x.recordDate,y.recordDate)=1
where x.temperature>y.temperature;
