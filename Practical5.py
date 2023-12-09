# Write a Python program to store names and mobile numbers of your friends in
# sorted order on names. Search your friend from list using binary search (recursive and
# non- recursive). Insert friend if not present in phonebook.

name = []
phone_number = []

print("Hit enter without any data to finish entering entries.")
while True:
    data = input("Enter data in format (Name Number): ")
    if not data:
        break
    else:
        data = data.split(" ")
        name.append(data[0])
        phone_number.append(int(data[1]))

print("Names entered by the user:")
print(name)
print("Phone numbers entered by the user:")
print(phone_number)

# Sort the lists for binary search
for i in range(0, len(name)):
    for j in range(i + 1, len(name)):
        if name[i] > name[j]:
            temp_name = name[i]
            name[i] = name[j]
            name[j] = temp_name
            temp_number = phone_number[i]
            phone_number[i] = phone_number[j]
            phone_number[j] = temp_number

print("sorted names")
print(name)
print("sorted numbers")
print(phone_number)

# Binary search (recursive)
def binary_search_recursive(arr, target, start, end):
    if start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search_recursive(arr, target, mid + 1, end)
        else:
            return binary_search_recursive(arr, target, start, mid - 1)
    else:
        return -1

# Binary search (non-recursive)
def binary_search_non_recursive(arr, target):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

search = input("Enter name and number you want to search (in format Name Number): ")
search_data = search.split(" ")
search_name = search_data[0]
search_number = int(search_data[1])

# Perform binary search
index_recursive = binary_search_recursive(name, search_name, 0, len(name) - 1)
index_non_recursive = binary_search_non_recursive(name, search_name)

# Display the results
if index_recursive != -1:
    print(f"{search_name} found at index {index_recursive} (recursive search)")
else:
    print(f"{search_name} not found (recursive search)")

if index_non_recursive != -1:
    print(f"{search_name} found at index {index_non_recursive} (non-recursive search)")
else:
    print(f"{search_name} not found (non-recursive search)")

# Insert the friend if not present
if index_recursive == -1:
    # Insert at the correct position
    position = 0
    while position < len(name) and search_name > name[position]:
        position += 1

    name.insert(position, search_name)
    phone_number.insert(position, search_number)

    print(f"{search_name} inserted into the phonebook.")
    print("Updated names in the phonebook:")
    print(name)
    print("Updated phone numbers in the phonebook:")
    print(phone_number)
