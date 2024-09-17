# def reverse_string(phrase):
#     """Reverse string,

#         >>> reverse_string('awesome')   
#         'emosewa'

#         >>> reverse_string('sauce')
#         'ecuas'
#     """
#     reversed_phrase = ''

#     last_index = len(phrase) - 1   
#     for i in range(last_index, -1, -1):  
#         reversed_phrase = reversed_phrase + phrase[i] 
#     return reversed_phrase


    #practice
def reverse_this_string(phrase): 
    reversed_phrase = '' # Initialize an empty string to hold the reversed characters
    last_index = len(phrase) -1 # Get the last index of the string
    for i in range(last_index, -1, -1): # Loop from last character to the first
        reversed_phrase += phrase[i] # Add each character in reverse order
    return reversed_phrase # Return the reversed string

print(reverse_this_string('I WILL BECOME A SOFTWARE ENGINEER!, THANK YOU MICHAEL!'))

    
            


        



     




    


