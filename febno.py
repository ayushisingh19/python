# febonaccai series means addtion to privious two no like first and sec ond value are given than next no is addtion of pribvious no  0,1 ,1,2,3,,5
# upto n terms 0,1,2,3,5,8,13,21,34
# upto n 0 ,1,1,2,5,8,

n=int(input("how many terms do you want to print"))
n1=0
n2=1
print(n1,n2,end="  ")
while n>2:
    n3=n1+n2
    print(n3,end=" ")
    n1,n2=n2,n3
    n=n-1
