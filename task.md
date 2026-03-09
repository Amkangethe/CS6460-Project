Task 1: Count Vowels

Function
count_vowels(s: str) -> int

Description
Return the number of vowels in the given string. Vowels include a, e, i, o, u and should be counted regardless of case.

Example
Input: "hello"
Output: 2

Edge Example
Input: "sky"
Output: 0

---------------------------------------------------------------------------------------

Task 2: Running Sum

Function
running_sum(nums: list[int]) -> list[int]

Description
Return a new list where each element is the running total of the numbers up to that position.

Example
Input: [1, 2, 3, 4]
Output: [1, 3, 6, 10]

Edge Example
Input: []
Output: []

---------------------------------------------------------------------------------------

Task 3: Remove Duplicates

Function
dedupe(nums: list[int]) -> list[int]

Description
Return a new list with duplicate values removed while preserving the original order of elements.

Example
Input: [1, 2, 2, 3]
Output: [1, 2, 3]

Edge Example
Input: [5, 5, 5]
Output: [5]

---------------------------------------------------------------------------------------

Task 4: Reverse Words

Function
reverse_words(sentence: str) -> str

Description
Return a new string where the order of the words is reversed.

Example
Input: "hello world"
Output: "world hello"

Edge Example
Input: "python"
Output: "python"

---------------------------------------------------------------------------------------

Task 5: Find Maximum Value

Function
my_max(nums: list[int]) -> int

Description
Return the largest number in the list. Do not use Python’s built-in max() function.

Example
Input: [1, 5, 3, 9, 2]
Output: 9

Edge Example
Input: [7]
Output: 7

---------------------------------------------------------------------------------------

Task 6: Palindrome Check

Function
is_palindrome(s: str) -> bool

Description
Return True if the string reads the same forwards and backwards. Otherwise return False.

Example
Input: "racecar"
Output: True

Edge Example
Input: "python"
Output: False

---------------------------------------------------------------------------------------

Task 7: Letter Grade

Function
letter_grade(score: int) -> str

Description
Return a letter grade based on the score.

Grading scale
A: 90–100
B: 80–89
C: 70–79
D: 60–69
F: below 60

Example
Input: 95
Output: "A"

Edge Example
Input: 50
Output: "F"

---------------------------------------------------------------------------------------

Task 8: FizzBuzz

Function
fizzbuzz(n: int) -> list[str]

Description
Return a list of numbers from 1 to n following FizzBuzz rules.

Rules
Multiples of 3 → "Fizz"
Multiples of 5 → "Buzz"
Multiples of both → "FizzBuzz"

Example
Input: 5
Output: ["1", "2", "Fizz", "4", "Buzz"]

Edge Example
Input: 0
Output: []