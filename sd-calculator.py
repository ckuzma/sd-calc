#---------------------------------------#
#  Sonority Distance Calculator v.1.0   #
#                                       #
#    Written by Christopher Kuzma       #
#        November 13, 2013              #
#---------------------------------------#

# This program displays the sonority distance between the first
# two letters of each word in two word lists. It then displays
# the minimum and maximum sonority distance of each word, which
# is useful information for helping to determine the minimal /
# maximal sonority distance for each set of words.
#
# In order to run the program, there needs to be two files
# located in the same folder as this program. The first file
# is to be labeled 'data.txt' and needs to be filled with the
# wordlists to be tested. There should be one word per line
# and the lists separated by an empty line between them. The
# second file required should be labeled 'hierarchy.txt' and
# be filled in the according to the to-be-tested sonority
# hierarchy. The first line corresponds with a sonority value
# of 1, the second with 2, and so on.
#
# A word of caution: this program only reads files formatted
# as plain text. It also does not work with anything but
# standard ASCII characters. As such, any 'unusual' character
# should be a common character (numbers work) and a matching
# character should also be placed in the hierarchy file.
#
# Execute this file from the command line. This looks like:
# python sd-calculator.py

# This function will assign sonority values to letters:
def assignSonority(hierarchy,letter):
    x = 0
    while x < len(hierarchy):
        if letter in hierarchy[x]:
            return x
        x+=1

# This function calculates the sonority distance:
def calculateDistance(hierarchy,first,second):
    one = assignSonority(hierarchy,first)
    two = assignSonority(hierarchy,second)
    if one > two:
        return one - two
    if one < two:
        return two - one
    if one == two:
        return 0
    else:
        return 'Something went wrong.'

# This function stores all of the distances calculated and then
# returns those as a list.
def distances(hierarchy,wordlist):
    sdlist = []
    x = 0
    while x < len(wordlist):
        word = wordlist[x]
        word = word[0]
        sdlist.append(calculateDistance(hierarchy,word[0],word[1]))
        x+=1
    return sdlist

# Establish global variables and import text files:
workingData = []
hierarchy = []

rawFile = open('data.txt','r')
while True:
    line = rawFile.readline()
    workingData.append(line)
    if not line:
        break
rawFile.close()

rawFile = open('hierarchy.txt','r')
while True:
    line = rawFile.readline()
    hierarchy.append(line)
    if not line:
        break
rawFile.close()



# Reformat the import of the data set to make it work.
x = 0
while x < len(workingData):
    line = workingData[x]
    line = line.split()
    workingData[x] = line
    x+=1

# Split the data set into two groups, based upon where
# the program finds the first line without any sort of
# data stored in it. This also makes sure not to save
# that blank line.
firstSet = []
secondSet = []
split = 0
x = 0
while x < len(workingData):
    if split == 0 and workingData[x] != []:
        firstSet.append(workingData[x])
    if split == 1 and workingData[x] != []:
        secondSet.append(workingData[x])
    if workingData[x] == []:
        split = 1
    x+=1


# Home stretch! Here's where we actually call the
# functions and then save the lists to some variables
# for easier presentation later.
firstDistances = distances(hierarchy,firstSet)
firstHL = list(firstDistances)
secondDistances = distances(hierarchy,secondSet)
secondHL = list(secondDistances)

# For simplicity's sake, we'll sort the sonority distance
# list copies in order to easily extract the largest and
# smallest values.
firstHL.sort()
secondHL.sort()

# Rather straightforward; time to extract those high and
# low sonority values, and return them.
def highLow(list):
    hl = []
    hl.append(list[0])
    hl.append(list[len(list)-1])
    return hl

# Pesent all the data!
print '\n\nFirst data set:'
print firstDistances
print '[min,max] : ',highLow(firstHL),'\n'
print 'Second data set:'
print secondDistances
print '[min,max] : ',highLow(secondHL),'\n\n'


#---------------------------------------#
# Copyright (C) 2013 Christopher Kuzma  #
# You may use, distribute and modify    #
# this code for personal use, so long   #
# as this original license remains      #
# intact. Any other use requires prior  #
# approval from the copyright holder.   #
#                                       #
#          christopherkuzma.com         #
#---------------------------------------#
