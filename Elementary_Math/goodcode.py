import operator
import random

score = 0
operators = [('+', operator.add), ('-', operator.sub), ('*', operator.mul)]
user_wants_more = True

while user_wants_more:
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    op, fn = random.choice(operators)
    prompt = "What is {} {} {}?\n".format(a, op, b)
    if int(input(prompt)) == fn(a, b):
        score += 1
        print("You are correct, more ???")
        more = input()
        if more == "yes":
            user_wants_more = True
        else:
            user_wants_more = False
    else:
        print("incorrect")

print("Score: {}".format(score))
