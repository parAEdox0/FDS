# Write a python program to store roll numbers of student array who
# attended training program in sorted order.
# Write function for searching whether particular student attended training program or not,
# using Binary search and Fibonacci search'''

def binary_search(list, target):

    lower_bound = 0
    upper_bound = len(list)-1

    while lower_bound <= upper_bound:

        mid = (lower_bound + upper_bound) // 2

        if list[mid] == target:
            print(f"Roll number {target} has attended the training program and is found at position {mid}")
            print()
            break
        elif list[mid] < target:
            lower_bound = mid + 1

        else: 
            upper_bound = mid - 1
    else:
        print(f"Roll number {target} has not attended the training program")     
        print()  

present_list = []

print()
number_of_students = int(input("Enter number of students attended the Program : "))
print()

for i in range(0, number_of_students):
    roll_numbers = int(input("Enter roll number of students : "))
    present_list.append(roll_numbers)

print()

for i in range(0, len(present_list)):
    for j in range(i + 1, len(present_list)):
        if present_list[i] > present_list[j]:
            temp = present_list[i]
            present_list[i] = present_list[j]
            present_list[j] = temp


print(f"Roll numbers of students attended training program = {present_list}")
print()


key = int(input("Enter the roll number you want to search : "))
print()


binary_search(present_list, key)
