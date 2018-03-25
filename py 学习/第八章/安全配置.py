#不安全
from xml.etree.ElementTree import parse
et = parse(xmlfile)

#受保护
from defusedxml.ElementTree import parse
et = parse(xmlfile)