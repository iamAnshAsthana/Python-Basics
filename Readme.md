# Python Interview Preparation – MCQs, Output Prediction & Coding Questions

## How to Use

- Try to solve all MCQs first.
- Then attempt output prediction without running the code.
- Finally, implement all coding questions in `solution.py` (or your own file).

This document contains three sections commonly asked in Python basic-level interviews:
- **Section A:** Multiple Choice Questions  
- **Section B:** Output Prediction  
- **Section C:** Coding Questions  

Use this to practice and revise before interviews.

---

## 🧩 Section A – MCQs (Basic Concepts)

1. What is the correct file extension for Python files?  
   A. `.pt`  
   B. `.py`  
   C. `.pyt`  
   D. `.python`

2. What will `type(3/2)` return in Python 3?  
   A. `<class 'int'>`  
   B. `<class 'float'>`  
   C. `<class 'decimal'>`  
   D. `<class 'complex'>`

3. Which of these is immutable?  
   A. `list`  
   B. `dict`  
   C. `set`  
   D. `tuple`

4. What is the output of `bool("")` ?  
   A. `True`  
   B. `False`  
   C. `None`  
   D. Error

5. Which of these creates a list?  
   A. `x = ()`  
   B. `x = []`  
   C. `x = {}`  
   D. `x = set()`

6. What is the index of the last element in a list of length `n`?  
   A. `n`  
   B. `n-1`  
   C. `n+1`  
   D. `0`

7. Which operator is used for exponentiation in Python?  
   A. `^`  
   B. `**`  
   C. `pow`  
   D. `//`

8. What will `len("hello\n")` return?  
   A. `5`  
   B. `6`  
   C. `7`  
   D. Error

9. Which of these is not a valid variable name?  
   A. `_value`  
   B. `value_1`  
   C. `1value`  
   D. `valueOne`

10. What does `pass` do in Python?  
    A. Skips the current loop iteration  
    B. Exits the loop  
    C. Does nothing (placeholder)  
    D. Raises an exception

11. Which is the correct way to import only `sqrt` from `math`?  
    A. `import math.sqrt`  
    B. `import sqrt from math`  
    C. `from math import sqrt`  
    D. `from math import *sqrt`

12. What is the type of `range(5)` in Python 3?  
    A. `list`  
    B. `tuple`  
    C. `range`  
    D. `iterator`

13. Which statement opens a file for reading text by default?  
    A. `open("file.txt")`  
    B. `open("file.txt", "w")`  
    C. `open("file.txt", "a")`  
    D. `open("file.txt", "wb")`

14. If a function has no return statement, what does it return?  
    A. `0`  
    B. `""`  
    C. `None`  
    D. Error

15. Which keyword is used to handle exceptions?  
    A. `throw`  
    B. `catch`  
    C. `try/except`  
    D. `error`

---

## 🧠 Section B – Predict the Output

1.
```python
-> a = 5
b = 2
print(a / b)
print(a // b)

-> x = [1, 2, 3]
y = x
y.append(4)
print(x, y)

-> print(2 ** 3 ** 2)

-> s = "python"
print(s[1:4])
print(s[-3:])

-> nums = [1, 2, 3, 4]
print(nums[::-1])

-> x = 10
def func():
    x = 5
    print("inside:", x)

func()
print("outside:", x)

-> def add(a, b=2, c=3):
    return a + b + c

print(add(1))
print(add(1, 5))
print(add(1, c=10))

-> for i in range(3):
    print(i)
else:
    print("done")

-> x = []
print(bool(x), bool([0]), bool(0))

-> def func(val, lst=[]):
    lst.append(val)
    return lst

print(func(1))
print(func(2))
print(func(3, []))
print(func(4))
```

## 🧑‍💻 Section C – Coding Questions

1. Write a function is_even(n) that returns True if n is even.

2. Write a function max_of_two(a, b) that returns the larger number without using max().

3. Write a function count_vowels(s) that returns how many vowels are present in the string.

4. Write a function reverse_string(s) that returns the reversed string.

5. Write a function sum_list(nums) that returns the sum without using sum().

6. Write a function unique_elements(lst) that returns a list of unique elements.

7. Write a function factorial(n) using a loop.

8. Write a function is_palindrome(s) that ignores case and spaces.

9. Write a function find_min_max(nums) that returns (min_value, max_value) without using built-in min() and max().

10. Write a function word_frequency(s) that returns a dictionary mapping each word to its count.
