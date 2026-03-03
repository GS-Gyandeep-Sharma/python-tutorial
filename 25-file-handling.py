#opening a flie
#r = Read
#w = Write
#a = Append
#rb/wb = Read/Write in binary mode

# read()        = reads the entire content of file
file = open('example.txt','r')
content = file.read()
print("read()")
print(content)
file.close()
# readline()    = reads one line from file at a time
file = open('example.txt','r')
content = file.readline()
print("readline()")
print(content)
file.close()
# readlines()   = reads all the line into list
file = open('example.txt','r')
content = file.readlines()
print("readlines()")
print(content)
file.close()


#write()        = Write a string to a file
file = open('example.txt','w')
content = file.write("Hello world")
file.close()
#appending a line
file = open('example.txt','a')
content = file.write("\nGyandeep Sharma")
file.close()
#writelines()   = Write a list of strings
file = open('example.txt','a')
content = file.writelines("")
file.close()



