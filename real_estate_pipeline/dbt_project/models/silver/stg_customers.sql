with source as (
    select
        $1::int as customer_id,
        trim($2)::varchar as first_name,
        trim($3)::varchar as last_name,
        try_to_timestamp(nullif(trim($4::varchar), 'NaT')) as date_of_birth,
        $5::int as address_id,
        $6::int as customer_type_id,
        row_number() over (
            partition by $1::int 
            order by $1::int
        ) as rn
    from {{ source('bronze', 'RAW_CUSTOMERS') }}
)

select
    customer_id,
    first_name,
    last_name,
    date_of_birth,
    address_id,
    customer_type_id
from source
where rn = 1