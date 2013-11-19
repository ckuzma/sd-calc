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
#

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
