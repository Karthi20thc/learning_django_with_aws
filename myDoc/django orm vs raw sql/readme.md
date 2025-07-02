```python
# connection.cursor() gives you direct access to the database.
# cursor.execute(...) runs the SQL insert statement.
# This bypasses the Django model (UserModel) and interacts directly with the database table (users_user).


# def insert_user_into_db(self, data):
#     hashed_password = make_password(data.get("password"))
#     with transaction.atomic(), connection.cursor() as cursor:
#         cursor.execute(
#             """
#             INSERT INTO users_user (username, email, is_admin, password, created_at)
#             VALUES (%s, %s, %s, %s, NOW())
#             RETURNING id, username, email, is_admin, created_at
#             """,
#             [
#                 data.get("username"),
#                 data.get("email"),
#                 data.get("is_admin", False),
#                 hashed_password,
#             ],
#         )
#         return cursor.fetchone()

# Here’s how you can rewrite insert_user_into_db using the Django ORM instead of raw SQL:
def insert_user_into_db(self, data):
    hashed_password = make_password(data.get("password"))
    with transaction.atomic():
        user = UserModel.objects.create(
            username=data.get("username"),
            email=data.get("email"),
            is_admin=data.get("is_admin", False),
            password=hashed_password,
        )
        return (
            user.id,
            user.username,
            user.email,
            user.is_admin,
            user.created_at,
        )
```
