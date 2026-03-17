SELECT
    c.cart_id,
    c.user_id,
    c.product_id,
    p.price,
    c.quantity,
    (p.price * c.quantity) AS total_value,
    c.date
FROM "warehouse"."public"."stg_carts" c
LEFT JOIN "warehouse"."public"."stg_products" p
    ON c.product_id = p.id