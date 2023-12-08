# Write a Python program to store marks scored in subject “Fundamental of Data Structure” by N students
# in the class. Write functions to compute following:
# a) The average score of class
# b) Highest score and lowest score of class
# c) Count of students who were absent for the test
# d) Display mark with highest frequency

marklist = []
absents = []
presents = []
print()
students = int(input("Enter Number of Students : "))
print()

for i in range(1, students + 1):
    marks = input(f"Enter Marks Obtained by Roll Number {i} : ")
    if marks == "ab":
        absents.append(marks)
    else:
        presents.append(marks)
    marklist.append(marks)
print()
def average():
    sum = 0
    for i in presents:
        sum = sum + int(i)
    avg = sum / len(presents)
    print()
    print(f"Average of Class : {avg}")

def highest():
    high = 0
    for i in presents:
        if int(i) > int(high):
            high = i
    print()
    print(f"Highest of Class : {high}")

def lowest():
    low = 999
    for i in presents:
        if int(i) < int(low):
            low = i
    print()
    print(f"Lowest of Class : {low}")  
    print()

print(f"The Number of Present Students = {len(presents)}")
print(f"The Number of Absent Students = {len(absents)}")

def highest_frequency():
    temp = 0
    count = 0
    index = 0
    for i in range(0, len(presents)):
        temp = presents.count(presents[i])
        if temp > count:
            count = temp
            index = i
    print()
    print(f"The marks {presents[index]} and it is repeated {count} times")
    print()

average()
highest()
lowest()
highest_frequency()
