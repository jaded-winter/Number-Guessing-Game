from os import system, name 
def clear(): 
    if name == 'nt': 
        _ = system('cls') 

A = int(input("Think of a number that your partner will try to guess: "))
clear()
i = int(input("Enter guess here: "))
j = 1
while i != A:
  j+=1
  if i < A:
      print("Number is too small")
  if i > A:
      print("Number is too big")
  i = int(input("Enter guess here: "))
if i == A :
  print("Correct!!" + " It took you " + str(j) + " guesses.")
  if j<=10:
    print("Nice job!")
  else:
    print("Lame...")
  
