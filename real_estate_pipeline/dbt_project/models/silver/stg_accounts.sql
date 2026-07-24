with source as (
    select
        $1::int as account_id,
        $2::int as customer_id,
        $3::int as account_type_id,
        $4::int as account_status_id,
        $5::numeric(15,2) as balance,
        try_to_timestamp($6::varchar) as opening_date,
        row_number() over (
            partition by $1::int 
            order by try_to_timestamp($6::varchar) desc
        ) as rn
    from {{ source('bronze', 'RAW_ACCOUNTS') }}
)

select
    account_id,
    customer_id,
    account_type_id,
    account_status_id,
    balance,
    opening_date
from source
where rn = 1