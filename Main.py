class stackADT:

  def __init__(self,s) :
      self.size = s
      self.l = [None] * s
      self.top = -1

  def isFull(self) :
   if self.top == (self.size - 1) :
     return 1
   else :
     return 0

  def isEmpty(self) :
    if self.top == -1 :
     return 1
    else :
     return 0

  def push(self,y):
      if self.isFull()==1:
          print("The stack is full")
          return "Push is not filled"
      else:
          self.top = self.top+1
          self.l[self.top]=y

  def pop(self):
      if self.isEmpty()==1:
          return "the stack overflow"
      else:
          print(self.l[self.top])
          self.top = self.top-1
          return "elemnt pop removed"

  def peek(self):
      if self.top ==-1:
          return "THe stack is empty"
      else:
          return self.l[self.top]
  def display(self):
      for x in range(self.top+1):
          print(self.l[x])

size = int(input("Enter the size of the stack:"))

st1 = stackADT(size)

while(1):

  ch = int(input("1. Push 2. Pop 3. Peek 4. Display 5. Exit"))

  if ch == 1 :

    a = int(input("Enter the value to push :"))
    st1.push(a)

  elif ch == 2 :
    print(st1.pop())

  elif ch == 3 :
    print (st1.peek())

  elif ch == 4 :
    st1.display()

  elif ch == 5:
     break

  else :
     print("Invalid Input")
