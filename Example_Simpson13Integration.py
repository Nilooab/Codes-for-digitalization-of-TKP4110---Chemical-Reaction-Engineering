import numpy as np
import matplotlib.pyplot as plt
# #######################################################################
# # Chemical Reaction Engineering – Integration with Simpson's 1/3 Rule
# #######################################################################

# #######################################################################
# #summary:  Numerical integration
# #contact:  niloufarabtahi@gmail.com
# #requires:  Python 3 or higher
# #since: 8.11.21
# #version: 0.1
# #change: 
# #author: Niloufar Abtahi
# #copyright: 2021 Niloufar Abtahi A All rights reserved.
# #--author--= ’ Niloufar Abtahi’
# #######################################################################

#######################################################################
# Input Parameters and data
#######################################################################
n = 21       # total number of points which is an odd number(number of results for xfinal)
x0 = 0.0     #Initial conversion
# #####################################################################

# #####################################################################
# # Define function to integrate (input for this function)
# #####################################################################
def function(x):
    f = x**5+x/(1 + x**5 + x**3)
    return f

#####################################################################


#####################################################################
# Numerical Integration for implementing Simpson's 1/3
#####################################################################
def simpson(xn):
    x = np.linspace(x0,xn,n)
    h = (xn-x0)/n                           # calculating step size
    f = np.zeros(len(x))                         #pre  allocation f
    fsimpson = np.zeros(len(x))
    for i in range(0,n):
        f[i] = function(x[i])
        if i == 0:
              fsimpson[i] = f[i]
        elif i == n:
             fsimpson[i] = f[i]
        elif (-1)**i < 0:                         # for odd number
             fsimpson[i] = 4*f[i]  
        else:
             fsimpson[i] = 2*f[i]                 # for even number    
    Result = (h/3)*sum(fsimpson)
    return Result          
#####################################################################

#####################################################################
# Table of Data (Results)
#####################################################################
print('='*35)
print('|      X       |         f        |')
print('='*35)
xfinal=np.linspace(1.0,10.0,n)
f = np.zeros(n)                   # Defining the pre allocation of I
for i in range(0,n):
    xfnow = xfinal[i]
    f[i] = simpson(xfnow)
    print('|%14.2f| %17.2f|' %(xfnow,f[i]))    
print('='*35)
#####################################################################

#####################################################################
#Graphical Results in matplotlib
#####################################################################
plt.plot( xfinal, f, '-r')
plt.xlabel('x')                                 # naming the x axis
plt.ylabel('function(x)')                       # naming the y axis
plt.title('Example of Graphical Result')        # giving a title to my graph
plt.savefig('Exercise.png')                     # save the plot as a file
plt.show()                                      # function to show the plot
