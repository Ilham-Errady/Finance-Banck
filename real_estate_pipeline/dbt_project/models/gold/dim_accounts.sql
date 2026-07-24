select
    account_id,
    customer_id,
    account_type_id,
    account_status_id,
    balance,
    opening_date
from {{ ref('stg_accounts') }}