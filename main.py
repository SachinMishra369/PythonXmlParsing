# import xml.etree.ElementTree as ET
# data = '''
# <person>
#   <name>Chuck</name>
#   <phone type="intl">
#     +1 734 303 4456
#   </phone>
#   <email hide="yes" />
# </person>'''

# data = '''
# <stuff>
#   <users>
#     <user x="2">
#       <id>001</id>
#       <name>Chuck</name>
#     </user>
#     <user x="7">
#       <id>009</id>
#       <name>Brent</name>
#     </user>
#   </users>
# </stuff>'''

# tree=ET.fromstring(data)
# lst=tree.findall('users/user')
# print('User count:', len(lst))
# for l in lst:
#   print('Id:',l.find('id').text)
#   print('Name:',l.find('name').text)
#   print('User x:',l.get('x'))
# print(tree.find('stuff/users/user/id'))
# print(tree.find('phone').text)
# print(tree.find('email').get('hide'))
import urllib.request
import xml.etree.ElementTree as ET
fhand = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_724905.xml')
mstr=''
for line in fhand:
    mstr=mstr+line.decode().strip()
tree=ET.fromstring(mstr)
count=list()
lst=tree.findall('comments/comment')
# print(len(count))
for l in lst:
  count.append(int(l.find('count').text))

print(sum(count))