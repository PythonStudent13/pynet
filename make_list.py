#!/usr/bin/env python

#Import interpreters
import yaml
import json

#Create list with a few keys
new_list = range(8)
new_list.append('wahtever')
new_list.append('hello')
new_list.append({})
new_list[-1]['ip_addr'] = '72.82.92.102'
new_list[-1]['attribs'] = range(7)
print "###################################"
print "Programmatically set new list looks like:"
print new_list
print "###################################"

#Output YAML format to file and screen
print "Writing YAML format filename: yaml_list.yml"
with open("yaml_list.yml", "w") as f:
	f.write(yaml.dump(new_list, default_flow_style=False))
with open("yaml_list.yml") as f:
	new_list = yaml.load(f)
from pprint import pprint as pp
pp(new_list)
print "###################################"

#Output JSON format to file and screen
print "Writing JSON format filename: json_list.json"
with open("json_list.json", "w") as f:
	json.dump(new_list, f)
print "It looks like:"
with open("json_list.json") as f:
	new_list = json.load(f)
pp(new_list)
print "###################################"

#Complete
print "All done!"
