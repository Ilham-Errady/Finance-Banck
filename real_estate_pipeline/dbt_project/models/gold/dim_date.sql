with dates as (
    select transaction_date::date as date_day from {{ ref('stg_transactions') }}
    union
    select start_date::date as date_day from {{ ref('stg_loans') }}
    union
    select opening_date::date as date_day from {{ ref('stg_accounts') }}
)

select distinct
    to_char(date_day, 'YYYYMMDD')::int as date_id,
    date_day as full_date,
    year(date_day) as year,
    quarter(date_day) as quarter,
    month(date_day) as month,
    monthname(date_day) as month_name,
    day(date_day) as day,
    dayname(date_day) as day_of_week
from dates
where date_day is not null