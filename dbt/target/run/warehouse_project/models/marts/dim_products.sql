
  create view "warehouse"."public"."dim_products__dbt_tmp"
    
    
  as (
    SELECT
    id AS product_id,
    title,
    category,
    price
FROM "warehouse"."public"."stg_products"
  );