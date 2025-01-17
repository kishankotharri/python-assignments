string = "wwwwaaadebbbbbw"

def count_char(string):
    str_list = list(string)
    total = len(str_list)
    count = 1
    a = ''
    new_string = ''


    for x in list(str_list):

        if a == x:
            count += 1

        if a != x:        
            new_string = new_string + a
            if len(new_string) != 0:
                new_string = new_string + str(count)

            count = 1
            a = x

            if total == 1:
                new_string = new_string + x
                new_string = new_string + str(count)

        total -= 1
    return new_string
    
print(count_char(string))