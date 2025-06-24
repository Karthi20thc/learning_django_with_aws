Certainly! In Django, `objects` is the **default model manager** for every model class.

For example, if you have a model like this:

```python
from django.db import models

class UserModel(models.Model):
    username = models.CharField(max_length=100)
    # ... other fields ...
```

Django automatically adds a manager called `objects` to your model. This manager provides methods to interact with the database, such as:

- `UserModel.objects.all()` – Get all records
- `UserModel.objects.filter(...)` – Filter records
- `UserModel.objects.raw(...)` – Run raw SQL queries

So, in your code:

```python
users = UserModel.objects.raw(GET_NON_ADMIN_USERS)
```

- `UserModel` is your Django model.
- `.objects` is the default manager.
- `.raw()` is a method provided by the manager to execute raw SQL.

**Summary:**  
`objects` is a built-in manager Django adds to every model for database operations.