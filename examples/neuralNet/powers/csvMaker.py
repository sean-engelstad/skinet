#file to make the CSV
import random

#goal is list of 0.1^p, 0.2^p, 0.3^p, ..., 1^p for given p
#output = p the power as a float, p in [0,3] range

#open the csv file
f = open("powers.csv", "w")

numSamples = 200
delim = ","

#iterate over each sample
for isample in range(numSamples):
    power = random.random() * 3
    line = ""
    for i in range(10):
        number = (i+1)/10
        print(number)
        result = number ** power
        line += str(round(result, 4))
        line += delim + " "
    print("new line")
    #output is the power
    line += str(power)
    line += "\n"
    f.write(line)

f.close()

    
