with source as (
    select
        $1::int as transaction_id,
        $2::int as account_origin_id,
        $3::int as account_destination_id,
        $4::int as transaction_type_id,
        $5::numeric(15,2) as amount,
        $6::timestamp as transaction_date,
        $7::int as branch_id,
        trim($8)::varchar as description,
        row_number() over (
            partition by $1::int 
            order by $6::timestamp desc
        ) as rn
    from {{ source('bronze', 'RAW_TRANSACTIONS') }}
)

select
    transaction_id,
    account_origin_id,
    account_destination_id,
    transaction_type_id,
    amount,
    transaction_date,
    branch_id,
    description
from source
where rn = 1