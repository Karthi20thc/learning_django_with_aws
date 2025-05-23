# users/views/queries.py

GET_NON_ADMIN_USERS = """
SELECT * FROM users_user
WHERE is_admin = false
ORDER BY created_at DESC
LIMIT 10
"""
