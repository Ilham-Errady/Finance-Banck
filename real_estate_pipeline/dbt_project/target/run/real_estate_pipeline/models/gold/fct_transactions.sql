
  
    

create or replace transient table FINANCE_DW.gold.fct_transactions
    
    
    
    
    

    as (select
    t.transaction_id,
    t.account_origin_id,
    t.account_destination_id,
    a.customer_id as origin_customer_id,
    t.transaction_type_id,
    t.branch_id,
    to_char(t.transaction_date::date, 'YYYYMMDD')::int as date_id,
    t.transaction_date,
    t.amount
from FINANCE_DW.silver.stg_transactions t
left join FINANCE_DW.silver.stg_accounts a on t.account_origin_id = a.account_id
    )
;


  