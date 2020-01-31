import numpy

#my_array = numpy.array([ [1, 2], [3, 4] ])

# print("MEANS!")
# print(numpy.mean(my_array, axis = 0))        #Output : [ 2.  3.]
# print(numpy.mean(my_array, axis = 1))        #Output : [ 1.5  3.5]
# # print(numpy.mean(my_array, axis = 2))     # When I add this to the sample code, I get a tuple index out of range
# print(numpy.mean(my_array, axis = None))     #Output : 2.5
# print(numpy.mean(my_array))                  #Output : 2.5


# Oooooo kkkkkk. So I'm re-learning a lot of statistics stuff here with this Stats 001 course. 
# Here are some interesting notes from my google rabbit hole that is Means/Axis/etc:

# Flattening an array: if passing a multi-dimensional array (like the one above) then the numpy
# mean will flatten it. In other words, flattening this:
# [ [1, 2], [3, 4], [3, 3] ]
# Should become this:
# [ 1, 2, 3, 4, 3, 3 ]

# Now for Axis. The "axis" parameter noted here:
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html
# means something that I either don't remember or have never heard. Everyone's talking about "axis this" and "axis that"
# and I couldn't seem to find a valid definition
# SO while I foray once more into something that feels like it's high school statistics, this is what "axis" means:

# Given the following numpy array: 
# numpy.array([ [1, 2], [3, 4], [3, 3] ])
# AXIS refers to the nth element in each multidemensional array. For example.

# numpy.mean(my_array, axis = 0) 
# will process on the quoted values:
# [ ["1", 2], ["3", 4], ["3", 3] ]
# and...
# numpy.mean(my_array, axis = 1) 
# will process on the quoted values:
# [ [1, "2"], [3, "4"], [3, "3"] ]
# etc.
# The important thing to remember here is without specifying the axis, mean flattens the entire tuple. 

# MOVING ONNNNNNNN TO VARIANCES

# print("VARIANCES!")
# print(numpy.var(my_array, axis = 0))         #Output : [ 1.  1.]
# print(numpy.var(my_array, axis = 1))         #Output : [ 0.25  0.25]
# print(numpy.var(my_array, axis = None))      #Output : 1.25
# print(numpy.var(my_array))                   #Output : 1.25

# Welp, here we go back to children's web sites explaining stats concepts. 
# A varienace is defined as: 

# The average of the squared differences from the Mean.
# https://www.mathsisfun.com/data/standard-deviation.html

# Let's use our example with default paramters, which would flatten this and use:
# [ 1, 2, 3, 4 ]

# Essentially you:
# 1) Work out the mean.
# ( 1 + 2 + 3 + 4 ) / 4 = 2.5
# 2) For each number: subtract the Mean and square the result. 
# ( 1 - 2.5 )^2 = -2.25, ( 2 - 2.5 )^2 = -0.25, ( 3 - 2.5 ) = 0.25, ( 4 - 2.5 ) = 2.25
# 3) Then work out the average of those squared differences.
# ( -2.25 + -0.25 + 0.25 + 2.25 ) / 4 = 0
# In retrospect I chose an awful example because the variance is zero. 

# That was fun. Now for Standard Deviation.

# print("STANDARD DEVIATIONS!")
# print(numpy.std(my_array, axis = 0))         #Output : [ 1.  1.]
# print(numpy.std(my_array, axis = 1))         #Output : [ 0.5  0.5]
# print(numpy.std(my_array, axis = None))      #Output : 1.11803398875
# print(numpy.std(my_array))                   #Output : 1.11803398875

# Super easy. Just the root of the variance. Neato.

# After stuggling a bit more with what a multidimensional array IS and how it is DEFINED, this helped a lot:

# https://www.mathworks.com/help/matlab/math/multidimensional-arrays.html

# Now let's, uh... get to the excersise. 



import numpy
# see below for my frustrations for why this is necessary, and I thought
# it was a dtype problem. 
numpy.set_printoptions(legacy='1.13')

def inputToIntArray(entry):
    entry = entry.split(" ")
    return list(map(int, entry)) 

# Just 
rayTable = inputToIntArray(input())

# Initialize the empty numpy array according to the first entry.
# Something is wrong here. When I input this in and run it, the 
# online compiler rounds to the 12th mantissa... which is super wierd
# considering float32 comes out too long and float16 is far too short. 
# the result it: 11803398875 where my code spits out: 118033988749895
finalArray = numpy.zeros(rayTable)

# I can't help but think that there is a better way to keep
# prompting until the input is done... but let's see whats up
for i in range(rayTable[0]):
    entry = inputToIntArray(input())
    # I spent a whole day trying to get the below to work, only to
    # discover that I could just...
    #finalArray = numpy.append([finalArray], entry, axis=i)
    finalArray[i] = entry

print(numpy.mean(finalArray, axis = 1))
print(numpy.var(finalArray, axis = 0))
print(numpy.std(finalArray))

# It should be noted here that someone else on HR got the following to work:

# n,m = map(int, input().split())
# b = []
# for i in range(n):
#     a = list(map(int, input().split()))
#     b.append(a)
# b = np.array(b)

# Which wrinkles my brain a bit. They added a numpy array to a normal one- looks like I
# need to play around with this some more. I think maybe I was going a bit too
# hard in the numpy world when simpler answers would have worked.