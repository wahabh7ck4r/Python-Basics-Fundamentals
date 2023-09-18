from num2words import num2words

user = int(input("Enter the number you want to convet in words: "))

words = num2words(user, lang='en')#we can also convert num into year like to='year'

print(words)