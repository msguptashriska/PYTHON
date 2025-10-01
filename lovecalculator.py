name1=input("Enter you name: \n")
name2=input("Enter your partner's name: \n")
bothnames=name1+name2
print(bothnames)
small=bothnames.lower()
t=small.count('t')
r=small.count('r')
u=small.count('u')
e=small.count('e')
true=t+r+u+e
l=small.count('l')
o=small.count('o')
v=small.count('v')
e=small.count('e')
love=l+o+v+e
lovescore=int(str(true)+str(love))

if lovescore<10 or lovescore>90:
  print("You are made for each other")
elif lovescore<=40 or lovescore>=50:
  print("You are very lucky to have your partner")
else:
  print("You are the Unique couple in the world")
