# Django imports
from django.db import connection,transaction
from django.contrib.auth.hashers import make_password

from rest_framework.response import Response
from rest_framework import generics, status

def validate_input(self, data):
    required_fields = ['username', 'email', 'password']
    missing_fields = [field for field in required_fields if not data.get(field)]
    if missing_fields:
        error_msg = f"Missing required fields: {', '.join(missing_fields)}"
        return False, Response({"error": error_msg}, status=status.HTTP_400_BAD_REQUEST)
    return True, None

def insert_user_into_db(self, data):
    hashed_password = make_password(data.get("password"))
    with transaction.atomic(), connection.cursor() as cursor:
        cursor.execute(
            """
            INSERT INTO users_user (username, email, is_admin, password, created_at)
            VALUES (%s, %s, %s, %s, NOW())
            RETURNING id, username, email, is_admin, created_at
            """,
            [
                data.get("username"),
                data.get("email"),
                data.get("is_admin", False),
                hashed_password,
            ],
        )
        return cursor.fetchone()

def build_success_response(self, user_row):
    return Response({
        "message": "User created successfully",
        "user": {
            "id": user_row[0],
            "username": user_row[1],
            "email": user_row[2],
            "is_admin": user_row[3],
            "created_at": user_row[4],
        }
    }, status=status.HTTP_201_CREATED)