max=int(input("Enter the max:"))
top=''
def push(s):
  global top,t
  if len(s)>= max:
    print("Overflow")
  else:
    e=input("Enter docid:")
    n=input("Enter name:")
    dep=input("Enter dept:")
    s.append([e,n,dep])
    top=s[-1]
    print('Stack:',s,'\nTop:',top)
def pop(s):
  if len(s)==0:
    print('Underflow')
  else:
    a=s.pop()
    top=s[-1]
    print('Stack:',s,'\nTop:',top,'\nPopped element:',a)
def dis(s):
  for i in range(len(s)-1,-1,-1):
    print(s[i])
s=[]
while True:
  print('''1.	Push
  2.	Pop
  3.	Display entire stack content.
  4.	Exit
  ''')
  ch=int(input("Enter the choice:"))
  if ch==1:
    push(s)
  elif ch==2:
    pop(s)
  elif ch==3:
    dis(s)
  elif ch==4:
    print("Exiting....")
    break
  else:
    print("Invalid Option")
