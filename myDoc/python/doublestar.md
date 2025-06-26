The `**` syntax in Python is used to **unpack a dictionary into keyword arguments** when calling a function.

For example:
```python
data = {'username': 'john', 'email': 'john@example.com'}
UserModel.objects.create(**data)
```
is equivalent to:
```python
UserModel.objects.create(username='john', email='john@example.com')
```

**Why use `**`?**
- It allows you to pass a dictionary of parameters as named arguments to a function or method.
- It’s useful when you have dynamic or variable sets of data.

**Summary:**  
`**` unpacks a dictionary so its keys become parameter names and its values become parameter values in a function call.