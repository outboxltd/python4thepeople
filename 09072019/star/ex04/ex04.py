quote = "some people drink from the fountain of knowledge, others just gargle."
VOWELS = ["a", "e", "i", "o", "u"]

whare_are_the_vowels = [i for (i, value) in enumerate(quote) if value in VOWELS]
print(whare_are_the_vowels)



