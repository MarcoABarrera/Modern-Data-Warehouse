
  create view "warehouse"."public"."stg_carts__dbt_tmp"
    
    
  as (
    SELECT
    id AS cart_id,
    user_id,
    product_id,
    quantity,
    date
FROM raw_carts
  );