#!/usr/bin/env python

# Python for Network Engineers
# Class 1 - Lab 9

print "\nParent and Child Matching entries with PFS group 2:"
from ciscoconfparse import CiscoConfParse
parse = CiscoConfParse("cisco_ipsec.txt")
group= parse.find_objects_w_child(parentspec=r"^cyprto map CRYPTO", childspec=r"pfs group2")
for entry in group:
	print "  {0}".format(entry.text)
print
print "All done!"

