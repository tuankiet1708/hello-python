# Basic String Operations
# Strings are bits of text. They can be defined as anything between quotes:
astring = "Hello world!"
astring2 = 'Hello world!'

# As you can see, the first thing you learned was printing a simple sentence. This sentence was stored by Python as a string. However, instead of immediately printing strings out, we will explore the various things you can do to them. You can also use single quotes to assign a string. However, you will face problems if the value to be assigned itself contains single quotes.For example to assign the string in these bracket(single quotes are ' ') you need to use double quotes only like this
astring = "Hello world!"
print("single quotes are ' '")

# This prints out 12, because "Hello world!" is 12 characters long, including punctuation and spaces.
print(len(astring))

# This prints out 4, because the location of the first occurrence of the letter "o" is 4 characters away from the first character. Notice how there are actually two o's in the phrase - this method only recognizes the first.

# But why didn't it print out 5? Isn't "o" the fifth character in the string? To make things more simple, Python (and most other programming languages) start things at 0 instead of 1. So the index of "o" is 4.
# astring = "Hello world!"
print(astring.index("o"))

# For those of you using silly fonts, that is a lowercase L, not a number one. This counts the number of l's in the string. Therefore, it should print 3.
astring = "Hello world!"
print(astring.count("l"))

# This prints a slice of the string, starting at index 3, and ending at index 6. But why 6 and not 7? Again, most programming languages do this - it makes doing math inside those brackets easier.
astring = "Hello world!"
print(astring[3:7])

# If you just have one number in the brackets, it will give you the single character at that index. If you leave out the first number but keep the colon, it will give you a slice from the start to the number you left in. If you leave out the second number, it will give you a slice from the first number to the end.

# You can even put negative numbers inside the brackets. They are an easy way of starting at the end of the string instead of the beginning. This way, -3 means "3rd character from the end".
print(astring[3])
print(astring[:7])
print(astring[3:])
print(astring[-4])
print(astring[:-4])

# This prints the characters of string from 3 to 7 skipping one character. This is extended slice syntax. The general form is [start:stop:step].
astring = "Hello world!"
print(astring[3:7:2])

# both of them produce same output
astring = "Hello world!"
print(astring[3:7])
print(astring[3:7:1])

# There is no function like strrev in C to reverse a string. But with the above mentioned type of slice syntax you can easily reverse a string like this
astring = "Hello world!"
print(astring[::-1])

# These make a new string with all letters converted to uppercase and lowercase, respectively.
astring = "Hello world!"
print(astring.upper())
print(astring.lower())

# This is used to determine whether the string starts with something or ends with something, respectively. The first one will print True, as the string starts with "Hello". The second one will print False, as the string certainly does not end with "asdfasdfasdf".
astring = "Hello world!"
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))

# This splits the string into a bunch of strings grouped together in a list. Since this example splits at a space, the first item in the list will be "Hello", and the second will be "world!".
astring = "Hello world!"
words = astring.split(" ")
print(words)