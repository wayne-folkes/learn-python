#!/usr/bin/python

import sys

#using string formatting
print 'hello you called a program called %s and you passed in %s as an argument' % (sys.argv[0], sys.argv[1])

#not using string formatting
print 'hello you called a program called ' + sys.argv[0] + ' and you passed in ' + sys.argv[1] + ' as an argument'
