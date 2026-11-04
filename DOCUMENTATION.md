# DevOps Assignment 4: Git & GitHub Workflow Report

**Student Name:** Rahul Motvani  
**GitHub Username:** [rahulmotvani0-sketch](https://github.com/rahulmotvani0-sketch)  
**GitHub Repository:** [https://github.com/rahulmotvani0-sketch/Git_and_GitHub_Assignment](https://github.com/rahulmotvani0-sketch/Git_and_GitHub_Assignment)  
**Technology Stack:** Python Flask 3.1.3, MongoDB 7.x, Bootstrap 5.3, Git, GitHub  

---

## 1. Executive Summary
This project implements the complete Git and GitHub workflow using a Flask web application with MongoDB integration.
Key DevOps capabilities demonstrated:
1. **SSH Key Pair Generation & GitHub Deploy Key Authentication**: Secure, non-interactive passwordless repository management.
2. **Feature Branching & Flask Application Setup**: Initial development isolated on branch `rahulmotvani` and non-fast-forward merge to `main`.
3. **Merge Conflict Trigger & Resolution**: Concurrent updates to `data/items.json`, triggering authentic merge conflict markers (`<<<<<<< HEAD`, `=======`, `>>>>>>> rahul_new`), and resolving by accepting incoming changes (`git checkout --theirs`).
4. **Parallel Feature Development**: Simultaneous branches `master_1` (frontend To-Do form with `Item Name` and `Item Description`) and `master_2` (backend `/submittodoitem` route persisting records to MongoDB), merged into `main`.
5. **Sequential Commits & Atomic History**: Enhancing the To-Do form with `Item ID`, `Item UUID`, and `Item Hash` as three separate atomic commits.
6. **Soft Reset & Rebase**: Executing `git reset --soft` on `main` to inspect staged changes, re-committing state, and running `git rebase main master_1` while preserving individual commits without squashing.

---

## 2. Task 1: Repository Setup & First Branch
### Commands Executed:
```bash
# 1. Generate SSH key pair
ssh-keygen -t ed25519 -N "" -f ~/.ssh/id_ed25519_assignment -C "rahulmotvani0-sketch"

# 2. Add public key as Deploy Key with write access to GitHub repo
gh api repos/rahulmotvani0-sketch/Git_and_GitHub_Assignment/keys \
  -f title="Assignment Key" \
  -f key="$(cat ~/.ssh/id_ed25519_assignment.pub)" \
  -F read_only=false

# 3. Test SSH authentication
ssh -T git@github.com
# Hi rahulmotvani0-sketch/Git_and_GitHub_Assignment! You've successfully authenticated...

# 4. Clone repository
git clone git@github.com:rahulmotvani0-sketch/Git_and_GitHub_Assignment.git Git_and_GitHub_Rahul
cd Git_and_GitHub_Rahul

# 5. Create user branch and add Flask project
git checkout -b rahulmotvani
# Created app.py, data/items.json, templates/, static/, requirements.txt, .gitignore
git add .
git commit -m "feat: add Flask project files and /api route on rahulmotvani"

# 6. Merge into main and push
git checkout main
git merge --no-ff rahulmotvani -m "Merge branch 'rahulmotvani' into main"
git push -u origin main rahulmotvani
```

---

## 3. Task 2: Update JSON & Resolve Conflicts
### Commands Executed:
```bash
# 1. Create branch rahul_new and update API JSON
git checkout -b rahul_new main
# Updated data/items.json to v2.0 schema
git commit -am "feat(api): update JSON data content for /api route on rahul_new"

# 2. Concurrent commit on main to trigger merge conflict
git checkout main
# Modified data/items.json to v1.1.0-mainline
git commit -am "chore(api): update JSON data content on main branch"

# 3. Attempt merge to trigger conflict
git merge rahul_new
# Output:
# Auto-merging data/items.json
# CONFLICT (content): Merge conflict in data/items.json
# Automatic merge failed; fix conflicts and then commit the result.

# 4. Resolve conflict by accepting changes from rahul_new (theirs)
git checkout --theirs data/items.json
git add data/items.json
git commit -m "fix(merge): resolve merge conflict in data/items.json by accepting changes from rahul_new"
git push origin main rahul_new
```

---

## 4. Task 3: Parallel Feature Development
### Commands Executed:
```bash
# 1. Create parallel branches from main
git checkout main
git checkout -b master_1
git checkout main
git checkout -b master_2

# 2. Frontend Development on master_1
git checkout master_1
# Created templates/todo.html with Item Name and Item Description form
# Added /todo route in app.py
git add templates/todo.html app.py
git commit -m "feat(frontend): create To-Do Page with Item Name and Item Description form"

# 3. Backend API Development on master_2
git checkout master_2
# Configured PyMongo client and created /submittodoitem POST route
git commit -am "feat(backend): add /submittodoitem route storing items in MongoDB"

# 4. Merge both branches into main
git checkout main
git merge --no-ff master_1 -m "merge: integrate frontend To-Do page from master_1 into main"
git merge --no-ff master_2
# Integrated app.py preserving both /todo and /submittodoitem
git add app.py
git commit -m "merge: integrate backend /submittodoitem route from master_2 into main"
git push origin main master_1 master_2
```

---

## 5. Task 4: Sequential Commits, Reset & Rebase
### Commands Executed:
```bash
# 1. Three Sequential Commits on master_1
git checkout master_1

# Commit 1: Item ID
git add templates/todo.html
git commit -m "feat(todo): add Item ID field to To-Do form"

# Commit 2: Item UUID
git add templates/todo.html
git commit -m "feat(todo): add Item UUID field to To-Do form"

# Commit 3: Item Hash
git add templates/todo.html
git commit -m "feat(todo): add Item Hash field to To-Do form"

# 2. Merge master_1 to main
git checkout main
git merge --no-ff master_1 -m "merge: integrate enhanced To-Do form with Item ID, UUID, and Hash from master_1"

# 3. Roll back to commit where ONLY Item ID was added via git reset --soft
git reset --soft f03e83f
git status
# Confirms changes remain staged in the index

# 4. Re-commit state on main with backend MongoDB integration
git commit -m "feat(main): re-commit state at Item ID stage with backend MongoDB integration"

# 5. Rebase main onto master_1 preserving individual commits
git rebase main master_1
# Output:
# Rebasing (1/2)
# Rebasing (2/2)
# Successfully rebased and updated refs/heads/master_1.

# 6. Verify individual commits are preserved
git log --oneline -n 4
# 4b36450 (HEAD -> master_1) feat(todo): add Item Hash field to To-Do form
# c6d14a5 feat(todo): add Item UUID field to To-Do form
# 0a64975 (main) feat(main): re-commit state at Item ID stage with backend MongoDB integration
# f03e83f feat(todo): add Item ID field to To-Do form
```

---

## 6. Commit History Graph
```text
* 89b2968 (HEAD -> main, origin/main) fix(ui): resolve Jinja2 dict items reference and modernize datetime
* 4b36450 (origin/master_1, master_1) feat(todo): add Item Hash field to To-Do form
* c6d14a5 feat(todo): add Item UUID field to To-Do form
* 0a64975 feat(main): re-commit state at Item ID stage with backend MongoDB integration
* f03e83f feat(todo): add Item ID field to To-Do form
* b88a624 feat(frontend): create To-Do Page with Item Name and Item Description form
| * 9ee0ba7 (origin/master_2, master_2) feat(backend): add /submittodoitem route storing items in MongoDB
|/  
*   50f4ef5 fix(merge): resolve merge conflict in data/items.json by accepting changes from rahul_new
|\  
| * b54fb5c (origin/rahul_new, rahul_new) feat(api): update JSON data content for /api route on rahul_new
* | 5f67d2e chore(api): update JSON data content on main branch
|/  
*   6bfcb8a Merge branch 'rahulmotvani' into main
|\  
| * 6026c99 (origin/rahulmotvani, rahulmotvani) feat: add Flask project files and /api route on rahulmotvani
|/  
* 4e050b4 chore: initial repository setup
```

---

## 7. Submission Details
- **Folder:** `Git_and_GitHub_Rahul`
- **Compressed Archive:** `Git_and_GitHub_Rahul.zip`
- **Documentation:** `Assignment_4_Git_and_GitHub_Report.docx` and `Assignment_4_Git_and_GitHub_Report.pdf`
- **GitHub Repository:** [https://github.com/rahulmotvani0-sketch/Git_and_GitHub_Assignment](https://github.com/rahulmotvani0-sketch/Git_and_GitHub_Assignment)
