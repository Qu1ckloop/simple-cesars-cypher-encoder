def encode(text,s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        elif (char == " "):
            result += " "
        else:
            result += chr((ord(char) + s-97) % 26 + 97)
    return result

text = input("enter message to be encoded ")
s = int(input("what is the key you want to use "))

print("your encoded message: " + encode(text,s))
