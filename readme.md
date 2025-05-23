Starting a Django REST API project from scratch involves several steps. Here’s a step-by-step guide:

---

### ✅ Prerequisites

* Python installed (preferably 3.8+)
* pip installed
* Virtual environment tool (e.g., `venv`)
* Optional: `PostgreSQL` or other DB setup (default is SQLite)

---

### 📁 Step 1: Setup Project Directory

```bash
mkdir myproject
cd myproject
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
source venv/Scripts/activate  #bash
```

---

### 📦 Step 2: Install Django and Django REST Framework

```bash
pip install django djangorestframework
```

---

### 🚀 Step 3: Create Django Project

```bash
django-admin startproject backend .
```

---

### 🛠 Step 4: Create an App

```bash
python manage.py startapp api
```

---

### ⚙️ Step 5: Update `settings.py`

In `backend/settings.py`:

1. Add apps to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'api',
]
```

---

### 🗃 Step 6: Create a Model (Example: `Book`)

In `api/models.py`:

```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published = models.DateField()

    def __str__(self):
        return self.title
```

Then run:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 🧰 Step 7: Create Serializer

In `api/serializers.py`:

```python
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
```

---

### 🌐 Step 8: Create Views (API endpoints)

In `api/views.py`:

```python
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```

---

### 🛣 Step 9: Setup URLs

#### In `api/urls.py` (create this file if it doesn’t exist):

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

#### In `backend/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
```

---

### 🧪 Step 10: Run the Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/api/books/` to access the API.

---

### ✅ Bonus: Add a Book from Django Admin

* Create a superuser:

```bash
python manage.py createsuperuser
```

* Add `Book` to `admin.py`:

```python
from django.contrib import admin
from .models import Book

admin.site.register(Book)
```

---

Would you like to include authentication (like JWT) or deploy it to a platform (like Heroku or Render)?
