Input_sentence = "Hello, World! Welcome to Python programming."

words = Input_sentence.split()
reversed_words = words[::-1]

New_sentence = ' '.join(reversed_words)

print(New_sentence)