def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    frequencies = {}

    for char in phrase:
        if char in frequencies:
            frequencies[char] = frequencies[char] + 1
        else:
            frequencies[char] = 1

    return frequencies

print(multiple_letter_count('michael'))
print(multiple_letter_count('tenyay'))
print(multiple_letter_count('hello'))