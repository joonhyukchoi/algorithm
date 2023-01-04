select t1.flavor from (
select flavor, sum(total_order) as s from july group by flavor)
as t1
left outer join
first_half as t2
on t1.flavor = t2.flavor
order by (t1.s + t2.total_order) desc
limit 3
