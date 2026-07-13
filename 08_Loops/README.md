# Loops in Python

## 📌 Overview

Loops are used to execute a block of code repeatedly until a specific condition is satisfied.

Loops help reduce code repetition and make programs more efficient.

Python mainly provides two types of loops:

* `for loop`
* `while loop`

---

## 📚 Topics Covered

* Introduction to Loops
* for Loop
* while Loop
* range() Function
* Nested Loops
* break Statement
* continue Statement
* pass Statement
* Loop with Strings
* Loop with Lists
* Loop with Dictionaries
* Loop with Sets

---

## 🎯 Learning Objectives

After completing this topic, you will understand:

* How to repeat tasks using loops.
* Difference between for and while loops.
* How to control loops.
* How loops work with data structures.
* How to solve real-world problems using loops.

---

## 📂 Files

| File            | Description            |
| --------------- | ---------------------- |
| practice.py     | Loop practice examples |
| tasks.md        | Practice questions     |
| mini_project.py | Loop based project     |

---

## 🔹 For Loop Syntax

```python id="h4o7m1"
for variable in sequence:
    statement
```

Example:

```python id="xj3z9m"
for i in range(5):
    print(i)
```

---

## 🔹 While Loop Syntax

```python id="k6w2pv"
while condition:
    statement
```

Example:

```python id="x9u4dp"
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

## 🛠️ Loop Control Statements

| Statement | Purpose                 |
| --------- | ----------------------- |
| break     | Stops the loop          |
| continue  | Skips current iteration |
| pass      | Placeholder statement   |

---

## 💡 Best Practices

* Avoid infinite loops.
* Use meaningful loop variables.
* Prefer for loop when number of iterations is known.
* Use while loop when condition-based repetition is needed.

---

## ❌ Common Mistakes

* Forgetting to update while loop condition.
* Wrong indentation.
* Creating infinite loops.
* Using unnecessary nested loops.

---

## 🚀 Mini Project

Create a Number Guessing Game.

Features:

* Generate a number.
* Take user guesses.
* Give hints.
* Count attempts.

---

## 📖 What I Learned

* Loops automate repeated tasks.
* for loop works with sequences.
* while loop works with conditions.
* break and continue control loop execution.

---

## 🚀 Next Topic

Functions
