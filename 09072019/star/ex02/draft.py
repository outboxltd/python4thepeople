# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.

num_list = [5,3,55,43,1,8,100]


def front_x(l):
  for i in range(len(l)):
    for j in range(i + 1, len(l)): 
        if l[i] > l[j]:
         l[i], l[j] = l[j], l[i]
     

print(front_x(num_list))

