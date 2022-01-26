f = open("purchasedata.txt","r")
o = open("output1.txt","w")           # open file, read-only
for line in f:  
    outputList = line.strip().split("    ")    # count the spaces!
    print (outputList   )
    print (len(outputList  ))
    if len(outputList  ) == 6:
        date, time, location, dept, amount, payType = outputList  #assign names
        print ("{0}\t{1}".format(location, amount))
        o.write("{0}\t{1}\n".format(location, amount))
f.close()
o.close()
