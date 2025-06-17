input()
chars = input()
message = input()

if (all([char in chars for char in message])):
    print("S")
else:
    print("N")