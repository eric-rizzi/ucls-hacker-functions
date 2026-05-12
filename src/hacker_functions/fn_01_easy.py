def shipping_cost(weight: int, is_member: bool) -> float:
    """
    Calculate the shipping cost for a package. Members get a 50% discount.
    Packages 5 pounds or under cost $10. Packages over 5 pounds cost $20.

    Bug: Should be `<=` in first comparison
 
    :param weight: The weight of the package in pounds
    :param is_member: Whether the customer is a member
    :returns: The shipping cost as a float
    """
    if weight < 5:
        cost = 10.0
    else:
        cost = 20.0
 
    if is_member == True:
        cost = cost * 0.5
 
    return cost


def rock_paper_scissors(player: str, opponent: str) -> str:
    """
    Determine the winner of a round of rock-paper-scissors. Returns "player"
    if the player wins, "opponent" if the opponent wins, and "tie" if both
    chose the same thing.
 
    Bug: Missing one of the key conditions for victory
    
    :param player: The player's choice ("rock", "paper", or "scissors")
    :param opponent: The opponent's choice ("rock", "paper", or "scissors")
    :returns: "player", "opponent", or "tie"
    """
    if player == opponent:
        return "tie"
    elif player == "rock" and opponent == "scissors":
        return "player"
    elif player == "paper" and opponent == "rock":
        return "player"
    else:
        return "opponent"


def can_ride_coaster(height: int, age: int) -> bool:
    """
    Determine whether someone can ride the roller coaster. A rider must be
    at least 48 inches tall AND at least 8 years old.
 
    Bug: Should be `and` instead of `or`
    
    :param height: The rider's height in inches
    :param age: The rider's age in years
    :returns: T/F about whether the rider can ride
    """
    if height >= 48 or age >= 8:
        return True
    return False


def average(numbers: list[int]) -> float:
    """
    Get the average of a list of integers. Returns 0 if the list is empty.

    Bug: Guard doesn't work so get DivisionByZero

    :param numbers: List of integers
    :returns: Float representing the average
    """
    if len(numbers) < 0:
        return 0.0

    return sum(numbers) / len(numbers)


def first_and_last(items: list[int]) -> tuple[int, int]:
    """
    Return a tuple of the first and last item in a list.
    For example, [3, 7, 2, 9] should return (3, 9). If there
    are less than 2 items, return (0, 0)

    Bug: Returns first and second rather than first and last
 
    :param items: The list to extract from
    :returns: A tuple of (first item, last item)
    """
    if len(items) < 2:
        return (0, 0)

    return (items[0], items[1])


def days_in_month(month: int) -> int:
    """
    Return the number of days in a given month. February is assumed to have
    28 days (ignore leap years). Months are numbered 1-12.

    Bug: Handles nonsensical months
 
    :param month: The month number (1 = January, 12 = December)
    :returns: The number of days in that month
    """
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    if month in [4, 6, 9, 11]:
        return 30
    return 28


def contains_an_a(word: str) -> bool:
    """
    Checks whether a given string contains an "a" character

    Bug: Assumes that words can't be over 100 chars in length

    :param word: The word/string to check for an "a"
    :returns: T/F about whether an "a" was found
    """
    for i in range(100):
        if i < len(word) and word[i] == "a":
            return True

    return False


def last_word(sentence: str) -> str:
    """
    Return the last word in a sentence. Words are separated by spaces.
    For example, "hello there friend" should return "friend".

    Bug: Breaks for an empty string
 
    :param sentence: The sentence to extract the last word from
    :returns: The last word in the sentence
    """
    words = sentence.split(" ")
    return words[-1]


def triangle_type(a: int, b: int, c: int) -> str:
    """
    Determine the type of a triangle based on the length of three sides

    Bug: Misses a case where `c == a`

    :param a: Length of side a
    :param b: Length of side b
    :param c: Length of side c
    :returns: The type of triangle: Scalene, Equilateral, or Isosceles
    """

    if a == b == c:
        return "Equilateral"
    if a == b or b == c:
        return "Isosceles"
    else:
        return "Scalene"


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


def count_vowels(word: str) -> int:
    """
    Count the number of vowels in a given word

    Bug: Doesn't account for upper-case letters
 
    :param word: The word to count vowels in
    :returns: The number of vowels in the word
    """
    vowels = "aeiou"
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
    return count


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
