fname = input("Enter file name: ")
#use romeo file
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    line = line.split()
    for i in line:
        if i not in lst:
            lst.append(i)

lst.sort()
print(lst)
