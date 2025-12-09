"""
->  def is_even(n):
        if n % 2 == 0:
            return True
        else:
            return False
        
    print(is_even(2))

->  def max_of_two(a, b):
        if a > b:
            return a
        elif b > a:
            return b
        else:
            return "Both are equal"

    print(max_of_two(1, 2))

->  def count_vowels(n):
        count = 0
        for char in n:
            if char in "aeiouAEIOU":
                count += 1
        return count

    print(count_vowels("Hello"))    

->  def reverse_string(n):
        return n[::-1]

    print(reverse_string("Hello"))

->  def sum_list(*nums):
        tot = 0
        for num in nums:
            tot += num
        return tot

    print(sum_list(1, 2, 3))

->  def unique_elements(lst):
        unique = []
        for num in lst:
            if num not in unique:
                unique.append(num)
        return unique

    print(unique_elements([1, 2, 3, 4, 1, 2, 3]))

->  def factorial(n):
        fact = 1
        for i in range(1, n+1):
            fact *= i
        return fact

    print(factorial(5))

->  def is_palindrome(s):
        s = s.replace(" ", "").lower()    
        if s == s[::-1]:
            return True
        else:
            return False
    
    print(is_palindrome("ma dam"))

->  def find_min_max(lst):
        min = lst[0]
        max = lst[0]
        for num in lst:
            if num < min:
                min = num
            elif num > max:
                max = num
        return min, max

    print(find_min_max([1, 2, 3, 4, 5]))

->  def word_frequency(s):
    freq = {}
    for word in s.lower().split():
        freq[word] = freq.get(word, 0) + 1
    return freq

print(word_frequency("hello world hello"))
"""
