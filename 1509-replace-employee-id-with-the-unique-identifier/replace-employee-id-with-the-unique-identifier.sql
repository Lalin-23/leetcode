# Write your MySQL query statement below
select u.unique_id,n.name
from Employees as n
left join EmployeeUNI as u
on n.id=u.id;