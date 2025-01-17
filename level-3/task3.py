def JtoI():
    r = open("words.txt", "r")

    c = r.read()

    new_content = c.replace("J", "I")

    print(new_content)

JtoI()