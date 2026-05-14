def categorize_grade(grade: int) -> str:
    """
    Translate a number grade to a letter grade

    Bug: Logic error due to an `elif` being mistyped as an `if`

    :param grade: The current grade of the student as an integer
    :returns: The string letter grade (e.g., "C+")
    """
    letter_grade = ""
    if grade >= 97:
        letter_grade = "A+"
    if grade >= 93:
        letter_grade = "A"
    elif grade >= 90:
        letter_grade = "A-"
    elif grade >= 87:
        letter_grade = "B+"
    elif grade >= 83:
        letter_grade = "B"
    elif grade >= 80:
        letter_grade = "B-"
    elif grade >= 77:
        letter_grade = "C+"
    elif grade >= 73:
        letter_grade = "C"
    elif grade >= 70:
        letter_grade = "C-"
    elif grade >= 67:
        letter_grade = "D+"
    elif grade >= 63:
        letter_grade = "D"
    elif grade >= 60:
        letter_grade = "D-"
    else:
        letter_grade = "F"

    return letter_grade


def capitalize_first(s: str) -> str:
    """
    Capitalize the first letter of a word/sentence

    Bug: Fails when s is empty

    :param s: The word/sentence to capitalize
    :returns: The updated (capitalized) string
    """
    return s[0].upper() + s[1:]


def find_middle(a: int, b: int, c: int) -> int:
    """
    Find the second largest of three numbers. For example, given the inputs
    (3, 6, 5), the function would return 5 since it's the second largest -
    middle number.

    Bug: Doesn't check for <=

    :param a: First integer
    :param b: Second integer
    :param c: Third integer
    :returns: The middle - second largest - number
    """
    if a < b < c:
        return b
    elif a < c < b:
        return c
    elif b < c < a:
        return c
    elif b < a < c:
        return a
    elif c < a < b:
        return a
    else:
        return b


def is_palindrome(word: str) -> bool:
    """
    Checks whether a given word is a palindrome or not

    Bug: Only checks whether the first letters are the same

    :param word: The word to check for palindrome-ness
    :returns: T/F of whether the word is a palindrome
    """
    for i in range(len(word) // 2):
        if word[i] == word[-1 + -i]:
            return True

    return False


def count_matches(l: list[str], word: str) -> int:
    """
    Count the number of times a given word appears in a list of words

    Bug: Off by one error

    :param l: The list of strings/words
    :param word: The word to look for matches for
    """
    matches = 0
    for i in range(len(l) - 1):
        if l[i] == word:
            matches += 1
    return matches


def find_in_list(lst: list[int], item: int) -> bool:
    """
    Determines whether a given item appears in a list

    Bug: Function returns False too early

    :param lst: A list of integers
    :param item: The item to look for in the list
    :returns: T/F about whether the item is in the list
    """
    for i in lst:
        if i == item:
            return True
        elif i > item:
            return False
    return False


def strings_are_equal(s1: str, s2: str) -> bool:
    """
    Determine whether two strings are equal

    Bug: Assumes the strings are of equal length

    :param s1: The first string
    :param s2: The second string
    :returns: T/F of whether the two strings are equal
    """
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False

    return True


def max_number(numbers: list[int]) -> int:
    """
    Find the largest number in a list of integers

    Bug: Assumes that the list is non-empty

    :param numbers: List of numbers
    :returns: The largest integer in the list of numbers
    """
    max_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
    return max_num


def sum_evens(numbers: list[int]) -> int:
    """
    Return the sum of all even numbers in the list.
    For example, [1, 2, 3, 4, 5] should return 6 (2 + 4).

    Bug: `total` isn't being added to

    :param numbers: The list of integers to scan
    :returns: The sum of the even numbers
    """
    total = 0
    for n in numbers:
        if n % 2 == 0:
            total = n
    return total
