SELECT
    c.id AS cart_id,
    c.user_id,
    c.date
FROM "warehouse"."public"."stg_carts" c