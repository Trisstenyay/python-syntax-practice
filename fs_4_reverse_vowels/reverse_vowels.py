def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
def reverse_vowels(s):

    vowels = "aeiouAEIOU"  # Set of vowels (both lowercase and uppercase)

    vowel_list = [char for char in s if char in vowels]  # List of vowels in the order they appear
    vowel_list.reverse()  # Reverse the order of the vowels

    result = []  # Initialize an empty list to build the new string
    for char in s:  # Loop through each character in the original string
        if char in vowels:  # Check if the character is a vowel
            result.append(vowel_list.pop(0))  # Replace it with the next vowel from the reversed list
        else:
            result.append(char)  # Keep non-vowel characters in their original positions

    return ''.join(result)  # Join the list of characters into a string and return it
