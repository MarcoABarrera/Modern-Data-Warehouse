
  create view "warehouse"."public"."stg_products__dbt_tmp"
    
    
  as (
    SELECT
    id,
    title,
    price,
    category
FROM raw_products
  );