with customers as (
    select * from FINANCE_DW.silver.stg_customers
),
accounts as (
    select 
        customer_id,
        count(account_id) as total_accounts,
        sum(balance) as total_balance
    from FINANCE_DW.silver.stg_accounts
    group by customer_id
)

select
    c.customer_id,
    c.first_name,
    c.last_name,
    c.date_of_birth,
    c.customer_type_id,
    coalesce(a.total_accounts, 0) as total_accounts,
    coalesce(a.total_balance, 0) as total_balance
from customers c
left join accounts a on c.customer_id = a.customer_id