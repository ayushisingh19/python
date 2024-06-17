n=int(input("enter the range:"))
sum=0
even=0
odd=0
while n>0:
   num=int(input("enter the number:"))
   print(num)
   if num%2==0:
      even=even+num
   else:
      odd=odd+num
   n=n-1
print("even:",even)
print("odd:",odd)

    