select
    l.loan_id,
    l.account_id,
    a.customer_id,
    l.loan_status_id,
    to_char(l.start_date::date, 'YYYYMMDD')::int as date_id,
    l.principal_amount,
    l.interest_rate,
    l.start_date,
    l.estimated_end_date
from FINANCE_DW.silver.stg_loans l
left join FINANCE_DW.silver.stg_accounts a on l.account_id = a.account_id