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
from users.models import UserModel
from .helper.utils import validate_input, insert_user_into_db, build_success_response

# logging
import logging

# -----------------------------------------------------------------------------------------------------------------------------------------

logger = logging.getLogger(__name__)

# all get methods
class CustomUserListView(APIView):
    def get(self, request):
        user_id = request.query_params.get('id')
        try:
            if user_id:
                user = UserModel.objects.get(id=user_id)
                serializer = UserSerializer(user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                # users = UserModel.objects.raw(GET_NON_ADMIN_USERS)
                users = UserModel.objects.all().order_by('-created_at')
                serializer = UserSerializer(users, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except UserModel.DoesNotExist:
            return Response(
                {"error": "User not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        except DatabaseError as e:
            logger.error(f"DatabaseError while fetching users: {str(e)}")
            return Response(
                {"error": "Database error occurred while fetching users", "err_message": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        except Exception as e:
            logger.error(f"Error fetching users: {str(e)}")
            return Response(
                {"error": "Failed to fetch users", "err_message": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


# all post methods
class UserListCreateView(generics.ListCreateAPIView):
    queryset = UserModel.objects.all()
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
