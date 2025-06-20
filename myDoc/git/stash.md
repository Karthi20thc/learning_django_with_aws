`git stash` is a Git command used to temporarily save (or "stash") changes in your working directory that are not yet committed. This is useful when you want to:

* Switch branches without committing unfinished work.
* Clean up your working directory quickly.

---

### 🔧 Basic Usage

```bash
git stash
```

This stashes:

* Tracked modified files
* Staged files

It does **not** stash:

* Untracked files (unless specified)
* Ignored files (unless specified)

---

### 📦 View Stashes

```bash
git stash list
```

Shows a list of stashes, like:

```
stash@{0}: WIP on feature-branch: abc1234 Some message
stash@{1}: WIP on master: def5678 Another message
```

---

### 🧩 Apply a Stash

```bash
git stash apply        # Applies the latest stash
git stash apply stash@{1}  # Applies a specific stash
```

> Changes are re-applied, but the stash is **not removed**.

---

### ✅ Apply and Remove (Pop)

```bash
git stash pop          # Applies and removes the latest stash
```

---

### 🗑️ Drop or Clear Stashes

```bash
git stash drop stash@{0}   # Remove a specific stash
git stash clear            # Remove all stashes
```

---

### 🚀 Stash Untracked & Ignored Files

```bash
git stash -u   # Include untracked files
git stash -a   # Include untracked + ignored files
```

---

### 🔄 Create Named Stash

```bash
git stash push -m "work in progress on validation"
```

---

Let me know what you're trying to do with `git stash` and I can tailor the explanation.
