def front_x(words):
  for index in range(1,len(words)):
    value = words[index]
    i= index - 1
    while i >=0:
      if value > words[i]:
        words[i+1] = words[i]
        words[i] = value
        i -=1
      else:
        break
  return  words    
     
num_list = [5,3,55,43,1,8,100]
print(front_x(num_list))