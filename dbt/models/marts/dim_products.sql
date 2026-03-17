SELECT
    id AS product_id,
    title,
    category,
    price
FROM {{ ref('stg_products') }}