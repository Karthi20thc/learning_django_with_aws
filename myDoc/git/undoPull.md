# How to Undo a Git Pull

If you've performed a `git pull` and want to undo it, here are several methods depending on your situation:

## Method 1: Undo a merge pull (most common case)

```bash
git reset --hard ORIG_HEAD
```

This reverts your local branch to the state before the pull/merge.

## Method 2: If you want to keep changes as uncommitted

```bash
git reset --merge ORIG_HEAD
```

## Method 3: If you pulled a fast-forward update

```bash
# Find the commit hash before the pull
git reflog
# Then reset to that commit
git reset --hard <commit-hash>
```

## Method 4: If you want to completely undo the merge and the commit

```bash
git reset --hard HEAD~1
```

## Important Notes:

1. These commands will discard local changes - make sure to stash them first if needed
2. `ORIG_HEAD` is a reference to the previous state of HEAD before dangerous operations
3. If you've already pushed the changes, you'll need to force push after resetting (use with caution)

Would you like more specific instructions for your particular situation?
