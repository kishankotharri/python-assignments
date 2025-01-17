students = ['Sam', 'Alice', 'Mona']
subjects = ['Commerce', 'Science', 'Computer']

new_list = {}

for x in range(0,len(students)):
    new_list[students[x]] = subjects[x]

print(new_list)