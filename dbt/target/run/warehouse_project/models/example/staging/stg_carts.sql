
  create view "warehouse"."public"."stg_carts__dbt_tmp"
    
    
  as (
    SELECT
    id,
    user_id,
    date
FROM raw_carts
  );