#!/usr/bin/python

import sys

#This is a list
simple_list = {'wayne' : 'knows some python', 'david' : 'is learning some python'}

#using string formatting
print 'hello you called a program called %s and you passed in %s as an argument' % (sys.argv[0], sys.argv[1])

#not using string formatting
print 'hello you called a program called ' + sys.argv[0] + ' and you passed in ' + sys.argv[1] + ' as an argument'

#this is annoying 
print 'Wayne ' + simple_list['wayne'] + ' and David ' + simple_list['david'] 

#this is simpler
print 'Wayne %s and David %s' % ( simple_list['wayne'], simple_list['david'])
