#libraries, need to be installed first
import numpy
import matplotlib.pylab as pylab
import random 

#setting the number of steps
steps = 10000

#creating two array for containing x and y coordinate 
x = numpy.zeros(steps) 
y = numpy.zeros(steps) 

#setting the title of graph (for decoration only)
pylab.title("Result of Random Walk")

for i in range(1,steps):
    #generate random number, i make it from 0 to 100 so that every result will appear in the graph
    rand = random.randint(0,100) 

    #the percentage for each direction is 100/8=12,5%
    if rand>=0 and rand<12.5: #north
        x[i] = x[i-1]
        y[i] = y[i-1]+1
    elif rand>=12.5 and rand<25: #northeast
        x[i] = x[i-1]+1
        y[i] = y[i-1]+1
    elif rand>=25 and rand<37.5: #east
        x[i] = x[i-1]+1
        y[i] = y[i-1]
    elif rand>=37.5 and rand<50: #southeast
        x[i] = x[i-1]+1
        y[i] = y[i-1]-1
    elif rand>=50 and rand<62.5: #south
        x[i] = x[i-1]
        y[i] = y[i-1]-1
    elif rand>=62.5 and rand<75: #southwest
        x[i] = x[i-1]-1
        y[i] = y[i-1]-1
    elif rand>=75 and rand<87.5: #west
        x[i] = x[i-1]-1
        y[i] = y[i-1]
    elif rand>=87.5 and rand<=100: #northwest
        x[i] = x[i-1]-1
        y[i] = y[i-1]+1

    #plot and set the 'color of line to mediumpurple
    print(i,". ",end="")
    print("x = ",x[i],"\n")
    print("      y = ",y[i],"\n")
pylab.plot(x,y,color='mediumpurple')
    
#show the graph using mathplotlib   
pylab.show()
    

