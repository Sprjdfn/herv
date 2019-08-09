import re

class entity:
    def __init__(self, _id, _ch, _sP, _eP, _str, _ele):
        self.HERVid = _id
        self.chro = _ch
        self.ele = _ele
        self.sP = _sP
        self.eP = _eP
        self.strand = _str
    def __repr__(self):
        return ">%s,%s:%s-%s(%s),%s\n" % (self.HERVid, self.chro, self.sP, self.eP, self.strand, self.ele)
    def __lt__(self, other):
        return self.ele < other.ele

entfile = open("./data/genes/HERVd/entities.tsv", "r")
entlist = []

#st = int(input())

n = 1

while True:
    line = entfile.readline()
    #if (n < st):
        #n = n + 1
        #continue
    if (line == ""):
        break
    items = re.split(r"\t", re.sub("\n", "", line))
    entlist.append(entity(items[1], items[10], int(items[11]), int(items[12]), items[13], items[9]))
    n = n + 1

entfile.close()

entlist.sort()

nowele = entlist[0].ele
elefile = open("./data/genes/HERVd/elements/%s.fa" % entlist[0].ele, "w")

for ent in entlist:
    if (ent.ele != nowele):
        elefile.close()
        nowele = ent.ele
        elefile = open("./data/genes/HERVd/elements/%s.fa" % nowele, "w")
    elefile.write(open("./data/genes/HERVd/entities/%s/%s.fa" % (ent.chro, ent.HERVid), "r").read())
    elefile.write("\n")

elefile.close()