my_list = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter the index you want to access: "))
    element = my_list[index]
    print("Element at index:", index, element)
except:
    print("Please enter a valid integer for the index.")