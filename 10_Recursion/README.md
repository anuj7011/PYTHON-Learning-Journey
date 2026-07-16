# Recursion in Python

## 📌 Overview

Recursion is a programming technique where a function calls itself to solve a problem. It is useful for problems that can be divided into smaller, similar subproblems.

Every recursive function must have a **base case** to stop the recursion. Without a base case, the function will continue calling itself and eventually raise a `RecursionError`.

---

## 📚 Topics Covered

* What is Recursion?
* Recursive Functions
* Base Case
* Recursive Case
* Call Stack
* Direct Recursion
* Advantages & Disadvantages
* Real-world Examples

---

## 🎯 Learning Objectives

After completing this topic, you will understand:

* How recursion works.
* Why a base case is important.
* How recursive calls are executed.
* Difference between recursion and loops.
* Common recursion problems.

---

## 📂 Files

| File            | Description                 |
| --------------- | --------------------------- |
| practice.py     | Recursion practice examples |
| tasks.md        | Practice questions          |
| mini_project.py | Recursion mini project      |

---

## 🔹 Recursion Syntax

```python
def function_name():
    if base_case:
        return value

    return function_name(smaller_problem)
```

---

## 🛠️ Common Recursion Problems

* Factorial
* Fibonacci Series
* Sum of Natural Numbers
* Reverse String
* Power Calculation
* Binary Search
* Tower of Hanoi (Advanced)

---

## 💡 Best Practices

* Always define a base case.
* Keep recursive functions simple.
* Avoid unnecessary recursive calls.
* Use recursion only when it makes the solution cleaner.

---

## ❌ Common Mistakes

* Forgetting the base case.
* Infinite recursion.
* Modifying variables incorrectly.
* Using recursion where loops are more suitable.

---

## 🚀 Mini Project

Create a Recursive Math Calculator.

Features:

* Factorial
* Power Calculation
* Sum of Numbers

---

## 📖 What I Learned

* A recursive function calls itself.
* Base case stops recursion.
* Recursive problems are solved by breaking them into smaller problems.
* Recursion is powerful but should be used carefully.

---

## 🚀 Next Topic

Modules
