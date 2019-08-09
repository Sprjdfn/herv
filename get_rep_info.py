import requests
import xml.dom.minidom
import re

outfile = open("./data/genes/HERVd/repeats.txt", "w")

page = 1
while page <= 29031:
    print("parsing page %s:\ngetting html..." % page, end='')
    url = "https://herv.img.cas.cz/repeats?page=%d" % page
    r = requests.get(url)
    #outfile.write(r.text[r.text.find("<tbody>"):r.text.find("</tbody>")+8])
    #outfile.close()
    print("done.\nparsing html...", end='')
    DOMTree = xml.dom.minidom.parseString(r.text[r.text.find("<tbody>"):r.text.find("</tbody>")+8])
    collection = DOMTree.documentElement
    for rep in collection.getElementsByTagName("tr"):
        tds = rep.getElementsByTagName("td")
        outfile.write("%s\t" % tds[0].childNodes[0].data)
        outfile.write("%s\t" % tds[1].childNodes[0].childNodes[0].data)
        outfile.write("%s\t" % tds[2].childNodes[0].childNodes[0].data)
        outfile.write("%s\t" % tds[3].childNodes[0].data)
        outfile.write("%s\t" % tds[4].childNodes[0].data)
        outfile.write("%s\t" % re.sub(",", "", tds[5].childNodes[0].data))
        outfile.write("%s\t" % re.sub(",", "", tds[6].childNodes[0].data))
        outfile.write("%s\t" % tds[7].childNodes[0].data)
        outfile.write("%s\t" % tds[8].childNodes[0].data)
        try:
            outfile.write("%s\n" % tds[9].childNodes[0].data)
        except:
            outfile.write("\n")
    print("done.")
    page = page + 1

outfile.close()