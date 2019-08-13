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

entfile = open("../data/genes/HERVd/repeats.txt", "r")
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
    entlist.append(entity(items[2], items[4], int(items[5]), int(items[6]), items[7], items[1]))
    n = n + 1

entfile.close()

entlist.sort()

nowele = entlist[0].ele
elefile = open("../data/genes/HERVd/elements/%s.fa" % entlist[0].ele, "w")

for ent in entlist:
    if (ent.ele != nowele):
        elefile.close()
        nowele = ent.ele
        elefile = open("../data/genes/HERVd/elements/%s.fa" % nowele, "w")
    elefile.write(open("../data/genes/HERVd/repeats/%s/%s_%s(%d-%d).fa" % (ent.chro, ent.HERVid, ent.ele, ent.sP, ent.eP), "r").read())
    elefile.write("\n")

elefile.close()