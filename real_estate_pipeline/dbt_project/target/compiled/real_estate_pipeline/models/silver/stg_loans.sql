with source as (
    select
        $1::int as loan_id,
        $2::int as account_id,
        $3::int as loan_status_id,
        $4::numeric(15,2) as principal_amount,
        $5::numeric(5,4) as interest_rate,
        $6::timestamp as start_date,
        $7::timestamp as estimated_end_date,
        row_number() over (
            partition by $1::int 
            order by $6::timestamp desc
        ) as rn
    from FINANCE_DW.BRONZE.RAW_LOANS
)

select
    loan_id,
    account_id,
    loan_status_id,
    principal_amount,
    interest_rate,
    start_date,
    estimated_end_date
from source
where rn = 1