#!/usr/bin/env python

# Python for Network Engineers
# Class 1 - Lab 8

from ciscoconfparse import CiscoConfParse
cisco_cfg = CiscoConfParse("cisco_ipsec.txt")
print "Parent Match:"
crypto_map=cisco_cfg.find_objects_w_child(parentspec=r"^crypto map CRYPTO",childspec=r"match address")
for obj in crypto_map:
	print obj.text

print "Parent and Child Match:"
for crypto_kids in crypto_map:
	print crypto_kids.text
	for child in crypto_kids.children:
		print child.text
	print

print "All done!"

