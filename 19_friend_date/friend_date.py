def friend_date(a, b):
    """Given two friends, do they have any hobbies in common?

    - a: friend #1, a tuple of (name, age, list-of-hobbies)
    - b: same, for friend #2

    Returns True if they have any hobbies in common, False is not.

        >>> elmo = ('Elmo', 5, ['hugging', 'being nice'])
        >>> sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
        >>> gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

        >>> friend_date(elmo, sauron)
        False

        >>> friend_date(sauron, gandalf)
        True
    """
    hobbies_a = a[2]  # Extract the list of hobbies from friend #1 (the 3rd element in the tuple)
    hobbies_b = b[2]  # Extract the list of hobbies from friend #2 (the 3rd element in the tuple)

    common_hobbies = set(hobbies_a) & set(hobbies_b)  # Use set intersection to find common hobbies

    return bool(common_hobbies)  # Return True if there are common hobbies, otherwise return False

