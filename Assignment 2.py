#question 1
#(a)
# to take input as 'Python is a case sensitive language'
print("(a)")
input_string=input("Give the statement:")
print(input_string)
length=len(input_string) #To print the length of the string
print(length)

#(b)
print("(b)")
reverse_string=input_string[length::-1] #To reverse the string
print(reverse_string)

#(c)
print("(c)")
new_string=input_string[10:26]
print(new_string)

#(d)
print("(d)")
#replace 'a case sensitive' with 'oject oriented'
replaced_string=input_string[0:10]+'object oriented'+input_string[26:35]
print(replaced_string)

#(e)
print("(e)")
index_a=input_string.find('a') #It finds the index of "a"
print(index_a)

#(f) first check the index of white spaces and then write the new string by not using those index
print("(f)")
remove_whitespaces=input_string.replace(" ","")
print(remove_whitespaces)
print(" ")
print(" ")
print("***")
print(" ")
print(" ")

#q2
name="Vivek Kumar Rahul"
SID=21104124
department_name="EE"
CGPA="9.9"

print("Hey,%s Here!"%(name))
print("My SID is %d"%(SID))
print("I am from %s department and my CGPA is %s"%(department_name,CGPA))
print(" ")
print(" ")
print("***")
print(" ")
print(" ")

#q3
#a=56 b=10
a=0b111000
b=0b1010

#(a)
print("(a)")
#&
print(bin(a&b))

#(b)
print("(b)")
#|
print(bin(a|b))

#(c)
print("(c)")
#^
print(bin(a^b))

#(d)
print("(d)")
#a<<2 b<<2 ,left shift 2
print(bin(a<<2))
print(bin(b<<2))

#(e)
print("(e)")
#a>>2 b>>4 right shift a with 2 bits and b with 4 bits
print(bin(a>>2))
print(bin(b>>4))
print(" ")
print(" ")
print("***")
print(" ")
print(" ")

#q4
num_1=int(input("Give a number:")) #Input first number
num_2=int(input("Give a number:")) #Input second number
num_3=int(input("Give a number:")) #Input third number

if(num_1>num_2):
    if(num_1>num_3):
        print(num_1,"is greatest number")
    else:
        print(num_3,"is greatest number")
else:
    if(num_2>num_3):
        print(num_2,"is greatest number")
    else:
        print(num_3,"is greatest number")
print(" ")
print(" ")
print("***")
print(" ")
print(" ")

#q5
user_input=input("Give a word:") #Input the string
if("name"in user_input):    #It checks whether the "name" is in the string or not
    print("Yes")
else:
    print("No")
print(" ")
print(" ")
print("***")
print(" ")
print(" ")

#q6
side_1=int(input("Give a number:")) #Input first side
side_2=int(input("Give a number:")) #Input second side
side_3=int(input("Give a number:")) #Input third side

if(side_1+side_2>side_3 and side_2+side_3>side_1 and side_1+side_3>side_2):
    print("The triangle is possible")
else:
    print("The triangle is not possible")
print(" ")
print(" ")
print("***")
print(" ")
print(" ")
