import re

infile = open("./share_data/cmp_result.txt", "r")
outfile = open("./share_data/cmp_res_uni_1.txt", "w")

class ans:
    def __init__(self, _id, _erv, _type):
        self.ensgid = _id
        self.erv = _erv
        self.type = _type
    def __repr__(self):
        return "%s\t%s\t%s" % (self.ensgid, self.erv, self.type)

anslist = {}
ensgset = set()
ervset = set()

for i in range(5):
    infile.readline()

for i in range(189099):
    line = re.sub("\n", "", infile.readline())
    ele = re.split(r"~", line)
    items = re.split(r"[\t;=]", ele[0])
    ervi = re.split(r"[\t;]", ele[1])
    id = "%s;%s" % (items[items.index("gene_id") + 1], ervi[1])
    ensgset.add(items[items.index("gene_id") + 1])
    ervset.add(ervi[1])
    if id in anslist:
        anslist[id].type = "%s;%s" % (anslist[id].type, items[2])
    else:
        anslist[id] = ans(items[items.index("gene_id") + 1], ervi[1], items[2])

outfile.write("###########################################\nERV in gencode annotation: %d\n" % len(anslist))
for an in anslist:
    outfile.write("%s\n" % anslist[an].__repr__())

outfile.write("###########################################\nTotal ENSGID: %d, Total ERVID: %d\n" % (len(ensgset), len(ervset)))
for ensg in ensgset:
    outfile.write("%s\n" % ensg)
outfile.write("*******************\n")
for erv in ervset:
    outfile.write("%s\n" % erv)

ensgset.clear()
ervset.clear()

for i in range(2):
    infile.readline()

anslist.clear()
for i in range(13819):
    line = re.sub("\n", "", infile.readline())
    ele = re.split(r"~", line)
    items = re.split(r"[\t;=]", ele[0])
    ervi = re.split(r"[\t;]", ele[1])
    id = "%s;%s" % (items[items.index("gene_id") + 1], ervi[1])
    ensgset.add(items[items.index("gene_id") + 1])
    ervset.add(ervi[1])
    if id in anslist:
        anslist[id].type = "%s;%s" % (anslist[id].type, items[2])
    else:
        anslist[id] = ans(items[items.index("gene_id") + 1], ervi[1], items[2])

outfile.write("###########################################\ngencode annotation in ERV: %d\n" % len(anslist))
for an in anslist:
    outfile.write("%s\n" % anslist[an].__repr__())

outfile.write("###########################################\nTotal ENSGID: %d, Total ERVID: %d\n" % (len(ensgset), len(ervset)))
for ensg in ensgset:
    outfile.write("%s\n" % ensg)
outfile.write("*******************\n")
for erv in ervset:
    outfile.write("%s\n" % erv)

ensgset.clear()
ervset.clear()

for i in range(2):
    infile.readline()

anslist.clear()
for i in range(15473):
    line = re.sub("\n", "", infile.readline())
    ele = re.split(r"~", line)
    items = re.split(r"[\t;=]", ele[0])
    ervi = re.split(r"[\t;]", ele[1])
    id = "%s;%s" % (items[items.index("gene_id") + 1], ervi[1])
    ensgset.add(items[items.index("gene_id") + 1])
    ervset.add(ervi[1])
    if id in anslist:
        anslist[id].type = "%s;%s" % (anslist[id].type, items[2])
    else:
        anslist[id] = ans(items[items.index("gene_id") + 1], ervi[1], items[2])

outfile.write("###########################################\ngencode annotation cross with ERV: %d\n" % len(anslist))
for an in anslist:
    outfile.write("%s\n" % anslist[an].__repr__())


outfile.write("###########################################\nTotal ENSGID: %d, Total ERVID: %d\n" % (len(ensgset), len(ervset)))
for ensg in ensgset:
    outfile.write("%s\n" % ensg)
outfile.write("*******************\n")
for erv in ervset:
    outfile.write("%s\n" % erv)

outfile.close()