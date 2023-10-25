from lxml import etree as ET
#import xml.etree.ElementTree as ET
from datetime import datetime, timedelta

tree = ET.parse("rss.xml")
root = tree.getroot()
channel = root.find('channel')
podcast =  channel.findall('item')

podcast = sorted(podcast, key=lambda i: int(i.find('{http://www.itunes.com/dtds/podcast-1.0.dtd}season').text)*10**4+int(i.find('{http://www.itunes.com/dtds/podcast-1.0.dtd}episode').text))
for i,p in enumerate(podcast):
    mytime = datetime(2015, 1, 1) + timedelta(i) 
    p.find('pubDate').text = mytime.strftime("%a, %d %b %Y %H:%M:%S %z")
ch = ET.SubElement(root, "channel", {})
for e in channel.findall("*"):
    if e.tag != 'item':
        ch.append(e)
root.remove(channel);
ch.extend(podcast)
#ch.find('link').text = "http://example.com"
print(ch.find('title').text)
tree.write("out.xml")
