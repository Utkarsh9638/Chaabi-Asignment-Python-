# Chaabi Assignment 
# Question 1
#Code for Implementation of selection Sort algorithm
def selection_sort(arr):
    for i in range(len(arr)):
        min_ind = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_ind]:
                min_ind = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_ind] = arr[min_ind], arr[i]

    return arr

# Test the function
new_list = [5, 416, 54, 21, 6135, 15, 741]
ans_list = selection_sort(new_list)
print(ans_list)

#Question 2
# This code prints the prints the file type from file name 
def get_file_type(extension_type_str, filenames):
    extension_type_pairs = extension_type_str.split(';')
    extension_type_dict = {}
    for pair in extension_type_pairs:
        extension, file_type = pair.split(',')
        extension_type_dict[extension] = file_type

    result = {}
    for filename in filenames:
        file_parts = filename.split('.')
        if len(file_parts) > 1:
            extension = file_parts[-1]
            if extension in extension_type_dict:
                result[filename] = extension_type_dict[extension]
            else:
                result[filename] = "unknown"
        else:
            result[filename] = "unknown"

    return result


extension_type_str = "xls,spreadsheet;xlsx,spreadsheet;jpg,image"
filenames = ["abc.jpg", "xyz.xls", "text.csv", "123"]
result_dict = get_file_type(extension_type_str, filenames)
print(result_dict)

#Question 3
#Python program that sorts a list of dictionaries based on a given key
def sort_list_of_dicts(lst, key):
    sorted_list = sorted(lst, key=lambda x: x[key])
    return sorted_list


input_list = [
    {"fruit": "orange", "color": "orange"},
    {"fruit": "apple", "color": "red"},
    {"fruit": "banana", "color": "yellow"},
    {"fruit": "blueberry", "color": "blue"}
]

sorted_list_by_fruit = sort_list_of_dicts(input_list, "fruit")
print(sorted_list_by_fruit)

sorted_list_by_color = sort_list_of_dicts(input_list, "color")
print(sorted_list_by_color)
 
#Question 4
def switch_dict(dict_input):
    return dict((v, k) for k, v in dict_input.items())
dict_input = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
    "key5": "value5"
}
result_dict = switch_dict(dict_input)
print(result_dict)

# Question 5
def compare_lists(list1, list2):
    common_elements = list(set(list1) & set(list2))
    non_common_elements = list(set(list1) ^ set(list2))
    return common_elements, non_common_elements


mainstream = [
    "One Punch Man", "Attack On Titan", "One Piece", "Sword Art Online",
    "Bleach", "Dragon Ball Z", "One Piece"
]

must_watch = [
    "Full Metal Alchemist", "Code Geass", "Death Note", "Stein's Gate",
    "The Devil is a Part Timer!", "One Piece", "Attack On Titan"
]

common, non_common = compare_lists(mainstream, must_watch)
print(common)
print(non_common)

# Question 6
# Sub_List between two indices with gap of 2
def get_sublist(lst, start_index, end_index):
    sublist = lst[start_index:end_index+1:2]
    return sublist


input_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
start_index = 2
end_index = 9

result = get_sublist(input_list, start_index, end_index)
print(result)

# Question 7
factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)
 # Test Case
num = 5
result = factorial(num)
print(f"The factorial of {num} is: {result}")

#Question 8
from functools import reduce

A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i: i*i for i in A1}
A6 = [[i, i*i] for i in A1]
A7 = reduce(lambda x, y: x + y, [10, 23, -45, 33])
A8 = list(map(lambda x: x*2, [1, 2, 3, 4]))
A9 = list(filter(lambda x: len(x) > 3, ["I", "want", "to", "learn", "python"]))

print("A0:", A0)
print("A1:", list(A1))
print("A2:", A2)
print("A3:", A3)
print("A4:", A4)
print("A5:", A5)
print("A6:", A6)
print("A7:", A7)
print("A8:", A8)
print("A9:", A9)

#Question 9
from datetime import datetime, timedelta

def check_date_difference(from_date, to_date, difference):
    # Convert string dates to datetime objects
    from_date_obj = datetime.strptime(from_date, '%y-%m-%d')
    to_date_obj = datetime.strptime(to_date, '%y-%m-%d')

    # Calculate the difference in days
    date_difference = abs((to_date_obj - from_date_obj).days)

    # Compare the difference with the provided value
    if date_difference < difference:
        return True
    else:
        return False
    result1 = check_date_difference('21-05-01', '21-05-10', 10)
    print(result1)  # Output: True

    result2 = check_date_difference('21-05-01', '21-05-15', 10)
    print(result2)

# Question 10
from datetime import datetime, timedelta

def get_date_before(date, n):
    # Convert string date to datetime object
    date_obj = datetime.strptime(date, '%y-%m-%d')

    # Calculate the date before by subtracting timedelta
    date_before = date_obj - timedelta(days=n)

    # Convert the date before back to string representation
    date_before_str = date_before.strftime('%y-%m-%d')

    return date_before_str


# Question 11
def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)
    f(2)
    f(3,[3,2,1])
    f(3)
# Output:
[0, 1]
[3, 2, 1, 0, 1, 4]
[0, 1, 0, 1, 4]

# When f(2) is called, the function f is executed with x equal to 2
# When f(3, [3, 2, 1]) is called, the function f is executed with x equal to 3 and the provided list [3, 2, 1] assigned to l
# When f(3) is called without providing a second argument, the function f is executed with x equal to 3. Since the default value for l is assigned as an empty list [], the previously modified list [0, 1, 0, 1, 4] is used as the default value.   












