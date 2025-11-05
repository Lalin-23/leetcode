# Write your MySQL query statement below
select x.student_id,x.student_name,y.subject_name,count(z.subject_name)as attended_exams
from Students as x
cross join Subjects as y
left join Examinations as z 
on x.student_id=z.student_id
and y.subject_name=z.subject_name
group by x.student_id,x.student_name,y.subject_name
order by x.student_id,x.student_name; 