import operator
import random

score = 0
good_answer = 0
bad_answer = 0
operators = [('+', operator.add), ('-', operator.sub), ('*', operator.mul)]
user_wants_more = True

def ask_for_more():
    print("do you want more ? y/n or yes/no")
    user_prompt_for_more = input()
    if user_prompt_for_more == "yes" or user_prompt_for_more == "y":
        user_wants_more = True        
    else:
        user_wants_more = False
    return user_wants_more
            

while user_wants_more:
    a = random.randint(1, 50)
    b = random.randint(1, 50)
    op, fn = random.choice(operators)
    prompt = "What is {} {} {}?\n".format(a, op, b)
    if int(input(prompt)) == fn(a, b):
        score += 1
        good_answer += 1
        print("You are correct")
        user_wants_more = ask_for_more()
    else:
        print("incorrect")
        bad_answer += 1
        user_wants_more = ask_for_more()

print("Score: {} good answer {} bad answer {} ".format(score,good_answer,bad_answer ))


