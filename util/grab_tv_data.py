__author__ = 'mmoutenot'
import urllib2
from xml.dom.minidom import parse, parseString



def getText(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return ''.join(rc)


apikey="CAE9400599938D0E"

xml_mirrors = []
banner_mirrors = []
zip_mirrors = []
response_mirrors = urllib2.urlopen('http://www.thetvdb.com/api/'+apikey+'/mirrors.xml')
mirror_xml = response_mirrors.read()
mirror_dom = parseString(mirror_xml)

mirrors = mirror_dom.getElementsByTagName("Mirror")
for mirror in mirrors:
    mirror_path = getText(mirror.getElementsByTagName("mirrorpath")[0].childNodes)
    type_mask   = getText(mirror.getElementsByTagName("typemask")[0].childNodes)
    if  type_mask == '7':
        xml_mirrors.append(mirror_path)
        banner_mirrors.append(mirror_path)
        zip_mirrors.append(mirror_path)
    if mirror_path == '6':
        banner_mirrors.append(mirror_path)
        zip_mirrors.append(mirror_path)
    if mirror_path == '5':
        xml_mirrors.append(mirror_path)
        zip_mirrors.append(mirror_path)
    if mirror_path == '4':
        zip_mirrors.append(mirror_path)
    if mirror_path == '3':
        xml_mirrors.append(mirror_path)
        banner_mirrors.append(mirror_path)
    if mirror_path == '2':
        banner_mirrors.append(mirror_path)
    if mirror_path == '1':
        xml_mirrors.append(mirror_path)

xml_mirror = xml_mirrors[0]
banner_mirror = banner_mirrors[0]
zip_mirror = zip_mirrors[0]

response_previous_time = urllib2.urlopen('http://www.thetvdb.com/api/Updates.php?type=none')
previous_time = response_previous_time.read()

show_list_file = open('tv_names.txt')

show_list = []
for line in show_list_file:
    show_list.append(line.rstrip())

show_info_list = []
for show in show_list:
    try:
        show_info = urllib2.urlopen('http://www.thetvdb.com/api/GetSeries.php?seriesname=' + str(show))
        show_info_list.append(show_info.read())
    except:
        print(str(show)+ " FAILED")

print(show_info)

