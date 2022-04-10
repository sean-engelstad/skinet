#file to make the CSV
import random

#goal is to have x, y, z, class data
#class 1 if inside unit sphere x^2+y^2+z^2 leq 1
#class 0 if outside unit sphere

#open the csv file
f = open("ball.csv", "w")

numSamples = 200
delim = ","

#iterate over each sample
for isample in range(numSamples):
    sumSq = 0
    line = ""
    for i in range(3):
        number = random.random() * 1
        sumSq += number**2
        line += str(round(number, 3))
        line += delim + " "
    
    #classify according to inside or outside unit ball
    if (sumSq <= 1):
        classNum = 1
    else:
        classNum = 0
    
    line += str(classNum)
    line += "\n"
    f.write(line)

f.close()

    
