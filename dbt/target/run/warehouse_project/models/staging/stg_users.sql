
  create view "warehouse"."public"."stg_users__dbt_tmp"
    
    
  as (
    SELECT
    id,
    email,
    username
FROM raw_users
  );