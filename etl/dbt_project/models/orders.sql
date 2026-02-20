
with raw_orders as (
    select * from {{ source('etl_data', 'raw_orders') }}
)

select
    order_id,
    customer_id,
    order_date,
    region,
    quantity,
    unit_price,
    discount_pct,
    quantity * unit_price as gross_amount,
    quantity * unit_price * discount_pct as discount_amount,
    quantity * unit_price * (1 - discount_pct) as net_amount,
    case
        when quantity >= 3 then 'bulk'
        else 'standard'
    end as order_size
from raw_orders
