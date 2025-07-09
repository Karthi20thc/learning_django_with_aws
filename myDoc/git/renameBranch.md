To **rename a Git branch** both **locally** and **remotely**, follow these steps:

---

### ✅ 1. **Rename the local branch**

If you're **on the branch** you want to rename:

```bash
git branch -m new-branch-name
```

If you're **on a different branch**:

```bash
git branch -m old-branch-name new-branch-name
```

---

### ✅ 2. **Delete the old branch on the remote**

```bash
git push origin --delete old-branch-name
```

---

### ✅ 3. **Push the new branch to the remote**

```bash
git push origin new-branch-name
```

---

### ✅ 4. **Reset the upstream tracking for the new branch**

If you want your local branch to track the new remote branch:

```bash
git push --set-upstream origin new-branch-name
```

---

### ✅ Full example:

```bash
git branch -m feature/login feature/auth         # Rename locally
git push origin --delete feature/login           # Delete old remote
git push origin feature/auth                     # Push new branch
git push --set-upstream origin feature/auth      # Set upstream
```

Let me know if you're using GitHub, GitLab, or another Git host — the steps are the same, but I can help automate or script it for you.
