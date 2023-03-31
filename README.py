a=5
data=[]
user=input()
dob=input()
roll=input()

while a!=0:
  data.append(input())
  a=a-1
alpha=[]
odd=[]
even=[]
for i in data:
  if i.isalpha():
     p=i.upper()
     alpha.append(p)
  else :
     k=int(i)
     if k%2==0:
        even.append(k)
     else:
        odd.append(k)
if len(dob)==6:
  print("is_success:"+" true")
else:
  print("is_success:"+" false")
print("user_id:",end='')
print(user,end='')
print("_",end='')
print(dob)
print("roll_number",end='')
print(roll)
print("odd_numbers:" ,end='')
print(odd)
print("even_numbers:",end='')
print(even)
print("alphabets:",end='')
print(alpha)
