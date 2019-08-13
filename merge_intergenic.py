import re

link = {"1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "11":11, "12":12, "13":13, "14":14, "15":15, "16":16, "17":17, "18":18, "19":19, "20":20, "21":21, "22":22, "X":23, "Y":24, "M":25}

class erv:
    def __init__(self, _id, _chr, _pos, _type, _str):
        self.id = _id
        self.chr = _chr
        self.pos = int(_pos)
        self.type = _type
        self.str = _str
    def __lt__(self, other):
        if (self.chr != other.chr):
            return link[self.chr[3:]] < link[other.chr[3:]]
        if (self.str != other.str):
            return self.str < other.str
        if (self.pos != other.pos):
            return self.pos < other.pos
        return self.type < other.type

ervfile = open("../data/genes/HERVd/intergenic1.gtf", "r")

ervlist = []

while True:
    line = ervfile.readline()
    if (line == ""):
        break
    items = re.split(r"\s", re.sub(r"\n", "", line))
    #print(items[10], items[11], items[12])
    name = re.sub(r"[\";]", "", items[9])
    ervlist.append(erv(name, items[0], items[3], 1, items[6]))
    ervlist.append(erv(name, items[0], items[4], 2, items[6]))

ervfile.close()

print(len(ervlist))

ervlist.sort()

print("sorted.")

sta = 0
stb = 0
nowst = 0
nowid = ""
nowstr = ""
cnt = 0
nnow = 0

outfile = open("../data/genes/HERVd/intergenic_merge.gtf", "w")

for tmp in ervlist:
    nnow += 1
    if (nnow % 1000 == 0):
        print(nnow, cnt)
    if (tmp.type == 1):
        sta = sta + 1
        nowid = "%s_%s" % (nowid, tmp.id)
    elif (tmp.type == 2):
        sta = sta - 1
    if (sta != 0 and stb == 0):
        nowst = tmp.pos
        nowchr = tmp.chr
        nowstr = tmp.str
    elif (sta == 0 and stb != 0):
        outfile.write("%s\tENSEMBL\texon\t%s\t%s\t.\t%s\t.\tgene_id \"%s\"; transcript_id \"%sT1\";\n" % (nowchr, nowst, tmp.pos, nowstr, nowid, nowid))
        nowid = ""
        cnt += 1
    stb = sta
    
print(cnt)
outfile.close()