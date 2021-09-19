"""
                            ~Caesar Cipher~

Difficulty: Comparable to the Primes Assignment
Focus: string functions, indexing, input and/or functions, loop

For this Assignment, you need to create a Caesar Cipher of some kind. 
You will need to ask the user for a sentence (or put into a function's parameter):

    Example:                                              
        Give me a Sentence: hello there!

And then convert it to a ciphered sentence using a "key". 
The key can be grabbed from the user (or put into a function's parameter')
And it should be an integer:

    Example:
        Give me an integer: 2

In this example, the Key is 2, therefore it will shift the sentence by 2 letters forward

    Example:
        New Sentence : jgnnq vjgtg!

Of course, document all assumptions. And don't be shy using str functions and such.

    Bonus marks for accounting for capitalization
    Bonus marks for making the key a letter rather than a number. So eg. B would shift 2 to the right.
    Bonus marks for making a function to decrypt
    Extra Extra Bonus marks if your code is more efficient than mine. Mine works, but I feel is inefficient
"""
# Scroll down for Hints. There are 7 in total, and the 7th hint is my solution

print("goodluck")













































# Hint 1-> to compare a letter against another letter, you can use these strings:
    # alphabet="abcdefghijklmnopqrstuvwxyz"
    # alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"










































# Hint 2-> You can use the .find() function on a string to find its index.
    # Then go ahead and do cool things with the index











































# Hint 3-> To prevent things from indexing too far, use %26 to ensure the index never goes 27 or over











































# Hint 4-> Starting here, I'm going to give you pieces of my actual code, then eventually my solution
# Scroll down like 10 lines













"""
raw_text = input("Give me a Sentence: ")
new_text = ""
key = int(input("Give me an integer: "))
alphabet="abcdefghijklmnopqrstuvwxyz"
alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
"""
# or if you don't like that, and want to do a function without inputs
"""
def cipher(raw_text, key):
    Do Some Shit Here

alphabet="abcdefghijklmnopqrstuvwxyz"
alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
new_text = ""

cipher("The thing I want to translate", 2)
"""










































# Hint 5-> Your main loop should look something like this 
  # for letter in raw_text:










































# Hint 6-> If you want the code to differentiate between upper and lowercase, use .upper() and .lower()      










































# Hint 7 -> My solution. Scroll further down to see it.









































"""
raw_text = input("Give me a Sentence: ")
new_text = ""
key = int(input("Give me an integer: "))
alphabet="abcdefghijklmnopqrstuvwxyz"
alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for letter in raw_text:
    if letter.islower():
        i = alphabet.find(letter)
        new_i = (i+ key)%26
        new_text += alphabet[new_i]
    elif letter.isupper():
        i = alphabet_upper.find(letter)
        new_i = (i+ key)%26
        new_text += alphabet_upper[new_i]
    else:
        new_text += letter
print(new_text)
"""

