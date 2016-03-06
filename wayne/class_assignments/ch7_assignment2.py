fname = raw_input("Enter file name: ")
fh = open(fname)
i = 0
sum = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    #Get the confidence score, strip out any spaces and convert to a float
    score = float(line.partition(":")[2].strip())
    #add the scores together
    sum = sum + score
    #print line
    #print score
    #keep count of the number of lines we found
    i = i + 1
#calculate the average
avg = sum / i
#print it out
print "Average spam confidence: {:.12}".format(avg)