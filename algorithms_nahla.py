#@*@*@*@
'''
for c in range (1,4): 
     print ("@*" , end=' ')
print("@")
'''
'''
for c in range (1,8): 
    if c % 2 == 0 : 
     print("*" , end=' ')
    else : print ("@" , end=' ')
'''
# odd numbers from 1 to n 
'''
c=0
n=int(input("Enter N : "))
for c in range (1, n+1 , 2) : 
    print(c)
'''
# sum of odd numbers from 1 to n
'''
c=0
sum=0
n=int(input("Enter N : ")) 
for c in range (1, n+1 , 2) : 
   sum=sum+ c 
print("sum = " ,sum )
'''
# summtion of first N odd numbers 
'''
c=0
sum=0
n=int(input("Enter N : ")) 
for c in range (1, n*2+1 , 2) : 
   sum=sum+ c 
print("sum = " ,sum )
'''
#summ of 1,2,3,4,5,......n 
'''
sum=0
n=int(input("Enter N : "))
for c in range (1 , n+1) :
    sum = sum+c 
print("the summtion from 1 to ", n, "is : ", sum )
'''
#n days convert C to F 
'''
n=int(input("Enter how many Days you have : "))
for b in range (1,n+1) : 
    F=float(input("Enter Degree in Fehrenheit : "))
    C= (5/9)*(F-32)
    print("celsius degree for " , F , "is : " , C )
'''
# 3 numbers and print the max valu between them 
'''
a=int(input("First Valu :"))
b=int(input("second Valu :"))
c=int(input("third Valu :"))
if a>= b and a>=c :
    print("The max value is :" , a )
else: 
    if b>= a and b>=c :
        print("The max value is :" , b )
    else: 
        print("The max value is :" , c)
'''

#1 1 * * * * 
#3 3 * * * 
#5 5 * *
#7 7 *
'''
x=7
c=-1
for i in range(4) :
    x=x-1 #became 6 ;  0 to 6 = 7 = cloms in the shap 
    c=c+2
    for j in range (x): 
        if j == 0 or j == 1 :
            print(c , end=' ')
        else : 
            print("*" , end=' ')
    print()
'''
# n of temps and print the avg between 0 to 5 
'''
c_temp=0
sum=0
n=int(input("Enetr how many temperture :"))
for c in range (1 , n+1) : 
    temp=int(input("Enetr temperture :"))
    if temp >= 0 and temp <= 5 :
        sum=sum+temp
        c_temp=c_temp+1
avg=sum/c_temp
print("avrage of temps between 0 to 5 is : " , avg )
'''
'''
max=0
n=int(input("Enter how many number do you have : "))
v=int(input("Enter value : "))
max=v 
for i in range (1, n) :
    v=int(input("Enter value : "))
    if v > max :
        max=v
print("The maxemim value is :" , max )
'''
# n numbers of mark and calculate : total avg , avg of +85 , num of pass (+50)
'''
sum=sumA=nofA=nofP=0 
n=int(input("enter how many student do you have : "))
for i in range (1,n+1): 
    mark=int(input("Enter the Mark : "))
    sum=sum+mark
    if mark >= 85 :
        sumA=sumA+1
        nofA=nofA+1
    if mark >= 50 : 
        nofP=nofP+1
totalavg= sum/n 
Aavg=sumA/nofA
print("The total avrage is : ", totalavg)
print("The avrafe of A student is :" , Aavg)
print("Number of student how are pass : ", nofP)
'''
# fact of n number 
'''
fact=1
n=int(input("enter the numbrer : "))
for i in range (1,n+1): 
    fact=fact*i 
print("fact of",n, "is : " ,fact )
'''
#y=2!*3!
'''
fact=1
y=0
for i in range (1,3): 
    fact=fact*i 
y=fact*(fact*3) 
print("fact is : " ,y )
'''
#y=4*x!+2d-(z!)^2
'''
factx=factz=1
x=int(input("Enter x : "))
z=int(input("Enter Z : "))
d=int(input("Enter D : "))
for i in range (1, x+1):
    factx=factx*i
for v in range (1, z+1):
    factz=factz*v
y=(4*factx)+(2*d)-(factz**2) 
print("y=" , y )
'''
#x=y
'''
z=0
x=int(input("Enter x : "))
y=int(input("Enter y : "))
z=x
x=y   
y=z
print("x is: " , x, end=' ')
print("y is : ",  y, end=' ')
'''
#@*@*@*@ with mod %
'''
for i in range (1,8): 
    if i %2 == 0 : 
        print("*" , end=' ')
    elif i %2 != 0 : 
        print("@" , end=' ')
'''
#A%AAA%
'''
for i in range (1,7): 
    if i ==2 or i== 6 :
        print("%" , end=' ')
    else :
        print("A", end=' ')
'''
'''
for i in range (1,7): 
    if i%2==0 and i!=4  :
        print("%" , end=' ')
    else :
        print("A", end=' ')
'''
#Y= 2! 3! + 3! 4!
'''
y=0 
for i in range (2,4) :
    fact=1
    for c in range (1,i+1):
        fact = fact * c 
    y=y+(fact*(fact*(i+1)))
print("The calculate Value : ", y)
'''
#@*@*@*@
#@*@*@*@
'''
l=1
while l <= 2 :
    for i in range (1,8): 
        if i %2 == 0 :
            print("*" , end=' ')
        else : 
            print("@" , end=' ')
    print()
    l=l+1
'''
#Y=2! * 3! + 3! 4! 
'''
y=0
n=1
for i in range(2):
    fact=1
    n=n+1
    for c in range(1,n+1):
        fact=fact*c
    y=y+(fact*(fact*(n+1)))
print("y=" , y)
'''
#y= 2! * 4! + 5! * 7!
'''
y=0
c=2
for v in range(1,3) : 
    fact=1
    for i in range(1,c+1) :
        fact=fact*i 
    y=y+(fact*(fact*(c+1)*(c+2)))
    c+=3
print("y=" , y )
'''
'''
y=0
c=2
while c <=5 :
    fact=1
    for i in range(1,c+1) :
        fact=fact*i 
    y=y+(fact*(fact*(c+1)*(c+2)))
    c+=3
print("y=" , y)
'''
#10 9 8 7 
#6  A 4 
#3  2
#1

""" v=10
for i in range(4,0,-1) :
    for c in range (1,i+1):
        if v == 5 :
            print("A " , end='')
        else : 
            print(v , end=' ')
        v-=1
    print()
 """


# n number of students in 3 subjects >> print the avg of each student in thoes 3 subjects 
'''
sum=0
nstd=int(input("enter how many std:"))
for s in range (1, nstd+1) :
    for i in range(1,4) : 
        m=int(input("Input mark :"))
        sum=sum+m
    avg=sum/3
    print("avg of",s , "is:",avg )
'''
#1 2 3 4 A 
#1 2 3 A 5 
#1 2 A 4 5 
#1 A 3 4 5
#A 2 3 5 5
'''
for i in range(1,6):
    for c in range(1 ,6) :
        if i+c==6 : 
            print("A", end='')
        else :
            print(c, end='')
    print()
'''
#A 
#1 A
#1 2 A 
#1 2 3 A
#1 2 3 5 A
""" for i in range(1,6):
    for c in range (1,i+1):
        if i==c :
            print("A " , end=' ')
        else :
            print(c, end=' ')
    print()
 """




# Print (-2 0 2 4 ) or N of lines 
'''
n=int(input("Enter Number of lines : "))
for c in range (1,n+1): 
    for j in range(-2,6,2):
        print(j , end=' ')
    print()
'''
# * 2 * 2 *
# 2 2 2 2 2
# * 2 * 2 *
# 2 2 2 2 2
# * 2 * 2 *
'''
for i in range (1 , 6) : 
    for c in range (1,6) : 
        if i%2 != 0 and c%2 != 0 : 
            print("* " , end=' ')
        else : 
            print("2" , end=' ')
    print()
'''
#y= ( 7X! / 3! ) + ( 5X! / 5! ) + ( 3X! / 7!)
""" 
y=0
factx=1
fact=1
x=int(input("Enter X = "))
for b in range(1,x+1):
    factx=factx * b 

for z in range (7,1,-2): 
    for i in range(3,9,2) :
        for c in range(1 ,i+1):
          fact=fact*c
        y=y+(z*factx)/fact
print("Y=",y)
 """
#5
#* 5
#* * 5
#* * * 5
'''
for i in range (1,5) : 
    for c in range (1,i+1) : 
        if i==c : 
            print("5 " ,end='')
        else : 
            print("* ",end='')
   
    print()
'''
#4444
#333
#22
#1
'''
for i in range(4,0,-1):
    for c in range(1,i+1):
        print(i,end=' ')
    print()
'''
    
'''
for r in range (4,0,-1):
    for c in range(1,r+1):
        if c==r :
            print(c , end=' ')
    print()
'''

#1 2 3 4 5!
#1 2 3 4! 5
#1 2 3! 4 5
#1 2! 3 4 5 
#1! 2 3 4 5 
'''
for i in range(1,6):
    for c in range(1,6): 
        if c+i==6 :
            fact=1
            for f in range(1,c+1):
                fact=fact*f
            print(fact,end=' ')
        else : 
            print(c, end=' ')
    print()
'''
#A 
#1 A
#1 2 A 
#1 2 3 A
#1 2 3 5 A
'''
for i in range(1,6):
    for c in range(1,i+1):
        if i==c :
            print("A" , end=' ')
        else : 
            print(c , end=' ' )
    print()
'''
#A         
#  A     
#    A
#       A
#         A
'''
for i in range(1,6):
    for c in range(1,i+1):
        if c==i :
            print("A" , end=' ')
        else : 
            print("  " , end=' ' )
    print()
'''
#         A
#       A
#    A
#  A     
#A         
'''
for i in range(1,6):
    for c in range(1,6):
        if c+i==6 :
            print("A" , end=' ')
        else : 
            print("  " , end=' ' )
    print()
'''
#A        A
#  A    A
#    N
#  A    A
#A        A
'''
for i in range(1,6):
    for c in range(1,6):
        if c!=3 and c==i :
            print("A" , end=' ')
        elif c!=3 and c+i==6 :
            print("A" , end=' ')
        elif c==3 and i==3 :
            print("N" ,  end=' ')
        else :
            print("  " , end=' ')
    print()
'''

#* * * * * 
#  *     *
#    *   *
#      * *
#        *
'''
for i in range(1,6):
    for c in range(1,6):
        if i == 1 :
            print("* " , end=' ')
        elif i==c :
            print("* " , end=' ')
        elif c == 5 :
            print("* " , end=' ')
        else: print("  ",end=' ')
    print()
'''
#        *
#      * *
#    *   *
#  *     *
#* * * * * 
'''
for i in range(1,6):
    for c in range(1,6):
        if i+c == 6 :
            print("* " , end=' ')
        elif c==5 :
            print("* ", end=' ')
        elif i==5 :
            print("* ", end=' ')
        else : print("  " , end=' ')
    print()
'''
# * 
# * * 
# *   *
# *     *
# * * * * *
""" for r in range (1,6):
    c=1
    while c <=r :
        if r==5 or c==1 or c==r : 
            print("*" , end=' ')
        else : 
            print(" " , end=' ')
        c=c+1
    print() """

#t! + x2 -5
'''
t=int(input("Enter t value : "))
fact=1
for i in range (1,t+1):
    fact=fact*i
x=int(input("Enter x value : "))
y=fact+(x*2) - 5 
print("y= " , y)
'''

#y= 2!3!4!+5!6!7!+8!9!10!

""" 
y=0
for i in range (2,9,+3):
    fact=1 
    for c in range (1,i+1):
        fact=fact*c
    y=y+(fact*(fact*(i+1))*(fact*(i+1)*(i+2)))
print("y=" , y) 
"""

#5!/2! + 3!/3! + 1!/4!

""" y=0
v=2
for i in range (5,0,-2):
    facti=1
    for c in range (1,i+1):
        facti=facti*c
    #print("fact m8am" , facti)
    factv=1
    for b in range (1,v+1):
        factv=factv*b
    #print("fact v " , factv)
    y=y+(facti/factv)
    v+=1
print("y=" , y ) """

'''    
s=0
m=2
g=5
for d in range (5,0,-2):
    fact1=1
    for j in range (1,g+1):
        fact1*=j
    fact2=1
    for h in range(1,m+1):
        fact2*=h
    s=s+(fact1/fact2)
    m+=1
    g-=2
print("y=",s)
'''
#* * * * *
# * * * *
#  * * *
#   * *
#    *
#   * *
#  * * * 
# * * * *
#* * * * *

""" s=0
st=5
for l in range (1,5):
    for C in range (s,0,-1) :
        print(" " , end='')
    for x in range (st,0,-1):
        print("*" , end=' ')
    s+=1
    st-=1
    print()

sp=4
star=1
for i in range (1,6):
    for v in range(1,sp+1):
        print(" " , end='')
    for c in range (1,star+1):
        print("*" , end=' ')
    print()
    sp-=1
    star+=1  """

#    *
#   * *
#  * * * 
# * * * *
#* * * * *
#   | |
#   | |
'''
space=4
star=1 
for  i in range (1,6):
    print(" "*space , "* "*star )
    star+=1
    space-=1

space=3
for v in range (1,3):
    print(" "*space ,  "| |") 
'''
""" 
o=1
m=5
y=0
while o < 4 :
    fact=1
    for i in range (1,m+1):
        fact*=i
    y=y+((fact*(m*1)/fact))
    o+=1
    m-=2
print(y) 
"""
""" number=[1,2,3,4,5,6,7]
result = []
for i in number:
    result.append(i*i)
print(number)
print(result) """
""" n=int(input("ENTER N :"))
salary=[n]
salary[0]= float(input("salary :"))
min=salary[0]
for i in range(1,n):
    salary.insert(i, float(input("salary :")))
    if salary[i] < min :
        min=salary[i]
print(min) """

""" n=int(input("ENTER N :"))
salary=[n]
minsalary=[n]
salary[0]= float(input("salary :"))
min=salary[0]
minsalary=[salary[0]]
for i in range(1,n):
    s=float(input("salary :"))
    salary.insert(i,s)
    if salary[i] < min :
        min=salary[i]
    minsalary.append(s)
print(min)
print(minsalary)
     """

""" name=[]
mark=[]
sum=max=0
for i in range (10):
    name.insert(i, str(input("name :")))
    mark.insert(i, int(input("Mark :")))
    sum=sum+ mark[i]
    if mark[i] > max :
        max=mark[i]
for i in range(10):
    print(name[i], mark[i])
print(max)
print(sum/10) """

""" sum=n=c=0
model=[10]
price=[10]
number=[10]
for i in range (0,10):
    model.insert(i, str(input("Model :")))
    price.insert(i, float(input("Price :")))
    number.insert(i, int(input("Number :")))
for i in range (0,10):
    if price[i] >= 50000 :
        print("car model" ,model[i] ,  "car number" ,number[i])
    if price[i] >= 25000 :
        n=n+1
    if price[i] < 10000 :
        sum=sum+price[i]
        c=c+1 
print(n)
print(sum/c) """
""" 
n=int(input("enter size :"))
list = [n]
for i in range(n):
    list.append(int(input("Enter n")))
sum=c=0
for i in range(n):
    if list[i] %2 == 0 :
        sum=sum+list[i]
        c+=1
print("sum of even values : " , sum )
print("number of even value : " , c) """
#* * *
#* * * *
#* * *
#* * * *
#* * *
""" r=1
p=3
while r <=5 :
    if r %2 == 0 :
        p=4
        v=1
        while v <= p:
            print("*" , end=' ')
            v+=1
    else:
        p=2
        c=1 
        while c <=p : 
            print("*" , end=' ')
            c+=1
    print()
    r+=1 """
#while: 
#y= ( 7X! / 3! ) + ( 5X! / 5! ) + ( 3X! / 7!)
""" y=0
x=int(input("enter X :"))
cx=1
fx=1
while cx<= x:
    fx=fx*cx
    cx+=1
p=7
i=3
while p >=3  :
    fi=1
    ci=1
    while ci<=i :
        fi=fi*ci 
        ci+=1
    y=y+((p*fx)/fi)
    i+=2
    p-=2
print(y)
 """
# * 2 * 2 *
# 2 2 2 2 2
# * 2 * 2 *
# 2 2 2 2 2
# * 2 * 2 *
""" r=5
while r >=1 :
    c=1
    while c<=5:
        if r%2==1 and c%2==1 :
            print("*" , end=' ')
        else : print("2", end=' ')
        c+=1
    print()
    r-=1 """
    #10 9 8 7 
#6  A 4 
#3  2
#1
""" r=4 
v=10
while r > 0 : 
    c=1
    while c <=r :
        if v == 5 : 
            print("A" , end=' ')
        else :
            print(v , end=' ')
        c+=1
        v-=1
    print()
    r-=1 """

#1 2 3 4 A 
#1 2 3 A 5 
#1 2 A 4 5 
#1 A 3 4 5
#A 2 3 5 5
""" r=1
while r <= 5 :
    c=1 
    while c <=5 :
        if c+r==6 : 
            print("A" , end=' ')
        else:
            print(c , end=' ')
        c+=1
    print()
    r+=1 """
#A 
#1 A
#1 2 A 
#1 2 3 A
#1 2 3 4 A
""" r=1
while r <= 5 : 
    c=1 
    while c <= r :
        if c==r : 
            print("A", end=' ')
        else: print(c,end=' ')
        c+=1
    print()
    r+=1 """
#y=2!3!
""" def fact(v):
    Fact=1
    for i in range(1,v+1):
        Fact=Fact*i
    return Fact
y=(fact(2)*fact(3))
print(y) """
#y=6!/5! + 4!/3! + 2!/1!
""" def fact(x):
    f=1
    for i in range (1,x+1):
        f*=i
    return f 
y=(fact(6)/fact(5))+(fact(4)/fact(3))+(fact(2)/fact(1))
print(y) """
#y=X! (1!/s^2) + X!^2 (2!/s^3) + X!^3 (3!/s^4)
""" x=int(input("enter X"))
s=int(input("enter s"))
def fact(v):
    f=1
    for i in range(1,v+1):
        f*=i
    return f 
y=(fact(x)*(fact(1)/(s**2)))+((fact(x)**2)*(fact(2)/(s**3)))+((fact(x)**3)*(fact(3)/(s**4)))
print(y)
 """
#777#777#
#555#555#
#333#333#
""" for i in range (7,2,-2):
    for c in range (1,9):
        if c==4 or c==8 :
            print("#" , end=' ')
        else:
            print(i , end=' ')
    print() """
#1234567
# 234567
#  34567
#   4567
#    567
#     67
#      7
#     67
#    567
#   4567
#  34567
# 234567
#1234567
""" p=0
v=1
for i in range(1,8):
    for s in range (p,i):
        print("  "*s , end=' ')
    p+=1
    for c in range (v,8):
        print(c,end=' ')
    v+=1
    print()
p=5
v=6
for x in range(6,0,-1):
    for s in range (p,x+1):
        print(" "*s , end='')
    p-=1
    for c in range (v,8):
        print(c,end=' ')
    v-=1
    print() """
#1
#21
#321
#4321
#54321
#4321
#321
#21
#1
'''
""" for i in range (1,6):
    for c in range (i,0,-1):
        print(c,end='')
    print()
for x in range (4,0,-1):
    for c in range (x,0,-1):
        print(c,end='')
    print() """
'''
#square  with dimenion given user 
""" 
x=int(input("Enter x : "))
c=1
while c <= x : 
    s=1
    while s <= x :
        print("*" , end=' ')
        s+=1
    c+=1
    print() 

#useing FOR loop :
for i in range (x):
    for c in range (x) :
        print ("*" , end='')
    print()
"""

""" z=int(input("Enter s : "))
x=int(input("Enter x : "))
v=input("Enter What you need inside the shape :")
c=1
while c <= x : 
    s=1
    while s <= z :
        print(v , end=' ')
        s+=1
    c+=1
    print() """
# * * * * 
# *     *
# *     *
# * * * *
""" s=5
for i in range (1,5):
    for c in range (1,5):
        if i==1 or i==4 or c==1 or c==4:
            print("*" , end =" ")
        else : 
            print(" " , end =" ")
    print() """
# 1
# 21   
# 321  
# 4321 
# 54321
# 4321 
# 321  
# 21   
# 1    
""" for i in range(1,5):
    for c in range(1,i+1):
        print(c , end=' ')
    print()
for i in range (5,0,-1):
    for c in range(i,0,-1):
        print(c , end=' ')
    print()
 """
'''
"""  *
    ***
   *****
  *******
 *********

  *******
   *****
    ***
     * """

""" sp=5
st=1
for r in range (1,6):
    for p in range(1,sp+1):
        print(" " , end='')
    for s in range(1,st+1):
        print("*", end=' ')
    st+=1
    sp-=1
    print() 
st=6
s=0
for i in range(7,0,-1):
    for s in range(1,s+1):
        print(" ", end='')
    for c in range(1,st+1):
        print("*", end=' ')
    s+=1
    st-=1
    print()
 """
""" x=int(input("enter x :"))
r=1
while r<=x:
    c=1
    while c<=x:
        print("*" , end='')
        c+=1
    print()
    r+=1 """
# Z=   4 (2!/a^2)  +  (3!/ a^3)  +  3 (4!/a^4)   +  (5!/ a^5)
""" w=4
o=2
y=0
a=int(input("Enter A :"))
for p in range(2,6):
        fact=1
        for i in range (1,p+1):
            fact*=i 
        if p%2==0 :
            y=y+(w*(fact/a**o))
            w-=1
        else :
            y=y+((fact/a**o))

        o+=1
print(y) """
# 1 
# 2 2 
# 3 3 3
# # # # #
# 5 5 5 5 5
""" w=1
for i in range (1,6):
    for c in range (1, i+1):
        if i==4 :
            print ("#", end =" ")
        else :
            print (w , end =" ")
    print ()    
    w=w+1
 """
#************
#***** ******
#****   *****
#**        **
#*          *
#************
""" stars=6
spaces=0
for i in range (6):
    star="*"
    space=" "
    print(star*stars , end='')
    print(space*spaces , end='')
    spaces+=2
    print(star*stars,end='')
    stars-=1
    print()
    if i>=5:
        print(star*12) """
#k= 3!2! + 4!5!+ 5!6! + 4*h 
""" y=0
h=int(input("Enter h: "))
for i in range (3,6):
    fact=1
    for c in range (1,i+1):
        fact*=c 
    #print(fact)
    y=y+(fact*(fact/i))
y=y+(4*h)
print(y)
 """
#2%22%2
#1%11%1
#0%00%0
#-1%-1-1%-1
#-2%-2-2%-2
""" for r in range (2,-3,-1):
    for c in range (1,7):
        if c==2 or c==5 :
            print("%", end='')
        else:
            print(r , end='')
    print()
 """
#7 6 3 0 -3
#7 6 3 0 -3
#7 6 3 0 -3
#7 6 3 0 -3
""" for i in range (1,5):
    v=6
    for c in range(1,6):
        if c==1 :
            print("7" , end='')
        else: 
            print(v , end='')
            v=v-3
    print()
 """
""" r=1
while r<= 4 :
    c=1
    v=6
    while c <= 5:
        if c==1:
            print("7",end='')
        else:
            print(v,end='')
            v-=3
        c+=1
    r+=1
    print() """
#y=(2f! +4f!+6f!)/3 -4f^2
""" y=0
v=int(input("Enter F:"))
for c in range(2,7,2):
    fact=1

    for i in range (1,v+1):
        fact*=i
    y=y+(c*fact)
y=(y/3)- (4*(v**2))
print(y) """
""" csum=tsum=c=coc=co60=0
Mark=[]
n=int(input("Enter No.student :"))
for i in range (n):
    Mark.append(float(input("Enter your Mark :")))
for i in Mark :

    tsum+=i
    c+=1

    if i >=65 and i <=74 :
        csum=csum+i 
        coc+=1

    if i > 60 :
        co60+=1 

tavg=tsum/n
cavg=csum/coc
print("total avg :" ,tavg ) 
print("C avg:", cavg )
print("More than 60:" , co60) """
#^2 of list of numbers
""" 
def pow(x):
    d=x**2
    return d
n=int(input("Enter how many numbers do you have :"))
number=[]
result=[]
for i in range(n):
    number.append(int(input("Enter Val:")))
for i in number:
    result.append(pow(i))
print(result)
 """
#create two arrays for names and marks then calculate average of 10 marks
#find maximum mark, and print the elements of the two arrays.
""" sum=max=0
Mark=[]
name=[]
for i in range (5):
    Mark.append(int(input("Enter your mark:")))
    name.append(str(input("ENter name :")))
for i in  Mark: 
    sum=sum+i
    if i > max:
        max=i 
for i in range (5):
    print(name[i] , Mark[i])
avg=sum/5
print("avg:" , avg )
print("maximum mark is :" , max) """

#Write a program that receive number of salary and print the minimum
""" min=0
n=int(input("Enetr Number of salaries :"))
salary=[n]
salary[0]: int(input("enter Salary :"))
min=salary[0]
for i in range (1,n):
    salary.insert(i, int(input("enter Salary :")))
    if salary[i]<min :
        min=salary[i]
print("the minimum is :" , min)
 """
""" min=0
n=int(input("Enetr Number of salaries :"))
salary=[]
for i in range (n):
    if i ==0 :
        salary.insert(i, int(input("enter Salary :")))
        min=salary[i]
    salary.insert(i, int(input("enter Salary :")))
    if salary[i]<min :
        min=salary[i]
print("the minimum is :" , min) """

#write a program receive 5 numbers and print the sum of even numbers 
""" sum=0
number=[]
for i in range (5):
    number.append(int(input("enter number :")))
for i in number :
    if i %2 == 0 :
        sum=sum+i
print("summiton of even numbers is :" , sum)
 """
#receive mobile phone number snd print the number of libyana , madar , home
""" libyana=madar=home=0
n=int(input("Enetr Number of phones :"))
number=[]
for i in range (n):
    number.insert(i,str(input("enter phone number :")))
    j=number[i]
    k=j[0:3]
    if k == "091" :
        madar+=1
    elif k == "092" : 
        libyana+=1
    elif k == "061" :
        home+=1
    else :
        print("Error , undefined number")
print("Number of Libyana Line users is :" , libyana)
print("Number of AL-Madar Line users is :" , madar)
print("Number of Home users is :" , home) """

#write a program that receive n numbers of salaries and print :
#1 total avg 
#2 salaries that less than 500 LD 
""" #3 maxmuim and minmuim salary 
sum=max=min=c50=0
n=int(input("Enetr Number of salaries do you have:"))
sal=[]
for i in range (n) :
    sal.append(int(input("Enetr Salary :")))
    if i == 0  :
        min=sal[i]
        max=sal[i]
for i in sal :
    sum=sum+i

    if i < 500 :
        c50+=1
    if i > max : max=i

    if i < min : min=i
avg=sum/n
print("total avg is :" , avg)
print("Number of salary less than 500 :" , c50)
print(" max salary :" ,  max , "Min salary :" ,  min) """

# receives the salaries of a number of employees and stores them in a list
#and then print the number of salaries above 1000
""" c1000=0
n=int(input("Enetr Number of salaries do you have:"))
sal=[]
for i in range (n):
    sal.insert(i, int(input("Enetr salary:")))

for i in sal :
    if i >=1000 : 
        c1000+=1
print(sal)
print("salaries above 1000 : " , c1000) """
#4 functions to print summation, avg , multiplication و subtraction for 2 values
""" def sum (x,y):
    h=x+y
    return h 
def mul (x,y):
    h=x*y
    return h
def avg (x,y):
    h=x+y
    return h/2
def sub (y,x):
    h=x-y
    return h
print(sum(5, 10))
print(sub(5, 10))
print(mul(5, 10))
print(avg(5, 10)) """

""" def shape (x,y,z):
    for i in range(1,x+1):
        if i == y : 
            print(z, end='')
        else: print("*" , end='')
    print()
x=int(input("Width :"))
y=int(input("Lenght :"))
c=int(input("Enter Execludion :"))
z=str(input("Enter Sign :"))
for i in range (y):
    a=shape(x, c, z) """
# -2 0 2 4 
""" def shape (x , y , z , r):
    for i in range (1,r+1):
        for c in range (x , y+1 , z):
            print(c , end=' ')
        print()
x=int(input("First Number  :"))
y=int(input("Last Number  :"))
z=int(input("change amount :"))
r=int(input("how many rows :"))
print(shape(x, y, z, r)) """
# print the name of student how has the basr Mark (useing list)
""" best=0
index=0
n=int(input("Enter Number of student : "))
mark=[]
name=[]
for i in range (n) :
    mark.append(float(input("Enter Mark:")))
    name.append(str(input("Enter Name :")))
    if i == 0 :
        best = mark[i]
for i in range(n):
    if mark[i] > best :
        i = index
        best=mark[i]
print( "Best One is :" , name[index])
 """
#Draw the following shape using both (while) & (for) loops
"""
7630-3
7630-3
7630-3
7630-3
"""

"""
i=1
while i <=4:
    n=6
    for j in range (1,6):
        if j==1: print("7" , end="")
        else:
            print(n , end="")
            n-=3
    print()
    i+=1
"""

#k=(2f!+4f!+6f!)/3 - 4f^2
#Solve K (When F is a User Input)
""" k=0
f=int(input("Enter F:"))
for i in range (2,7,2):
    fact=1
    for c in range (1,f+1):
        fact*=c
    k=k+(i*fact)
k=k/3 - ((4*(f**2)))
print(k) """

#5 43 43 43 43
#5 43 43 43 43
#5 43 43 43 43
""" r=1
while r <= 3:
    for c in range (1,6):
        if c ==1 :
            print("5" , end='')
        else :
            print("43" , end='')
    print()
    r+=1 """

#k=(-2 -5 -8 -11)^2-121
""" k=0
for i in range(2,12,+3):
    k=k+(-i)
k=(k**2)-121
print("K= " , k) """
'''
#4444BKKKK
#4444BKKKK
#4444BKKKK
#4444BKKKK
""" for r in range (1,5):
    c=1
    while c <= 9 :
        if c == 5 :
            print ("B",end=" ")
        elif c > 5 :
            print ("K",end=" ")
        else :
            print ("4",end=" ")
        c=c+1
    print () """
#k=2t!c!+3t!c!+4t!c! - 2t
""" def f(x):
    fact = 1
    for i in range (1,x+1):
        fact = fact * i
    return fact
k = 0
t = int (input ("enter t:"))
c = int (input ("enter c:"))
k = (2*f(t)*f(c)) + (3*f(t)*f(c)) + (4*f(t)*f(c)) - 2 * t 
print (k)
 """
#y=X! (1!/s^2) + X!^2 (2!/s^3) + X!^3 (3!/s^4)
""" x=int(input("enter X"))
s=int(input("enter s"))
def fact(v):
    f=1
    for i in range(1,v+1):
        f*=i
    return f 
y=(fact(x)*(fact(1)/(s**2)))+((fact(x)**2)*(fact(2)/(s**3)))+((fact(x)**3)*(fact(3)/(s**4)))
print(y)
 """
#777#777#
#555#555#
#333#333#
""" for i in range (7,2,-2):
    for c in range (1,9):
        if c==4 or c==8 :
            print("#" , end=' ')
        else:
            print(i , end=' ')
    print() """

#FINAL EXAM :

#A******A
#A*****A
#A****A
""" r=8
while r >= 6 : 
    for c in range (1,r+1):
        if c==1 :
            print("A" ,  end=' ')
        if c == r : 
            print("A" ,  end=' ')
        else : 
            print("*" , end=' ')
    r-=1
    print() """
#3 lists Mark , Pass student , Filed for 10 students .. print the listes and number of Pass and Fild student
""" cp=cf=0
mark=[]
p=[]
f=[]
for i in range (10):
    mark.append(int(input("enter mark  :")))
for i in mark :
    if i < 50 :
        f.append(i)
        cf+=1
    if i >=50 :
        p.append(i)
        cp+=1
print("number of P student :",cp)
print("number of F student :",cf)
print(mark)
print(p)
print(f) """
#L= -2(X!/Y!) + (X!/Y!)^2 + 4(X!/Y!)^3 - XY USING LOOP AND DEF 
""" def fact(x):
    f=1
    for i in range (1,x+1):
        f=f*i
    return f 
L=0
m=-2
x=int(input("X = "))
y=int(input("Y = "))
for i in range (1,4):
    L=L+(m*(fact(x)/fact(y)**i))
    m=m+3
L=L-(x*y)
print(L) """