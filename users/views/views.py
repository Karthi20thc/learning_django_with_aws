from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from users.serializers import UserSerializer

# Django imports
from django.db import  DatabaseError, IntegrityError

# These are both exception classes, not methods.

# Common Exception Classes in django.db:
# Here are some commonly used exception classes available in django.db:

# DatabaseError
# DataError
# OperationalError
# IntegrityError
# InternalError
# ProgrammingError
# NotSupportedError
# InterfaceError
# TransactionManagementError
# Error (base class for all database exceptions)



# query import
from .sql_quereis.get_queries import GET_NON_ADMIN_USERS

# model imports
from users.models import User
from .helper.utils import validate_input, insert_user_into_db, build_success_response

# logging
import logging

# -----------------------------------------------------------------------------------------------------------------------------------------

logger = logging.getLogger(__name__)

# all get methods
class CustomUserListView(APIView):
    def get(self, request):
        users = User.objects.raw(GET_NON_ADMIN_USERS)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# all post methods
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        data = request.data

        # Validate input
        is_valid, error_response = validate_input(self, data)
        if not is_valid:
            return error_response

        try:
            # Create user and return response
            user_row = insert_user_into_db(self, data)
            if user_row:
                return build_success_response(self, user_row)
            else:
                return Response(
                    {"error": "User creation failed"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        except IntegrityError as e:
            logger.error(f"IntegrityError: {str(e)}")
            return Response(
                {
                    "error": "Integrity error: possibly duplicate username or email",
                    "err_message": str(e),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        except DatabaseError as e:
            logger.error(f"DatabaseError: {str(e)}")
            return Response(
                {
                    "error": "Database error occurred",
                    "err_message": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            return Response(
                {"error": "An unexpected error occurred"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
