
  create view "warehouse"."public"."dim_users__dbt_tmp"
    
    
  as (
    SELECT
    id AS user_id,
    email,
    username
FROM "warehouse"."public"."stg_users"
  );