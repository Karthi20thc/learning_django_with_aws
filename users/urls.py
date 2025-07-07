from django.urls import path
from .views.views import CustomUserListView, UserListCreateView

urlpatterns = [
    path('get-users/', CustomUserListView.as_view(), name='user-list-create'),
    path('create-user/', UserListCreateView.as_view(), name='user-list-create'),
]


# How to use:

# Add a URL pattern like:
# path('users/<int:user_id>/', CustomUserDetailView.as_view(), name='user-detail')
# Make a GET request to /users/1/ to get the user with ID 1.

# class CustomUserDetailView(APIView):
#     def get(self, request, user_id):
#         try:
#             user = UserModel.objects.get(id=user_id)
#             serializer = UserSerializer(user)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except UserModel.DoesNotExist:
#             return Response(
#                 {"error": "User not found"},
#                 status=status.HTTP_404_NOT_FOUND,
#             )
#         except DatabaseError as e:
#             logger.error(f"DatabaseError while fetching user: {str(e)}")
#             return Response(
#                 {"error": "Database error occurred", "err_message": str(e)},
#                 status=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             )
#         except Exception as e:
#             logger.error(f"Error fetching user: {str(e)}")
#             return Response(
#                 {"error": "Failed to fetch user", "err_message": str(e)},
#                 status=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             )