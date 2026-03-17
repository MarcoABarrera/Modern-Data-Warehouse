SELECT
    id AS user_id,
    email,
    username
FROM {{ ref('stg_users') }}