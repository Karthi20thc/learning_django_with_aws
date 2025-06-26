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


-------------------------------------------------------------------------------------------------------------------

In Django, the `.objects` attribute is the **default model manager** for interacting with your database.

### 💡 What is a Model Manager?

A **manager** in Django is an interface through which database query operations are provided to Django models. Every Django model gets at least one manager by default — called `.objects`.

---

### ✅ Basic Usage of `.objects`

Assume we have this model:

```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
```

You can use `Book.objects` to query the database:

#### 1. Get all records

```python
Book.objects.all()
```

#### 2. Filter records

```python
Book.objects.filter(author='J.K. Rowling')
```

#### 3. Get a single record

```python
Book.objects.get(id=1)
```

#### 4. Create a new record

```python
Book.objects.create(title='1984', author='George Orwell')
```

#### 5. Delete records

```python
Book.objects.filter(title='1984').delete()
```

---

### 🎯 Custom Model Managers (Optional)

You can create your own manager if you want custom queries:

```python
class BookManager(models.Manager):
    def by_author(self, author_name):
        return self.filter(author=author_name)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)

    objects = BookManager()
```

Usage:

```python
Book.objects.by_author('George Orwell')
```

---

### Summary

| Task                  | Code Example                  |
| --------------------- | ----------------------------- |
| Get all records       | `Book.objects.all()`          |
| Filter records        | `Book.objects.filter(...)`    |
| Get a single record   | `Book.objects.get(...)`       |
| Create a new record   | `Book.objects.create(...)`    |
| Custom manager method | `Book.objects.by_author(...)` |

Let me know if you want to see examples using `.values()`, `.annotate()`, or chaining queries.
