with open("example.txt", "a+") as file:
    lines=['Line7','Line8','Line9']
    for item in lines:
        file.write(item+"\n")