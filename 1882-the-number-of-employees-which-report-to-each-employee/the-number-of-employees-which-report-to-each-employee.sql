# Write your MySQL query statement below
select x.employee_id,x.name,
count(y.employee_id)as reports_count,
round(avg(y.age)) as average_age
from Employees as x
join Employees as y
on y.reports_to=x.employee_id
group by x.employee_id,x.name
order by x.employee_id; 