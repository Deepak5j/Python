print("Hello world".capitalize())  # Capitalizes the first letter of the string
print("HELLO".casefold())  # Converts string into lower case
print("helxyxlo".center(10, "-"))  # Centers the string with a specified width and padding
print("Hello world".count("o"))  # Counts occurrences of "o" in the string
print("hello".encode())  # Encodes the string to bytes
print("hello".endswith("lo"))  # Checks if the string ends with "lo"
print("hello\tworld".expandtabs(4))  # Expands tabs to 4 spaces
print("Hello world".find("world"))  # Finds the position of "world"
print("My name is {}".format("John"))  # Formats a string with specified value
print("My name is {name}".format_map({"name": "John"}))  # Formats using a mapping
print("Hello world".index("world"))  # Finds the position of "world"
print("hello123".isalnum())  # Checks if the string is alphanumeric
print("hello".isalpha())  # Checks if the string contains only alphabet characters
print("hello".isascii())  # Checks if the string contains only ASCII characters
print("123".isdecimal())  # Checks if all characters are decimal
print("12345".isdigit())  # Checks if all characters are digits
print("variable_name".isidentifier())  # Checks if the string is a valid identifier
print("hello".islower())  # Checks if all characters are lowercase
print("12345".isnumeric())  # Checks if all characters are numeric
print("Hello world".isprintable())  # Checks if the string is printable
print("     ".isspace())  # Checks if the string contains only whitespace characters
print("Hello World".istitle())  # Checks if the string follows title case rules
print("HELLO".isupper())  # Checks if all characters are uppercase
print("-".join(["a", "b", "c"]))  # Joins elements of a list with "-"
print("hello".ljust(10, "-"))  # Left justifies the string with padding
print("HELLO".lower())  # Converts string to lowercase
print("   hello".lstrip())  # Removes leading spaces
print("abc".maketrans("abc", "123"))  # Creates a translation table
print("Hello world".partition(" "))  # Splits the string into three parts
print("Hello world".replace("world", "there"))  # Replaces "world" with "there"
print("Hello world".rfind("o"))  # Finds the last occurrence of "o"
print("Hello world".rindex("o"))  # Finds the last occurrence of "o" and returns its index
print("Hello".rjust(10, "-"))  # Right justifies the string with padding
print("Hello world".rpartition(" "))  # Splits the string into three parts from the right
print("a,b,c".rsplit(",", 1))  # Splits the string from the right, limit to 1 split
print("   hello".rstrip())  # Removes trailing spaces
print("Hello world".split())  # Splits the string by whitespace
print("hello\nworld".splitlines())  # Splits the string at line breaks
print("hello world".startswith("hello"))  # Checks if the string starts with "hello"
print("   hello   ".strip())  # Removes leading and trailing spaces
print("Hello World".swapcase())  # Swaps the case of each letter
print("hello world".title())  # Converts the first letter of each word to uppercase
print("hello".translate(str.maketrans("aeiou", "12345")))  # Translates characters based on a translation table
print("hello".upper())  # Converts string to uppercase
print("42".zfill(5))  # Fills the string with 0s to a width of 5
