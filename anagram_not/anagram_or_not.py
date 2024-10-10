# Prompt the user to enter the first string
string1 = input("Enter First String: ")

# Prompt the user to enter the second string
string2 = input("Enter Second String: ")

# Check if the sorted characters of both strings are equal
if sorted(string1) == sorted(string2):
    # If they are equal, print that the strings are anagrams
    print(f"The Strings '{string1.upper()}' and '{string2.upper()}' are Anagrams")
else:
    # If they are not equal, print that the strings are not anagrams
    print(f"The Strings '{string1.upper()}' and '{string2.upper()}' are Not Anagrams")




# Enter First String: silent
# Enter Second String: listen
# The Strings 'SILENT' and 'LISTEN' are Anagrams

# Enter First String: are
# Enter Second String: ore
# The Strings 'ARE' and 'ORE' are Not Anagrams

# Enter First String: flow
# Enter Second String: wolf
# The Strings 'FLOW' and 'WOLF' are Anagrams