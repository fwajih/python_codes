filename = raw_input("please indicate file name ")
#filename = "words.txt"
numlines = 0
with open(filename, 'r') as file:
    for line in file:
        numlines += 1
print "Number of Lines: %s " % (numlines) 
