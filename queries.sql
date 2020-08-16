SELECT
payment.payment,
--(sum(transaction.amount) +
--payment.initial_amount) as total
FROM api_payment as payment
left join api_transaction as transaction on transaction.payment_target_id = payment.id
where payment.user_id = 1
	and transaction.user_id = 1
--group by payment.payment, payment.initial_amount

--select * from api_payment

select 
api_payment.payment,
case
	when sum(api_payment.initial_amount) = 0 then 5
	else sum(api_payment.initial_amount)
	end as initial_sum,
sum(api_transaction.amount) as amount_sum
--(initial_sum + amount_sum) as total
from
api_payment
left join api_transaction on api_transaction.payment_target_id = api_payment.id
group by api_payment.payment