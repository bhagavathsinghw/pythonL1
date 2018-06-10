import string
try:
    input_file=open("input.txt",'r')
    output_file=open("output.txt",'w')
except IOError as err:
    print err

inp=input_file.readlines()
length=len(inp)
for i in range(0,length):
    no_of_words=len(inp[i].split())
    no_of_letters=len(inp[i])
    output_file.write("Line : %d , Words : %d , Letters : %d \n" %(i+1,no_of_words,no_of_letters))
input_file.close()
output_file.close()