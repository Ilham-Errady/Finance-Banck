
  
    

create or replace transient table FINANCE_DW.gold.dim_accounts
    
    
    
    
    

    as (select
    account_id,
    customer_id,
    account_type_id,
    account_status_id,
    balance,
    opening_date
from FINANCE_DW.silver.stg_accounts
    )
;


  