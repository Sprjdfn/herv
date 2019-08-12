import re

class entities:
    def __init__(self, _id, _ch, _sP, _eP, _ele, _str):
        self.id = _id
        self.ch = _ch
        self.sP = int(_sP)
        self.eP = int(_eP)
        self.ele = _ele
        self.str = _str
    def __repr__(self):
        return "%s\t%s\t%s:%d-%d(%s)" % (self.id, self.ele, self.ch, self.sP, self.eP, self.str)
    def __lt__(self, other):
        if (self.ch != other.ch):
            return self.ch < other.ch
        if (self.sP != other.sP):
            return self.sP < other.sP
        return self.eP < other.eP

entfile = open("./share_data/entities.tsv", "r")
entlist = []

gencodefile = open("./data/genes/gencode/gencode.v22.sorted.gff3", "r")

sn = 0
n = 0
m = 0
nowchr = "chr1"
nextchr = ""
flag = 0

ERV_in_gen_ans = []
gen_in_ERV_ans = []
equal_ans = []
cross_ans = []

lline = ""

while True:
    print("comparing %s..." % nowchr)
    while True:
        line = entfile.readline()
        #if (n < st):
            #n = n + 1
            #continue
        if (line == ""):
            flag = 1
            break
        items = re.split(r"\t", re.sub("\n", "", line))
        entlist.append(entities(items[1], items[10], int(items[11]), int(items[12]), items[13], items[9]))
        n = n + 1
        if (items[10] != nowchr):
            nextchr = items[10]
            break
    entlist.sort()
    while True:
        if (lline == ""):
            line = gencodefile.readline()
        else:
            line = lline
            lline = ""
        m = m + 1
        if (m % 10000 == 0):
            print(m, line)
        if (line == ""):
            break
        if (line[0] == "#"):
            break
        items = re.split(r"\t", re.sub("\n", "", line))
        if (items[0] != nowchr):
            lline = line
            break
        line = re.sub("\n", "", line)
        while len(entlist) and (int(items[3]) > entlist[0].eP):
            del entlist[0]
        for ent in entlist[:-1]:
            #if (int(items[4]) + 23049960 < ent.sP):
            #    break
            if (int(items[4]) < entlist[0].sP):
                #continue
                break
            if (abs(ent.sP - int(items[3])) <= 1 and (ent.sP - int(items[3]) == ent.eP - int(items[4]))):
                equal_ans.append("%s\t*\t%s" % (line, ent.__repr__()))
            elif (ent.sP <= int(items[3]) and ent.eP >= int(items[4])):
                gen_in_ERV_ans.append("%s\t*\t%s" % (line, ent.__repr__()))
            elif (ent.sP >= int(items[3]) and ent.eP <= int(items[4])):
                ERV_in_gen_ans.append("%s\t*\t%s" % (line, ent.__repr__()))
            elif ((ent.sP < int(items[3]) and ent.eP > int(items[3])) or (ent.sP < int(items[4]) and ent.eP > int(items[4]))):
                cross_ans.append("%s\t*\t%s" % (line, ent.__repr__()))
    print("%d*%d.done." % (n, m))
    if (flag == 1):
        break
    entlist = entlist[-1:]
    nowchr = nextchr
    n = m = 0

entfile.close()
gencodefile.close()

outfile = open("share_data/cmp_result.txt", "w")
outfile.write("###########################################\n")
outfile.write("A * B to show relation of A and B\n")
outfile.write("ERV equal gencode annotation: %d\n" % len(equal_ans))
for ans in equal_ans:
    outfile.write("%s\n" % ans)
outfile.write("###########################################\n")
outfile.write("ERV in gencode annotation: %d\n" % len(ERV_in_gen_ans))
for ans in ERV_in_gen_ans:
    outfile.write("%s\n" % ans)
outfile.write("###########################################\n")
outfile.write("gencode annotation in ERV: %d\n" % len(gen_in_ERV_ans))
for ans in gen_in_ERV_ans:
    outfile.write("%s\n" % ans)
outfile.write("###########################################\n")
outfile.write("gencode annotation cross with ERV: %d\n" % len(cross_ans))
for ans in cross_ans:
    outfile.write("%s\n" % ans)
outfile.close()