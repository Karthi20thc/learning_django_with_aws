
### 📝 Will installing a new package update `requirements.txt` automatically?

❌ **No, installing a package via `pip install` does NOT automatically update `requirements.txt`.**
You have to update it manually or generate it with `pip freeze`.

---

### ✅ How to update `requirements.txt` after installing a package

After installing a package (e.g., `pip install psycopg2-binary`), run:

```bash
pip freeze > requirements.txt
```

This will **regenerate the `requirements.txt` file** with the current state of all installed packages in your virtual environment.



