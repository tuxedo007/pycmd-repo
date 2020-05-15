file=open("example.txt", 'a')
lines=['Line4','Line5','Line6']
for item in lines:
    file.write(item+"\n")
file.close()