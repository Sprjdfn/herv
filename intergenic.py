import re

link = {"1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "11":11, "12":12, "13":13, "14":14, "15":15, "16":16, "17":17, "18":18, "19":19, "20":20, "21":21, "22":22, "X":23, "Y":24, "M":25}

class op:
    def __init__(self, _id, _chr, _pos, _type):
        self.id = _id
        self.chr = _chr
        self.pos = int(_pos)
        self.type = _type
    def __lt__(self, other):
        if (self.chr != other.chr):
            return link[self.chr[3:]] < link[other.chr[3:]]
        if (self.pos != other.pos):
            return self.pos < other.pos
        return self.type < other.type

gencodefile = open("../data/genes/gencode/gencode.v22.sorted.gff3", "r")
oplist = []

while True:
    line = gencodefile.readline()
    if (line == ""):
        break
    items = re.split(r"\t", re.sub(r"\n", "", line))
    oplist.append(op("ENSG", items[0], items[3], 1))
    oplist.append(op("ENSG", items[0], items[4], 2))

gencodefile.close()

ervfile = open("../data/genes/HERVd/entities.tsv", "r")

ervlist = dict()

while True:
    line = ervfile.readline()
    if (line == ""):
        break
    items = re.split(r"\t", re.sub(r"\n", "", line))
    #print(items[10], items[11], items[12])
    items[11] = int(items[11]) + 1
    items[12] = int(items[12]) + 1
    oplist.append(op(items[1], items[10], items[11], 3))
    oplist.append(op(items[1], items[10], items[12], 4))
    if(items[13] == "C"):
        items[13] = "-"
    ervlist[items[1]] = [1, items]

print(len(ervlist))

ervfile.close()

print(len(oplist))

oplist.sort()

sta = 0
stb = 0
blist = []

for tmp in oplist:
    if (tmp.type == 1):
        sta = sta + 1
        if (stb != 0):
            for tmp in blist:
                ervlist[tmp][0] = 0
    elif (tmp.type == 2):
        sta = sta - 1
    elif (tmp.type == 3):
        stb = stb + 1
        blist.append(tmp.id)
        if (sta != 0):
            ervlist[tmp.id][0] = 0
    elif (tmp.type == 4):
        stb = stb - 1
        blist.remove(tmp.id)
    
print(sta)

outfile = open("../data/genes/HERVd/intergenic1.gtf", "w")

for tmp in ervlist:
    if (ervlist[tmp][0] == 1):
        outfile.write("%s\tENSEMBL\texon\t%s\t%s\t.\t%s\t.\tgene_id \"%s\"; transcript_id \"%sT1\";\n" % (ervlist[tmp][1][10], ervlist[tmp][1][11], ervlist[tmp][1][12], ervlist[tmp][1][13], ervlist[tmp][1][1], ervlist[tmp][1][1]))

outfile.close()