""" m = [80 ,96 , 35 , 20 , 100]
n = []
f = []
for i in m :
    if i < 95 and i+5 >= 50 :
        n.append(i+5)
    elif i < 50 :
        n.append(i)
        f.append(i)
    else :
        a=100-i
        n.append(i+a)

print(n)
print(f) """

# 2 defs >> 1st resive list input user  and clc avg >> 2nd resive list input user  and clc sum

'''def avg_list(list1):
    sum = 0
    for x in list1:
        sum += x
    return sum/len(list1)

def avg_lit(list1):
    return sum(list1)/len(list1)


def sum_list(list1):
    sum = 0
    for x in list1:
        sum += x
    return sum


number = int(input("Enter how many number in the list  :"))
list1 = []
for i in range(number):
    user = int(input(f"Enter item Number {i+1}  :"))
    list1.append(user)

a = sum_list(list1)
b = avg_list(list1)
print(f"the avg of the list is {b} ,  and the sum is {a}")'''
# [4,5,7,9,1,13,-5]
# [5,1,13]
'''def subb(list1):
    N=0
    for i in range (len(list1)) :
        if i == 0 :
            continue
        elif i == len(list1) - 1 :
            N= N - list1[i]
            break
        else :
            N = N + (list1[i] - list1[i+1])
    return N'''

"""def sub_sequence(sublist, mainlist):
    Sndx=0
    Mndx=0
    while Sndx < len(sublist) and Mndx < len(mainlist):
        if sublist[Sndx] == mainlist[Mndx]:
            Sndx=Sndx+1
            Mndx = Mndx+1
        else :
            mainlist.remove(mainlist)
    print(mainlist)"""

"""
def sub_sequence(sublist, mainlist):
    Sindex = 0
    Mindex = 0
    turelist=[]
    while Sindex < len(sublist) and Mindex < len(mainlist):
        if sublist[Sindex] == mainlist[Mindex]:
            Sindex += 1
            turelist.append(mainlist[Mindex])
        Mindex += 1
    return turelist == sublist
#Main Program 
main = [ 4,5,7,9,1 , 13 , -5 ] 
sub = [4,13 , 5] 
print(sub_sequence(sub, main))"""

# "test.txt" ---> "testV5.txt"  "5"-->userinput
'''def filename(filename,version):
    newfilename = ""
    for i in filename:
        if (i) == "." :
            newfilename = newfilename + "V" + str(version)+(i)
        else:
            newfilename=newfilename+(i)
    return newfilename


z=filename("nahla.limu" , 3675)
print(z)'''
'''
def filename(filename,version):
    ndxofdote=filename.index(".")
    newfilename=filename[:ndxofdote]
    ext=filename[ndxofdote+1:]
    newfilename=newfilename+str(version)+"."+ext
    return newfilename
z=filename("text.txt" , 5)
print(z)'''
"""
def Word(word):
    for i in range(len(word)) :
        if word[i] == " " :
            print()
        else:
            print(word[i] , end="")
word("good moring sara alabar ")
"""

"""def splitword(word):
    nd=0
    for i in range(len(word)) :
        if word[i] == " " :
            print(word[nd:i+1])
            nd=i+1    
    word.split(" ")
    print("".join(word))
splitword("good moring sara alabar ")"""

# 2 str oneub in the econd (hello word python ) --> "hello " True "he" tre       "pt" false
'''def sub(t , w):
    return  w in t 
print(sub("hello word python","hello"))'''

""" 
def validpassword(password):
    result=[]
    lenth=lower=upper=number=False
    for i in password:
        if len(password) >= 8 :
            lenth= True
        if i.islower():
            lower= True 
        if i.isupper():
            upper= True
        if i.isnumeric() :
            number= True
    result.append(lenth)
    result.append(lower)
    result.append(upper)
    result.append(number)
    return all(result)
UserPassword="Limu#2022"
print(validpassword(UserPassword)) """

# pow
'''def power(x,y):
    z=pow(x, y)
    return z
a=power(2, 3)
print(a)'''

# sorted
'''
def sorted1(lst):
    print(sorted(lst))

def sorted2(lst):
    print(sorted(lst , reverse=True))

name=["Nahla" , "Nagib" , "Burweiss"]
sorted1(name)
sorted2(name)
'''
# abs
""" def ABS(x):
    return abs(x)
print(ABS(-9)) """

# CHR
""" x= chr(97)
print(x) """

# divmod
""" x=divmod(5, 2)
print(x) """

# Capetal letters Numbers
'''def ifUpper(txt):
    cnt=0
    for letter in txt :
        if letter.isupper():
            cnt+=1
    return cnt
s="MjilkHytWq"
print(ifUpper(s))'''

""" def word(w):
    for i in w :
        if i == " ":
            print()
        else:
            print(i , end="")
q= "Hello Python"
word(q) """

""" 
def ext(str):
    x=""
    for i in range(len(str)):
        if str[i]==".":
            x=str[i+1:]
        return x """

# ["A" , "B" , "C", "D" , "E" , "F"]  --> [3,10,15,,1] "A , D" "A,E" "A,F" "E,F" "D E"
""" def shopping(price ,names , val ):
    for i in range(len(price)) :
        for x in range(len(price)):
            if price[i] + price[x] <= val :
                print(names[i] , names[x])

price=[12,10,3,7,8,2,4]
names=["Pizza" , "Chocolata" , "Pepsi" , "Cheese" , "Nuella" , "Water" , "Orange"]
shopping(price,names,10)
 """
""" def shopping(price ,names , val):
    for i in range(len(price)) :
        for x in range(len(price)):
##["A" , "B" , "C", "D" , "E" , "F"]  --> [3,10,15,,1] """

# change to lower
'''def tolower(str):
    cnt=0
    x=""
    for i in str :
        if i.islower():
            x+=i
        else:
            x+= i.lower()
            cnt+=1
    print(x)
    print(cnt)
tolower("NaHLa")'''
'''def tolower(str):
    cnt=0
    x=""
    for i in str :
        if i.islower():
            x+=i
        else:
            x+= i.lower()
            cnt+=1
    print(x)
    print(cnt)
tolower("NaHLa")'''


# ["A" , "B" , "C", "D" , "E" , "F"]  --> [3,10,15,,1]

""" def shopping2(items , price , val):
    for i in range(len(price)):
        budget=val
        pay=list(divmod(budget , price[i]))
        if pay[0]!=0 :
            budget=pay[1]   
            print(f"You Can take {pay[0]} of {items[i]}" , end=' ')
            for c in range(len(price)):
                pay2=list(divmod(budget , price[c]))
                if pay2[0]!=0 :
                    budget=pay2[1]
                    print(f"and {items[c]}" , end='')
        print()
price=[12,10,3,7,8,2,4]
names=["Pizza " , "Chocolata " , "Pepsi " , "Cheese " , "Nutella " , "Water " , "Orange "]
shopping2(names, price, 10) """


# OOP
""" class student :
    name=""
    stdid=None
    email=""
    GPA=0.0
    def drop():
        pass
    def passed():
        pass
    def printinfo(self):
        print("Student Name is :" , self.name)
        print("Student ID is :" , self.stdid)
        print("Student Email is :" , self.email)
        print("Student GPA is :" , self.GPA)

a=student()
a.name="Nahla"
a.stdid=3675
a.email="nahla_3675@limu.edu.ly"
a.GPA=3
a.printinfo()
 """
""" def ext(text):
    x=""
    for i in range(len(text)):
        if text[i]==".":
            x=text[i+1: ]
    return x

de="hello.txt"
print(ext(de)) """
'''
class bankaccout :
    def __init__(self):
        self.name=""
        self.account_id=None
        self.type=
        self.balance=0
    def deposit(self):
        pass
    def withdraw(self):
        pass
    def printinfo(self):
        print(self.name)
        print(self.account_id)
        print(self.balance)
person1=bankaccout()
person1.name="NAHLA" 
person1.account_id=8888
person1.balance=9999
person1.printinfo()
class book():
    def __init__(self,n,w,p):
        self.name=n
        self.writer=w
        self.page=p
    def __str__(self):
        return f"name is {self.name} , the writer is {self.writer} , page is {self.page} "
    def __len__(self):
        return int(self.page)
    def __eq__(self, o):
        return(self.name==o.name)
b=book("oop" , "Ehab" , "320")
w=book("Python" , "Blal" , "400")
print(b)
print(len(b))
print(b==w)'''
""" class employee():
    def __init__(self,name , salary , project):
        self.name= name
        self.salary=salary 
        self.project = project
    def show(self):
        print(f"name is {self.name} , and salary is {self.salary}")
    def work(self):
        print(f"{self.name} is working on {self.project}")
emp=employee("ali" , 1000 , "Programming Project")
emp.show()
emp.work() """

""" 
class employee():
    def __init__(self):
        self.name= None
        self.salary=None 
        self.project = None
    def show(self):
        print(f"name is {self.name} , and salary is {self.salary}")
    def work(self):
        print(f"{self.name} is working on {self.project}")
emp=employee("ali" , 1000 , "Programming Project")
emp.show()
emp.work()
"""

'''class humanname():
    def __init__(self,fristname,middelname,lastname):
        self.fristname= fristname
        self.middelname=middelname 
        self.lastname = lastname
    def __info(self):
        return f"Name is {self.fristname} {self.middelname} {self.lastname}"
    def __str__(self):
        return self.__info()

H1=humanname("Nahla", "Nagib", "Burweiss")
print(H1)'''

""" class person():
    def __init__(self , name , age):
        self.name = name
        #1 make it privte 
        self.__age =age 
    #2 create getter
    @property()
    def age(self):
        return self.__age
    #3 create setter 
    @age.setter
    def age (self , v ):
        if v > 0 and v<=100 : 
            self.__age
        else : print("Out of Range !!")
p1:person()
p1.name="Asma"
p1.age=130
print(p1.name)
print(p1.age) """

# Slice(star , end"not include" , step)
""" a = "Hello python I am Nahla"
for i in range(len(a)) :
    if a[i] == "p":
        print(a[slice(i,12)]) """


#split (seperator , max)
""" a = "Hello python I am Nahla"
b=a.split(" ")
for i in b :
    print(i)
 """
# A TO THE POWER B :
""" def power(a,b):
    return pow(a, b)
a=int(input("add a :"))
b=int(input("add b :"))
print(power(a, b)) """

# Drive Examples :

# --------Functions--------

# 1st function : resevie list size , append an input user elemnts
# then calc the avrage of the list elemnts
# 2nd function : resevie list size , append an input user elemnts
# then calc the summtions of the list elemnts
""" def avg(n):
    A=[]
    for i in range(n):
        A.append(int(input("Enter nmber")))
    sum=0
    for i in A :
        sum+=i
    return sum/n

def summtion(n):
    A=[]
    for i in range(n):
        A.append(int(input("Enter nmber")))
    d=sum(A)
    return d
print(avg(5))
print(summtion(5)) """

# receive 2 number and return k where k=2A * 3b
""" def k(a,b):
    L=(2*a)*(3*b)
    return L
print(k(2, 1)) """

# receive 2 number and return minimum value
""" def minimum(a,b):
    return min(a ,b)
print(minimum(6, 17)) """

# funtion receive a list and return
# the number of even value
""" def even(lst):
    cnt=0
    for i in lst :
        if i %2 == 0:
            cnt+=1
    return cnt 
l=[5,8,6,3,1,0]
W=even(l)
print(W) """

# write function to receive string and print
# each word in one line
""" def one_word(str):
    list_words=str.split(" ")
    for i in list_words:
        print(i)
n="Hello Python I am Nahla And I am Tring Split Strings"
one_word(n) """

""" def words(string):
    word=""
    for i in string:
        if i == " ":
            print(word)
            word=""
        else:
            word+=i
n="Hello Python I am Nahla And I am Tring Split Strings"
words(n) """
# write function to receive like file name and
# version and return new file name with version
# ex: ("test.txt" , v5)   result("testV5.txt")
""" def File_name(name , version):
    newfilename=""
    for i in name :
        if i == ".":
            newfilename= newfilename + version +"."
        else: newfilename+=i
    print(newfilename)
name="test.txt"
File_name(name, "V5") """

# write fun to receive password and return true if
# password is valid and false if invalid
# 1 more than 7 letters
# 2  contain small letter
# 3 contain capital letter
# 4 contain number
""" def iflenth(password):
    if len(password) >= 8:
        return True
# --------
def iflower(password):
    for i in password:
        if i.islower():
            return True
# --------
def ifupper(password):
    for i in password:
        if i.isupper():
            return True
# --------
def ifdigit(password):
    for i in password:
        if i.isdigit():
            return True
# --------
def ifvalid(password):
    upper = ifupper(password)
    lenth = iflenth(password)
    lower = iflower(password)
    digit = ifdigit(password)
    result = [upper, lenth, lower, digit]
    print( all(result) )
# Main Program :
UserPassword = "Limu#2022"
ifvalid(UserPassword) """

# receive a string contain numbers inside rutern the number
# "K5tr6i9o" ---> "569"
""" def string_number(string):
    number=""
    for i in string:
        if i.isdigit()==True:
            number+=i
    return number
#main program 
a="K5tr6i9o"
print(string_number(a)) """

# function to receive list of student names
# and then print sorted and reversed
""" def sort(names):
    print(sorted(names))
def reversed(names):
    print(sorted(names , reverse=True))

num=int(input("Enter Number of students :"))
student=[]
for i in range(num):
    student.append(str(input("Enter Number of students : ")))
sort(student)
reversed(student) """

# write function to receive 2 lists and return odd count
# in both lists
""" def odd_count(lst1 , lst2):
    cnt1=cnt2=0
    for i in lst1:
        if i %2!=0:
            cnt1+=1
    for i in lst2:
        if i %2!=0:
            cnt2+=1
    return f"list 1 has {cnt1} odd number ,  list 2 has {cnt2} odd number "
a=[5,3,6,8,7]
b=[2,4,1]
print(odd_count(a, b)) """

# function to receive list and return avg of
# negative number
""" def negative_avg(num):
    cnt=0
    sum=0
    for i in num:
        if i < 0 :
            sum+=i
            cnt+=1
    return sum/cnt
a=[1,-3,-5,4]  
print(negative_avg(a))  """

# function to receive string and return how many
# times letter "s" occurs
""" def S_latter(string):
    cnt=0
    for i in string:
        if i.lower()=="s" : 
            cnt+=1
    return cnt
a="samira SsamS"
print(S_latter(a)) """

# fun reads list of integers and then return how many
# number 2 occurs
""" def digit2(int):
    cnt=0
    for i in int :
        if i == 2:
            cnt+=1
    return cnt 
a=[2 , 8 , 4,45,3,2,5,6,2]
print(digit2(a)) """

# function to find All Occurrences of “oo” in String
""" def counting(a,b):  #returns the number of elements with the specified value.
    return a.count(b)
print(counting("good morning and great mood ",'oo')) """

# recevi an Email return the name
""" def email_name(email):
    ndx=email.index("@")
    return email[:ndx] """
""" def name_email(email):
    nameofemail=""
    for i in email:
        if i =="@":
            print(nameofemail)
        else:
            nameofemail+=i

e="nahla.buweriss@gmail.com"
name_email(e) """

# Write function that receive two lists and return
# true if the second list is a sub-sequence from the first list and false otherwise.
""" def sub_sequence_2(sublist, mainlist):
    Sindex = 0
    Mindex = 0
    turelist=[]
    while Sindex < len(sublist) and Mindex < len(mainlist):
        if sublist[Sindex] == mainlist[Mindex]:
            Sindex += 1
            turelist.append(sublist[Sindex])
        Mindex += 1
    return turelist == sublist

main = [4,5,7,9,1,13,-5] 
sub = [13 ,7] 
print(sub_sequence_2(sub, main)) """
# function to return how many words in string
""" def words_in(string):
    list_words=string.split(" ")
    return len(list_words)
a="phyon nasser decamber"
print(words_in(a)) """
# write fun receive string and return how many small letters occures
""" def small_count(string):
    cnt=0
    for i in string:
        if i.islower()==True:
            cnt+=1
    return cnt
a="JGFWJfLPoo"
print(small_count(a)) """

# fun receive file name and return extension
""" def extension(string):
    ndx=string.index(".")
    return string[ndx+1:]
print (extension("track.mp3")) """

# given a sorted array of distnct int and a target value return the index of the target if found
# if not return the index where it would be
""" def ndx(num,target):
    num.append(target)
    num.sort()
    ndx= num.index(target)
    return ndx 

num=[1,3,5,6]
tar=2
print(ndx(num, tar)) """

# write a function that receives a txt and count how many capital letters in the string
""" 
def findCapital(txt):
    c=0
    for i in txt:
        if i.isupper()==True:
            c+=1
    return c
#main program 
intxt=(str(input("input your text: ")))
print(findCapital(intxt)) """


# --------OOP--------

# class car contain attribute: ownername, num , type , speed
# functions : drive() , stop() , printinfo()
# and then make object of this class

'''class car ():
    def __init__(self):
        self.ownername=None
        self.num=None
        self.type=None
        self.speed=None
    def drive():
        pass
    def stop():
        pass
    def printinfo(self):
        print(self.ownername)
        print(self.num)
        print(self.type)
        print(self.speed)
bmw=car()
bmw.ownername="Nahla"
bmw.num=5653
bmw.type="X80"
bmw.speed="350km/h"
bmw.printinfo()'''
# class student contain attribute: st_name, st_id , st_mark
# functions : print_st_info() and then make object of this class
""" class student():
    def __init__(self):
        self.st_name=None
        self.st_id=None
        self.st_mark=None
    def print_st_info(self):
        print(self.st_name)
        print(self.st_id)
        print(self.st_mark)
st1=student()
st1.st_name="nahla"
st1.st_id=3675
st1.st_mark= 90
st1.print_st_info() """
# class bank account contain attribute: name, account_id , balance
# functions : printinfo() , deposit() , withdraw() and then make object of this class
""" class bankaccout():
    def __init__(self):
        self.name=None
        self.account_id=None
        self.balance=None
    def deposit(self , value ):
        self.balance+=value
        print(f"Your New Balance Is {self.balance}")
    def withdraw(self,value):
        if self.balance >= 100 :
            self.balance-=value
            print(f"Here Is Your Cash {value}")
        else:
            print("Your Account Balance Under the Range")
    def printinfo(self):
        print(self.name)
        print(self.account_id)
        print(self.balance)
b=bankaccout()
b.name="nahla"
b.account_id=3675
b.balance=5000
b.deposit(600)
b.withdraw(1000) """

# CLASS
'''
class humanname():
    def __init__( self , fristname , secondname , lastname ):
        self.frist = fristname
        self.second = secondname
        self.last = lastname
    def __str__(self):
        return f"{self.frist} {self.second} {self.last}"
class student():
    def __init__(self , f , m , l):
        self.st_name=humanname(f, m, l)
        self.st_id=None
        self.st_mark=None
    def print_st_info(self):
        print(self.st_name)
        print(self.st_id)
        print(self.st_mark)
st1=student("Nahla" , "Nagib" ,"Burweiss")
st1.st_id=3675
st1.st_mark= 90
st1.print_st_info()
'''
# class hotel contain attribute: name, passport , stay
# functions : __init__(), check_in() , check_out () , Getpaid () , __str__()
#  __eq__() to compare if two object have same passport
'''
class hotel():
    def __init__(self , name, passpost , stay):
        self.name=name
        self.passport=passpost
        self.stay=stay
    def check_in():
        pass
    def check_out():
        pass
    def Getpaid(self): #100 LYD for each night 
        should_buy= self.stay*100
        return f"Dear customer , You Have To buy {should_buy}"
    def __str__(self):
        return f"hotel cus name : {self.name} , passport {self.passport} , stay {self.stay}"
    def __eq__(self, other):
        return self.passport == other.passport

person1=hotel("Nahla" ,11233 , 5)
person2=hotel("Nagat" ,112233 , 4)
print(person1==person2)
print(person1.Getpaid())'''

# class "My list class" contain attribute: lst()
# functions :readlst() , getsum() , getmulti() , getavg() , printrepeatNO()
#printarray() , find(x) , getelemnt(x)
'''
class mylist_class():
    def __init__(self , lst):
        self.lst=lst

    def readlst(self): #[3,5,2 , 2] --> output : 3 , 5 , 2 , 2
        for i in self.lst:
            print(i , end=",")
        print()

    def getsum(self): #[3,5,2 , 2] --> output : 12
        return f"Sum Is {sum(self.lst)}"

    def getmulti(self): #[3,5,2 , 2] --> output : 60
        result=1
        for i in self.lst:
            result=result*i
        return f"multi result is {result}"

    def getavg(self): #[3,5,2,2] --> output : 12/4 =3
        return f"avg is {sum(self.lst)/len(self.lst)}"

    def printrepeatNO(self):#[3,5,2,2] --> output : 2
        for i in self.lst:
            if self.lst.count(i)>=2 :
                print(f"repeted number is {i}")
                self.lst.remove(i)

    def printarray(self): #[3,5,2,2] --> output : [3,5,2,2]
        print(self.lst)

    def find(self,x):    #[3,5,2,2] , 5 --> output : 1
        for i in self.lst:
            if x==i:
                print(f"Your Elemnt {x} Index is {self.lst.index(i)}") 


    def getelemnt(self , x): #[3,5,2,2] , 5 --> output : 5
        for i in self.lst:
            if x==i:
                print(f"Your Elemnt {x} Is available")
    def __len__(self): #[3,5,2,2] --> output:4
        return len(self.lst)            
l=[3,5,2,2]
list1=mylist_class(l)
list1.readlst()
print(list1.getsum())
print(list1.getmulti())
print(list1.getavg())
list1.printrepeatNO()
list1.printarray()
list1.find(5)
list1.getelemnt(5)
print(list1)
print(len(list1))
'''
'''
# class employee contain attribute:EmpNo , EmpName , Empage
#Operyaer , Allwnc , Baicsalary , Companyname , EmpAddr
# contain Functions: printprofile() , Getannualbaiscsalary()
#GetSalary() , Getannualsalary
""" class humanname():
    def __init__( self , fristname , secondname , lastname ):
        self.frist = fristname
        self.second = secondname
        self.last = lastname
    def __str__(self):
        return f"{self.frist} {self.second} {self.last}"
class Employee():
    def __init__(self , f , m , l):
        self.EmpNo=None
        self.EmpName=humanname(f,m,l)
        self.EmpAge=None
        self.EmpAddress=None
        self.Companyname=None
        self.Operyaer=None
        self.Allwnc=None
        self.Baicsalary=None
    def printinfo(self):
        print(f"Number is {self.EmpNo} , Name Is {self.EmpName} , {self.EmpAge} Years , Address Is: {self.EmpAddress}, Work In {self.Companyname} , Open yaer: {self.Operyaer},Baic salary: {self.Baicsalary}")
    def Getannualbaiscsalary(self):
        print(f"annual baisc salary is {self.Baicsalary*12}")
    def GetSalary(self):
        tax=(12/100)*self.Baicsalary
        month=int(input("Enter Month Number:"))
        Salary=(self.Baicsalary+self.Allwnc[month-1])- tax 
        return Salary
    def Getannualsalary(self):
        annualsalary = self.GetSalary()*12
        print(f"Annual salary is {annualsalary}")
emp1=Employee("Nahla", "Nagib", "Burweiss")
emp1.EmpNo=3675
emp1.EmpAge=20
emp1.EmpAddress="Benghazi"
emp1.Companyname="CTR"
emp1.Operyaer=2010
emp1.Allwnc=[100 , 200 , 300 , 400 , 500 , 600 , 600 , 200 , 800 , 100 , 150 , 500]
emp1.Baicsalary=2000
emp1.printinfo()
emp1.Getannualbaiscsalary()
print(emp1.GetSalary()) """
# property
""" 
class person():
    def __init__(self):
        self.name=None
        self.__age=None

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self , v):
        if v >0 and v<100:
            self.__age = v
        else : print("aut of range ")

p1=person()
p1.name="Nahla"
p1.age=300
print(p1.name)
print(p1.age) """
# Writre Only
""" class person():
    def __init__(self):
        self.name=None
        self.__age=None

    @property
    def age(self):
        print("Erorr")
    @age.setter
    def age(self , v):
        if v >0 and v<100:
            self.__age = v
        else : print("aut of range ")

p1=person()
p1.name="Nahla"
p1.age=30
print(p1.name)
print(p1.age) """

#class Bank contain attribute:AccNo , AccName , AccType , Balance
# functions: deposit() , withdraw() , getcheckbook() , printAccountstatement()
# Default len Returning item balance
# compareing state return True if tow objects have same AccNo
""" class Bank():
    def __init__(self ):
        self.AccNo=None
        self.AccName=None
        self.AccType=AccountType()
        self.Balance=None
    def deposit(self , value ):
        self.Balance+=value
        print(f"Your New Balance Is {self.Balance}")

    def withdraw(self,value):
        if self.Balance >= 100 :
            self.Balance-=value
            print(f"Here Is Your Cash {value}")
        else:
            print("Your Account Balance Under the Range")
    def __eq__(self, other):
        return self.AccNo == other.AccNo
    def __len__(self):
        return self.Balance
    def getcheckbook(self):
        pass
    def printAccountstatement(self):
        pass
bank=Bank()
bank.AccNo=4123
bank.AccName="Nahla"
bank.AccType="Student Account"
bank.Balance=2000
bank.withdraw(100)
bank.deposit(1000)
print(bank)
print(len(bank))
 """

#class Bank contain attribute:AccNo , AccName , AccType , Balance
# functions: deposit() , withdraw() , getcheckbook() , printAccountstatement()
# Main program --> print the summtion of balance for 4 objects 
""" class Bank():
    def __init__(self , Name , Type , balance):
        self.AccName=Name
        self.AccType=Type
        self.Balance=balance
    def deposit(self , value ):
        pass
    def withdraw(self,value):
        pass
    def getcheckbook(self):
        pass
    def printAccountstatement(self):
        pass
O1=Bank("Nahla", "Student Account", 2000)
O2=Bank("Omar", "Current Accounts", 1500)
O3=Bank("Abdullah", "Savings  Accounts", 3500)
sum=O1.Balance+O2.Balance+O3.Balance
print(sum) """



#class Account Name contain attribute: TypeNo  , Typename
#PROPRTY FOR ALL AND default print --> show the class intormation
""" class Account():
    def __init__(self):
        self.__TypeNo:None
        self.__TypeName=None

    @property
    def TypeNo(self):
        return self.__TypeNo
    @TypeNo.setter
    def TypeNo(self, v):
        self.__TypeNo = v

    @property
    def TypeName(self):
        return self.__TypeName
    @TypeName.setter
    def TypeName(self, v):
        self.__TypeName = v


    def __str__(self):
        return f"{self.__TypeNo} - {self.__TypeName}"
v1=Account()
v1.TypeName="Nahla"
v1.TypeNo=3675
print(v1) """

#Fanction Name(SpecialSearch) receive string and number and return Ture if the all Individual numbers exist 
#"HY3IK4L5P" , "345" ---> True 
""" def sub_sequence(string, number):
    Strndx=0
    numndx=0
    list1=[]
    while Strndx< len(string) and numndx< len(number):
        if string[Strndx] == number[numndx]:
            list1.append(number[numndx])
            numndx+=1
        Strndx+=1
    return list(number)==list1
a="HY3IK4L5P"
b="35"
print(sub_sequence(a,b))


def sub_sequence(string, nummber):
    number=str(nummber)
    exist=False 
    Strndx=0
    numndx=0
    while Strndx< len(string) and numndx< len(number):
        if string[Strndx] == number[numndx]:
            exist=True
            numndx+=1
        Strndx+=1
    return exist
a="HY3IK4L5P"
b=235
print(sub_sequence(a,b)) """


""" class person :
    def __init__(self , f , l):
        self.firstname=f
        self.lastname=l
    def printname(self):
        print(f"{self.firstname} {self.lastname}")

class student(person) :
    def __init__(self , f,l  , year ):
        super().__init__(f, l)
        self.graduationyear = year
x=student("Nahla" ,"Burweiss" , 2010 )
x.printname() """
'''
'''
class person() :
    def __init__(self):
        self.firstname=None
        self.lastname=None
    def printname(self):
        print(f"{self.firstname} {self.lastname}")
class student(person) :
    def __init__(self):
        self.graduationyear = None

x=student()
x.firstname="Nahla"
x.lastname="Burweiss"
x.graduationyear=2010
print(x.graduationyear)'''
'''
class parent():
    def __init__(self,v):
        self.v=v
    def show(self):
        raise NotImplementedError
        
class child(parent):
    def __init__(self, f , J):
        self.j=super(J).__init__(self,J)
        self.f=f   
    def show(self):
        print("Hello" ,self.j )
#obj1=parent("Python")
obj2=child("hello","Hello")
#obj2.show()
'''
'''
class parent():
    def __init__(self,v):
        self.v=v
    def show(self):
        print("Hello" ,self.v )
        
class child(parent):
    def __init__(self, v):
        super().__init__(v)   
    def show(self):
        print("Hello" ,self.v )
obj1=parent("Class one")
obj2=child("Class Two")
obj2.show()
obj1.show()
'''
'''
class n_o():
    def __init__(self , number):
        self.number=number
obj1=n_o(55)
obj2=n_o(66)
obj3=n_o(44)
object_list=[obj1 , obj2 , obj3 ]
for obj in object_list:
    print(obj.number)

class student:
    def __init__(self , name , mark):
        self.name=name
        self.merk=mark
lst=[]
lst.append(student("ali" , 26))
lst.append(student("nahla" , 14))
lst.append(student("m" , 44))
for obj in lst :
    print(obj.name , obj.mark)'''
'''
class student:
    def __init__(self ):
        self.name=None
        self.merk=None
list=[4]
print(list)
for i in range(len(list)) :
    list[i]=student()
    list[i].name=input("Enter name ")
    list[i].mark=input("Enter mark ")
print(list[2].name)'''


#Encapsulation 
'''
class HumanName :
    def __init__(self) :
        self.__Fristname=None
        self.__MiddlName=None
        self.__LastName=None
    @property
    def FristName(self):
        return self.__Fristname
    @FristName.setter
    def FristName(self,v):
        self.__Fristname=v 
#Make the Middel Name Read Only 
    @property
    def MiddlName(self):
        return self.__MiddlName

#Make the Last Name Write Only 
    @property
    def LastName(self):
        print("Erorr")
    @LastName.setter
    def LastName(self,v):
        self.__LastName=v 


    def __GetFullName(self):
        return f"{self.__Fristname} {self.__MiddlName} {self.__LastName}"
    def PrintFullName(self):
        print(self.__GetFullName())
    def __len__(self):
        return len(self.__GetFullName())
obj1=HumanName()
obj1.Fristname="Nahla"
obj1.MiddlName='Nagib'
obj1.LastName="Burweiss"
obj1.PrintFullName()
print(len(obj1))
'''
'''
class person :
    pass

class Customer(person):
    def __init__(self):
        self.CustNo=None
        self.Adr=None
        self.Email=None
    def Dilevery(self):
        raise NotImplementedError("Can Not Run This Function From Here")
    def PrintProfile(self):
        print(f"Email: {self.Email} Address: {self.Adr} Number: {self.CustNo}")
    def GetItem(self,x):
        pass
    def GetTotalPrice(self):
        print("This Is From Base")
class HostingCustomer(Customer):
    def __init__(self):
        self.custDomain=None
        self.CusIP=None
    def Dilevery(self):
        print("Yes , From this Child You Can Call This Function")
    def AddHost(self):
        pass
    def GetTotalPrice(self):
        print("This Is From Child")

obj1=Customer()
obj1.Adr="Benghazi"
obj1.CustNo=3657
obj1.Email="Nahla@Nahla.com"
#obj1.Dilevery()
obj2=HostingCustomer()
obj2.Dilevery()'''
#LIST OF OBJECTS
'''
class listofobjects:
    def __init__(self , number1 , number2):
        self.x=number1
        self.y=number2
    def sum(self):
        return self.x+self.y

listone=[]
listone.append(listofobjects(3,4))
listone.append(listofobjects(1,6))
listone.append(listofobjects(5,2))
for obj in listone:
    print (obj.sum())'''

'''
class student:
    def __init__(self , name , GPA):
        self.name=name
        self.GPA=GPA
stu=[]
n=int(input("Number of students"))
for i in range(n):
    stu.append(student(str(input("Student Name: ")) , int(input("Student GPA: "))))
for obj in stu:
    if obj.GPA >= 50:
        print(f"{obj.name} Is PASS" )
    else:
        print(f"{obj.name} Is Faild")'''
"""
class persson:
    def __init__(self):
        self.__name=None
        self.__age=None
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,v):
        self.__name=v

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,v):
        self.__age=v

    def printinfo(self):
        return f"{self.name},{self.age}"
A=persson()
A.age=19
A.name="Nahla"
print(A.printinfo())"""

#OverLoding
#Two Numbers
""" from multipledispatch import dispatch
class number:
    @dispatch(int,int)
    def sum (self ,n1 , n2):
        print(n1+n2)
    
    @dispatch(float , float)
    def sum (self ,n1 , n2):
        print(n1+n2)

    @dispatch(str,str)
    def sum (self ,n1 , n2):
        print(n1+n2)

    @dispatch(str,str,str)
    def sum (self ,n1 , n2 , n3):
        print(n1+n2+n3)
A=number()
A.sum("nahla " , "nagib") """

'''
def getseem(a,b):
    q=0
    for i in a :
        for c in b :
            if i == c:
                q+=1
    return q 
LST1=[1,4,5,7,8,9]
LST2=[12,1,4,6,3,22]
print(getseem(LST1,LST2))'''


'''def unique (lst1 , lst2):
    cnt=0
    for i in lst1 :
        unique=0
        for j in lst2 :
            if i == j:
                unique=1
        if unique == 0 : 
            cnt+=1
    return cnt 
a=[12,34,11,10,31]
b=[32,33,11,10]
print(unique(a,b))'''
'''
def word (a):
    for i  in a :
        if i == " " :
            print()
        else: 
            print(i , end = "")
k="Good Morning"
word(k)'''

