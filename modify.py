from __future__ import print_function
from lxml import etree as ET
parser = ET.XMLParser(remove_blank_text=True) # makes pretty print work
file = '/var/ossec/etc/ossec.conf'
tree = ET.parse(file, parser)
root = tree.getroot()
ip = raw_input("Enter your server's IP:")

for globals in root.findall('global'):
    if(globals.findtext('white_list', None)):
        new_tag = ET.SubElement(globals, 'white_list')
        new_tag.text = ip
        tree.write('/var/ossec/etc/ossec.conf', pretty_print = True)
        print('Saved IP:', ip, 'to white list.')
