SELECT
    c.cart_id,
    c.user_id,
    c.product_id,
    p.price,
    c.quantity,
    (p.price * c.quantity) AS total_value,
    c.date
FROM {{ ref('stg_carts') }} c
LEFT JOIN {{ ref('stg_products') }} p
    ON c.product_id = p.id