To implement a rollback when inserting into a second table fails, you should use Django’s **database transaction management**. This ensures that if any part of your multi-step database operation fails, all previous changes are undone (rolled back).

Use `transaction.atomic()` for this:

````python
from django.db import transaction, DatabaseError

def create_user_and_profile(user_data, profile_data):
    try:
        with transaction.atomic():
            user = UserModel.objects.create(**user_data)
            # If the next line fails, the user creation above will be rolled back
            profile = ProfileModel.objects.create(user=user, **profile_data)
        return {"success": True}
    except DatabaseError as e:
        # Handle the error, rollback happens automatically
        return {"success": False, "error": str(e)}
````

**How it works:**
- All operations inside `with transaction.atomic():` are treated as a single transaction.
- If any exception occurs (e.g., second table insertion fails), all changes are rolled back.
- No partial data is saved.

**Summary:**  
Wrap your multi-table insertions in `with transaction.atomic():` to ensure rollback on failure.