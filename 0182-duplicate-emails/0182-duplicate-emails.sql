# Write your MySQL query statement below
select email as Email from Person
Group by email
Having count(email)>1;