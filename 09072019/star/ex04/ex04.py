quote = "some people drink from the fountain of knowledge, others just gargle."
VOWELS = ["a", "e", "i", "o", "u"]

whare_are_the_vowels = [i for (i, val) in enumerate(quote) if val in VOWELS]
print(whare_are_the_vowels)
