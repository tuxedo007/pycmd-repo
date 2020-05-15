file=open("file.txt", 'r')
file.seek(0)
content=file.readlines()
print(content)