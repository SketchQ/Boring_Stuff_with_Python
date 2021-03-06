#English to Pig Latin
print("Enter the English message to translate into Pig Latin")
message = input()

VOWELS = ('a','e','i','o','u','y')

pigLatin = [] # A list of the words in Pig Latin.

for word in message.split():
    #Seperate the non-letters at the start of this world:
    prefixNonLetters = ""
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]
    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue

#Seperate the non-letters at the end of this word:

    suffixNonLetters = ""
    while not word[-1].isalpha():
        suffixNonLetters += word[-1]
        word = word[:-1]

# Remember if the word was in uppercase or title case.
    wasUpper = word.isupper()
    wasTittle = word.istitle()

    word = word.lower() # make theword lowercase for translation.

#Seperate the consonants at the start of this word:
    prefixConsonants =''
    while len(word)>0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]

# Add the Pig Latin ending to the word:
    if prefixConsonants != '':
        word += prefixConsonants+"ay"
    else:
        word +='yay'

# Set the word back to uppercase or tittle case:
    if wasUpper:
        word = word.upper()
    if wasTittle:
        word = word.title()

# Add the non-letters back to the start or end of the word.
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)

# Join all the words back togethe into a single string:
print(' '.join(pigLatin))
    