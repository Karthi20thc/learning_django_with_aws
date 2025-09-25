Great question 👍 — let’s break it down in simple terms with SQL Server in mind.

---

## 🔑 **Primary Key Constraint**

A **Primary Key (PK)** is:

* A column (or set of columns) that **uniquely identifies each row** in a table.
* A table can only have **one primary key**, but it can include multiple columns (composite PK).
* By default, SQL Server:

  * Creates a **unique index** on the PK.
  * **Does not allow NULL values** in a PK column.

👉 Example:

```sql
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,   -- Primary Key
    FirstName NVARCHAR(50),
    LastName NVARCHAR(50)
);
```

Here, `EmployeeID` uniquely identifies each employee. No two rows can have the same `EmployeeID`, and it can’t be `NULL`.

---

## 🔑 **Unique Constraint**

A **Unique Constraint** is:

* Ensures that all values in a column (or group of columns) are **unique** across rows.
* A table can have **multiple unique constraints**.
* Unlike a primary key:

  * A column in a unique constraint **can allow one NULL** (but only one, because two NULLs would violate uniqueness in SQL Server).

👉 Example:

```sql
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    Email NVARCHAR(100) UNIQUE,   -- Unique Constraint
    PhoneNumber NVARCHAR(20) UNIQUE
);
```

Here:

* `EmployeeID` → PK (required, unique, no NULL).
* `Email` → must be unique, but it’s not the primary identifier of the table.
* `PhoneNumber` → also must be unique.

---

## ⚖️ **Key Differences**

| Feature              | Primary Key                  | Unique Constraint                     |
| -------------------- | ---------------------------- | ------------------------------------- |
| **Purpose**          | Main identifier of a row     | Enforce uniqueness on other column(s) |
| **Number per table** | Only 1                       | Can have many                         |
| **NULLs allowed**    | Not allowed                  | Allowed (but only one NULL)           |
| **Index created**    | Clustered index (by default) | Non-clustered index (by default)      |

---

### ✅ Example Together

```sql
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,        -- PK (unique, not null)
    RollNumber NVARCHAR(20) UNIQUE,   -- must be unique, can have 1 null
    Email NVARCHAR(100) UNIQUE,       -- must be unique, can have 1 null
    Name NVARCHAR(50)
);
```

* `StudentID` → **PK** (main ID).
* `RollNumber` → **Unique** (no duplicates, but not the main key).
* `Email` → **Unique** (no duplicates, but not the main key).

---

👉 In your database, I saw `UK_CAID` — that means a **Unique Key** exists on `CAID`, while your `dbo.CATS` table likely has a `Primary Key` on `id`.

Do you want me to check **why someone would use a UNIQUE constraint on CAID in addition to the Primary Key on id** in your `CATS` table?
