file=open("example.txt", 'w')
lines=['Line1','Line2','Line3']
for item in lines:
    file.write(item+"\n")
file.close()