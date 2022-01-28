import this


k = open("sortOutput01.txt", "r")  # open file, read only
t = open("reduceOutput01.txt", "w")  # open file, write
lines = k.readlines()

for line in lines:
   data = line.strip().split('\t')
   store, amount = data

   if store != thisKey:
       if thisKey:
           # output the last key value pair result
           t.write(thisKey + '\t' + str(thisValue)+'\n')

        # start over when changing keys
       thisKey = store
       thisValue = 0.0
   thisValue += float(amount)

k.close()
t.close()