Sure! Let’s go through **all the common types of keys in relational databases** with clear explanations and examples. I’ll focus on **Primary Key, Unique Key, Foreign Key, Candidate Key, Alternate Key, Composite Key, Super Key**.

---

### **1. Primary Key (PK)**

* **Definition:** Uniquely identifies each row in a table. Cannot be `NULL`.
* **Example:**

```sql
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    Name VARCHAR(50),
    Age INT
);
```

* Here, `StudentID` is the primary key. Each student must have a unique `StudentID`.

---

### **2. Unique Key (UK)**

* **Definition:** Ensures all values in a column (or group of columns) are unique. Can allow `NULL` (depending on DBMS).
* **Example:**

```sql
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    Email VARCHAR(100) UNIQUE,
    Name VARCHAR(50)
);
```

* `Email` must be unique for each student but is **not the primary identifier**.

---

### **3. Foreign Key (FK)**

* **Definition:** A column (or set of columns) in one table that **references the primary key** in another table. Maintains referential integrity.
* **Example:**

```sql
CREATE TABLE Courses (
    CourseID INT PRIMARY KEY,
    CourseName VARCHAR(50)
);

CREATE TABLE Enrollments (
    EnrollmentID INT PRIMARY KEY,
    StudentID INT,
    CourseID INT,
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);
```

* `StudentID` in `Enrollments` refers to `Students.StudentID`.
* `CourseID` in `Enrollments` refers to `Courses.CourseID`.

---

### **4. Candidate Key**

* **Definition:** A column (or combination) that **could be chosen as the primary key**. A table can have multiple candidate keys.
* **Example:**

```text
Table: Employees
Columns: EmployeeID, Email, SSN
```

* `EmployeeID`, `Email`, and `SSN` could each uniquely identify an employee.
* One will be chosen as the **primary key**, the others are candidate keys.

---

### **5. Alternate Key**

* **Definition:** A candidate key that **was not chosen as the primary key**.
* **Example:**

```sql
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    Email VARCHAR(100) UNIQUE,
    SSN VARCHAR(20) UNIQUE
);
```

* `EmployeeID` → primary key
* `Email` and `SSN` → alternate keys

---

### **6. Composite Key**

* **Definition:** A primary key made up of **two or more columns**.
* **Example:**

```sql
CREATE TABLE EnrollmentDetails (
    StudentID INT,
    CourseID INT,
    EnrollmentDate DATE,
    PRIMARY KEY (StudentID, CourseID)
);
```

* Here, the combination of `StudentID` and `CourseID` uniquely identifies each enrollment.

---

### **7. Super Key**

* **Definition:** A set of columns that **uniquely identifies a row**. Every primary key is a super key, but not every super key is minimal.
* **Example:**

```text
Table: Employees
Columns: EmployeeID, Email, SSN

Super Keys:
1. {EmployeeID}
2. {Email}
3. {EmployeeID, Email}
4. {EmployeeID, Email, SSN}
```

* The minimal super keys (those with no extra columns) are the **candidate keys**.

---

✅ **Summary Table**

| Key Type      | Unique? | Null Allowed? | Can have multiple? | Example Column(s)          |
| ------------- | ------- | ------------- | ------------------ | -------------------------- |
| Primary Key   | Yes     | No            | No                 | StudentID                  |
| Unique Key    | Yes     | Sometimes     | Yes                | Email                      |
| Foreign Key   | No      | Yes           | Yes                | StudentID (in Enrollments) |
| Candidate Key | Yes     | No            | Yes                | SSN, EmployeeID            |
| Alternate Key | Yes     | No            | Yes                | Email (if not PK)          |
| Composite Key | Yes     | No            | Yes                | StudentID + CourseID       |
| Super Key     | Yes     | No            | Yes                | EmployeeID + Email         |

---

If you want, I can **draw a simple diagram showing all these keys visually in one example table**, which makes it super easy to understand.

Do you want me to do that?
