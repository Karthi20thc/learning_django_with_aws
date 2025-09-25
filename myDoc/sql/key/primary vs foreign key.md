Here’s a clear breakdown of **Primary Key vs Foreign Key**:

---

### 🔑 **Primary Key**

* A **unique identifier** for each record (row) in a table.
* Ensures **uniqueness** → no two rows can have the same primary key value.
* Cannot be **NULL**.
* A table can have **only one primary key**, but it may consist of one or multiple columns (called a composite key).

✅ Example:

```sql
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    Name VARCHAR(100),
    Age INT
);
```

Here, `StudentID` uniquely identifies each student.

---

### 🔗 **Foreign Key**

* A column (or set of columns) in one table that **refers to the primary key** in another table.
* Creates a **relationship between two tables**.
* Helps enforce **referential integrity** (you can’t insert a foreign key value that doesn’t exist in the parent table).
* Can be **NULL** (if relationship is optional).

✅ Example:

```sql
CREATE TABLE Enrollments (
    EnrollmentID INT PRIMARY KEY,
    StudentID INT,
    CourseID INT,
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID)
);
```

Here, `StudentID` in `Enrollments` is a **foreign key** referencing `StudentID` in `Students`.

---

### ⚖️ Key Differences

| Feature         | Primary Key                               | Foreign Key                                      |
| --------------- | ----------------------------------------- | ------------------------------------------------ |
| Purpose         | Uniquely identifies a record in the table | Establishes a link between two tables            |
| Uniqueness      | Must be unique                            | Can have duplicate values                        |
| NULL values     | Not allowed                               | Allowed (unless explicitly restricted)           |
| Count per table | Only one (but can be composite)           | Can have multiple                                |
| Location        | Defined in the same table                 | Defined in child table, referencing parent table |

---

👉 Would you like me to also **draw a simple diagram** to show visually how a primary key and foreign key connect two tables?
