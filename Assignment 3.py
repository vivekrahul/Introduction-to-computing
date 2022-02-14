#Answer 1
print("Solution 1")
print("This program will count number of letters if a single word is inserted and and will print number of words if sentences are inserted")

string = input("Enter a string: ").lower() 
#converting the string to lowercase so that upper and lower case characters are not treated differently


str_list = string.split()
#splitting the string
def dict_count(list):
    count = {}
    
    n = len(list)
    for i in range(n):
        if list[i] in count:
            count[list[i]] += 1
        else:
            count[list[i]] = 1
    return count

#check for number of words
if len(str_list) == 1:
    
    #making a list of all the letters
    str_list = list(str_list[0])

    print(dict_count(str_list))
else:
    # the list has more than one word
    # so the function will count the words
    
    print(dict_count(str_list))

print("_____________________________________________________________")


print("Solution 2")
print("python program to print next date of input date with given input")

def calander_year(year):
    if (year % 400 == 0):
        leap_year = True
    elif (year % 100 == 0):
        leap_year = False
    elif (year % 4 == 0):
        leap_year = True
    else:
        leap_year = False
        
    return leap_year


   
def calander_month(month, leap_year):
    if month in (1, 3, 5, 7, 8, 10, 12):
        month_length = 31
    elif month == 2:
        if leap_year:
            month_length = 29
        else:
            month_length = 28
    else:
        month_length = 30
        
    return month_length

def calander_day(day, month, year, month_length):
    if day < month_length:
        day += 1
    else:
        day = 1
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
            
    return [day, month, year]



def main():
    day = int(input("Day [1-31]: "))
    month = int(input("Month [1-12]: "))
    year = int(input("Year[1800-2025]: "))
    leap_year = calander_year(year)
    month_length = calander_month(month, leap_year)
    n_list = calander_day(day, month, year, month_length)
    print("The next date is: {}/{}/{}".format(n_list[0], n_list[1], n_list[2]))
    
main()

print("__________________________________________________")



print("\n\nSolution 3")

inputlist = list(map(int, input("Enter a list of numbers: ").split()))

squarelist = [(inputlist[i], inputlist[i]**2) for i in range(len(inputlist))]

print(squarelist)

print("______________________________________________")

print("Solution 4")
x=int(input('Enter the Grade Points:'))
#Checking if the input lies in the given range or not
if x>10 or x<4:
    print('Error, out of range value entered')
    exit()
    #exiting the program if value is out of range to prevent it from executing anymore

#checking And assig15ning the correct values to Grade points
elif x==4:
    performance= "Poor" ; Letter_Grade="D"
elif x==5:
    performance= "Below Average" ; Letter_Grade="C"
elif x==6:
    performance= "Average" ; Letter_Grade="C+"
elif x==7:
    performance= "Good" ; Letter_Grade="B"
elif x==8:
    performance= "Very Good" ; Letter_Grade="B+"
elif x==9:
    performance= "Excellent" ; Letter_Grade="A"
elif x==10:
    performance= "Outstanding" ; Letter_Grade="A+"
print("Your Grade is ", Letter_Grade, "and", performance, "Performance")

print("__________________________________________________")




print("\nSolution 5")
#making the string given in question alphabets
alphabet = "ABCDEFGHIJK"

#defining a var for printing the alphabets
col = 11

#for the rows
for i in range(6):
    # print the spaces
    # 1 less than the row number
    print(" "*i, end="")
    
    # print the alphabets/columns
    # 11 for the first row with a decrement of 2
    print(alphabet[:col])
    col -= 2
print("_________________________________________________________")

print("Solution 6")

dic = {}
name = input("Enter Name: ")
sid = int(input("Enter SID: "))
dic[sid] = name
ch = input("Do you want to enter more details[y/n]: ")
while ch=="y":
    name = input("Enter Name: ")
    sid = int(input("Enter SID: "))
    dic[sid] = name
    ch = input("Do you want to enter more details[y/n]: ")
    
print("\nDetails of the students: ") 
print("SID\tName")
for i in dic:
    print("{}\t{}".format(i, dic[i]))
    
print("\nSorted dictionary using student SID: ") 
sort_id = {k: v for k, v in sorted(dic.items())}
print("SID\tName")
for i in sort_id:
    print("{}\t{}".format(i, dic[i]))    
        
print("\nSorted dictionary using student Names: ") 
sort_names = {k: v for k, v in sorted(dic.items(), key = lambda v:v[1])}
print("SID\tName")
for i in sort_names:
    print("{}\t{}".format(i, dic[i]))   
        
id = int(input("\nEnter the SID of the student: "))
if id in dic:
    print("Name of the student is: ",dic[id])
else:
    print("The entered SID is not found")



print("-__________________________________________________")

print("\n\nSolution 7.")

n = int(input("Enter the upper limit of fibbonacci sequence: "))
# making a list of fibonacci sequence
if n == 1:
    fib = [1]
else:
    fib = [1, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    print(fib)

sum = 0
for i in range(n):
    #add the number to later find out the average
    sum += fib[i]

#print average
print("The average of the series is ", sum/n)
print("_______________________________________________________")


print("Solution 8")

Set1= {1, 2, 3, 4, 5}
Set2= {2, 4, 6, 8}
Set3= {1, 5, 9, 13, 17}
Set4= {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
#first part
z=Set2.difference(Set1)
y=Set1.difference(Set2)
S = y.union(z)
print(S)
    
#second part
x = Set1.difference(Set2.union(Set3))
y = Set2.difference(Set1.union(Set3))
z = Set3.difference(Set2.union(Set1))
S = x.union(y.union(z))
print(S)
    
#third part
x = (Set1.intersection(Set2)).difference(Set3)
y = (Set3.intersection(Set2)).difference(Set1)
z = (Set1.intersection(Set3)).difference(Set2)
S = x.union(y.union(z))
print(S)
    
#fourth part
S = Set4.difference(Set1)
print(S)
    
#fifth part
t = Set1.union(Set2.union(Set3))
S = Set4.difference(t)
print(S)

print("--------------------------------------------------------")

