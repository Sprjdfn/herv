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
        if (self.chro != other.chro):
            return self.chro < other.chro
        if (self.sP != other.sP):
            return self.sP < other.sP
        return self.eP < other.eP

rlist = {'a':'t', 'A':'T', 't':'a', 'T':'A', 'c':'g', 'C':'G', 'g':'c', 'G':'C', 'r':'y', 'R':'Y', 'y':'r', 'Y':'R', 'm':'k', 'k':'m', 'M':'K', 'K':'M', 's':'w', 'w':'s', 'S':'W', 'W':'S', 'h':'d', 'd':'h', 'H':'D', 'D':'H', 'b':'v', 'v':'b', 'B':'V', 'V':'B', 'n':'n', 'N':'N'}

def reverse(s):
    s = s[::-1]
    s = list(s)
    for i in range(len(s)):
        s[i] = rlist[s[i]]
    s = ''.join(s)
    return s

def output(file, s):
    n = len(s) // 60
    nowr = 60
    while n > 0:
        file.write("%s\n" % s[nowr - 60 : nowr])
        nowr = nowr + 60
        n = n - 1
    file.write(s[nowr - 60:])

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

nowchr = "chr1"
print("chr1")
chrfile = open("./data/genes/hg38/chr1.fa")
chrfile.readline()
seq = re.sub(r"\s", "", chrfile.readline())
pr = 50
pl = 0
#seq是chr上[pl,pr)的序列，与bed格式相匹配

for ent in entlist:
    if (ent.chro != nowchr):
        chrfile.close()
        nowchr = ent.chro
        chrfile = open("./data/genes/hg38/%s.fa" % nowchr)
        print(nowchr)
        chrfile.readline()
        seq = re.sub(r"\s", "", chrfile.readline())
        pr = 50
        pl = 0
    while (ent.eP >= pr):
        line = re.sub(r"\s", "", chrfile.readline())
        seq = seq + line
        pr = pr + 50
    if (ent.sP > pl):
        seq = seq[ent.sP - pl - 1:]
        pl = ent.sP - 1
    outfile = open("./data/genes/HERVd/entities/%s/%s.fa" % (nowchr, ent.HERVid), "w")
    outfile.writelines(ent.__repr__())
    if (ent.strand == "+"):
        output(outfile, seq[:ent.eP - ent.sP + 1])
    else:
        output(outfile, reverse(seq[:ent.eP - ent.sP + 1]))
    outfile.close()

chrfile.close()