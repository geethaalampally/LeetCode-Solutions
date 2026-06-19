select customer_number from 
(
select customer_number , count(*) as total_orders 
from orders
group by customer_number 
) t
order by t.total_orders desc 
limit 1;