#!//usr/bin/python3
import xmltodict
import json

fd = open('sample.xml', 'r', encoding='utf-8')
doc = xmltodict.parse(fd.read())
docx = fd.readlines()
for i in fd.readlines():
    print(i)

for value in doc['breakfast_menu']['food']:
    print("%s is %s and costs %s" % (value.get('name'), value.get('description'), value.get('price')) )

# Print to console
print(json.dumps(doc, indent=4, sort_keys=False))

# Write to a file
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(doc, f, ensure_ascii=False, indent=4)