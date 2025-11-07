# Write your MySQL query statement below
select y.contest_id, round((count(distinct y.user_id)*100)/(select count(*) from Users),2) as percentage
from Register y
group by y.contest_id
order by percentage desc,y.contest_id asc;