import re

infile = open("./data/genes/gencode/gencode.v22.annotation.gff3", "r")
outfile = open("./data/genes/gencode/gencode.v22.sorted.gff3", "w")

link = {"1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "11":11, "12":12, "13":13, "14":14, "15":15, "16":16, "17":17, "18":18, "19":19, "20":20, "21":21, "22":22, "X":23, "Y":24, "M":25}

class a:
    def __init__(self, _chr, _sP, _eP, _s):
        self.chr = _chr
        self.sP = int(_sP)
        self.eP = int(_eP)
        self.s = _s
    def __lt__(self, other):
        if (self.chr != other.chr):
            return link[self.chr[3:]] < link[other.chr[3:]]
        if (self.sP != other.sP):
            return self.sP < other.eP
        return self.eP < other.eP

alist = []

maxlen = 0

while True:
    line = infile.readline()
    if (line == ""):
        break
    if (line[0] == '#'):
        continue
    items = re.split(r"\t", line)
    maxlen = max(maxlen, int(items[4]) - int(items[3]))
    alist.append(a(items[0], items[3], items[4], line))
infile.close()
alist.sort()
for tmp in alist:
    outfile.write(tmp.s)
outfile.close()
print(maxlen)