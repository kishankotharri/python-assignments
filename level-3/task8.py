string = "Robert000Smith000123"

arr = string.split("000")

key = ['first_name', 'last_name', 'id']

new_list = {}

for x in range(0,len(arr)):
    new_list[key[x]] = arr[x]

print(new_list)