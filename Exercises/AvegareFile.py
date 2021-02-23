fname = input("Enter a file name: ")
#use mbox-short file
fh = open(fname)
count = 0
som = 0
for line in fh:
    line = line.rstrip()
    if not 'X-DSPAM-Confidence:' in line:
        continue
    count = count + 1
    lval = line.find(': ')
    val = line[lval+1 :]
    som =  som + float(val)
    avg = som / count
print("Average spam confidence:", avg)
