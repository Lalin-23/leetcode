# Write your MySQL query statement below
select x.project_id,round(avg(y.experience_years),2) as average_years
from Project as x
left join Employee as y
on x.employee_id=y.employee_id
group by x.project_id;
