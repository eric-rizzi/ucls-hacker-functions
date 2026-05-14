def convert_to_usd(num_dollars: int, currency: str) -> float:
    """
    Calculate how much money a certain number of dollars would be in another
    denomination

    Bug: Fails to handle cases where currency is not in rates dictionary

    :param num_dollars: The number of dollars to convert
    :param currency: The currency to convert to
    """
    # Converts an amount from a specified currency to USD.
    rates = {"EUR": 1.1, "JPY": 0.0091}
    return num_dollars * rates[currency]


def is_valid_email(email: str) -> bool:
    """
    Determines whether a given string is a valid email address

    Bug: Doesn't validate that there's content before the @

    :param email: Potential email address
    :returns: T/F about whether the `email` was a valid email address
    """
    return "@" in email and "." in email.split("@")[1]


def sum_of_digits(n: int) -> int:
    """
    Adds up all of the digits in a particular number. For example, 12 would
    result in `3` (1 + 2) being returned.

    Bug: Fails to account for negative numbers

    :params n: the number to process
    :returns: The sum of the digits in `n`
    """
    return sum(int(char) for char in str(n))


def pair_items_in_list(items: list[int]) -> list[tuple[int, int]]:
    """
    Take a list of integers and create a new list where items 0 and 1 are
    paired, items 2 and 3 are paired, items 4 and 5 are paired ....

    For example [1, 5, 7, 4] -> [(1, 5), (7, 4)].

    Bug: Crashes with IndexError when the list has an odd number of items

    :param items: The list of items to "pair up"
    :returns: The list of paired items
    """
    processed: list[tuple[int, int]] = []

    i = 0
    while i < len(items):
        # Processes in pairs
        processed.append((items[i], items[i + 1]))
        i += 2

    return processed


def find_median(numbers: list[int]) -> int:
    """
    Find the median (middle) number for a list of numbers

    Bug: Incorrect for even-length lists

    :param numbers: The list of numbers to find the median for
    :returns: The median (middle) number
    """
    sorted_numbers = sorted(numbers)
    return sorted_numbers[len(sorted_numbers) // 2]


def count_unique(items: list[int]) -> int:
    """
    Count the number of unique items in a list.
    For example, [1, 2, 2, 3, 3, 3] should return 3.

    Bug: Returns too early

    :param items: The list to count unique items in
    :returns: The number of unique items
    """
    unique_count = 0
    for i in range(len(items)):
        is_unique = True
        for j in range(i):
            if items[i] == items[j]:
                is_unique = False
        if is_unique:
            unique_count += 1
        else:
            return unique_count
    return unique_count


def remove_duplicates(items: list[int]) -> list[int]:
    """
    Return a new list with duplicate items removed, preserving the order
    of first appearance.
    For example, [3, 1, 4, 1, 5, 9, 2, 6, 5, 3] should return [3, 1, 4, 5, 9, 2, 6].

    Bug: Keeps last occurrence instead of first

    :param items: The list to deduplicate
    :returns: A new list with duplicates removed
    """
    result: list[int] = []
    for i in range(len(items)):
        is_duplicate = False
        for j in range(i + 1, len(items)):
            if items[i] == items[j]:
                is_duplicate = True
        if not is_duplicate:
            result.append(items[i])
    return result


def binary_search(sorted_items: list[int], target: int) -> int:
    """
    Search for `target` in a sorted list. Returns the index of the target
    if found, or -1 if not found.

    Bug: Loop bound while low < high instead of <= high

    :param sorted_items: A list of integers in ascending order
    :param target: The integer to search for
    :returns: The index of target, or -1 if not found
    """
    low = 0
    high = len(sorted_items) - 1
    while low < high:
        mid = (low + high) // 2
        if sorted_items[mid] == target:
            return mid
        elif sorted_items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def group_by_first_letter(words: list[str]) -> dict[str, list[str]]:
    """
    Group a list of words into a dictionary keyed by their first letter.
    For example, ["apple", "ant", "bee", "cat", "cow"] should return
    {"a": ["apple", "ant"], "b": ["bee"], "c": ["cat", "cow"]}.

    Bug: Assumes words are non-zero

    :param words: The list of words to group
    :returns: A dictionary mapping first letters to lists of words
    """
    groups: dict[str, list[str]] = {}
    for word in words:
        first = word[0]
        if first not in groups:
            groups[first] = []
        groups[first].append(word)
    return groups


def longest_streak(numbers: list[int]) -> int:
    """
    Return the length of the longest streak of consecutive equal numbers.
    For example, [1, 1, 2, 2, 2, 3, 3] should return 3 (the three 2's).

    :param numbers: The list of integers to scan
    :returns: The length of the longest run of equal consecutive values
    """
    longest = 0
    current = 1
    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i - 1]:
            current += 1
            if current > longest:
                longest = current
        else:
            current = 1
    return longest
