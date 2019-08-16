import re

infile = open("../data/tumor/AML/AML_abu_cutoff.gtf", "r")

dic = dict()

flag = dict()

while True:
    line = re.sub(r"[\n;\"]", "", infile.readline())
    if (line == ""):
        break
    items = re.split(r"[\s]", line)
    dic[items[13]] = "AML\t%s\t%s\t" % (items[17], items[19])

infile.close()

infile = open("../data/tumor/breast/breast_abu_cutoff.gtf", "r")

while True:
    line = re.sub(r"[\n;\"]", "", infile.readline())
    if (line == ""):
        break
    items = re.split(r"[\s]", line)
    if (items[13] in dic):
        dic[items[13]] = "%sbreast\t%s\t%s\t" % (dic[items[13]], items[17], items[19])
    else:
        dic[items[13]] = "breast\t%s\t%s\t" % (items[17], items[19])

infile.close()
infile = open("../data/tumor/lung/lung_abu_cutoff.gtf", "r")

while True:
    line = re.sub(r"[\n;\"]", "", infile.readline())
    if (line == ""):
        break
    items = re.split(r"[\s]", line)
    if (items[13] in dic):
        dic[items[13]] = "%slung\t%s\t%s\t" % (dic[items[13]], items[17], items[19])
    else:
        dic[items[13]] = "lung\t%s\t%s\t" % (items[17], items[19])

infile.close()
infile = open("../data/tumor/lung_normal/lung_normal_abu_cutoff.gtf", "r")

while True:
    line = re.sub(r"[\n;\"]", "", infile.readline())
    if (line == ""):
        break
    items = re.split(r"[\s]", line)
    if (items[13] in dic):
        dic[items[13]] = "%slung_normal\t%s\t%s\t" % (dic[items[13]], items[17], items[19])
    else:
        dic[items[13]] = "lung_normal\t%s\t%s\t" % (items[17], items[19])

infile.close()
outfile = open("../data/tumor/res_list.tsv", "w")

for i in dic:
    outfile.write("%s\t" % i)
    items = re.split(r"\t", dic[i])
    if ("AML" in items):
        id = items.index("AML")
        outfile.write("%s\t%s\t" % (items[id+1], items[id+2]))
    else:
        outfile.write("0\t0\t")
    if ("breast" in items):
        id = items.index("breast")
        outfile.write("%s\t%s\t" % (items[id+1], items[id+2]))
    else:
        outfile.write("0\t0\t")
    if ("lung" in items):
        id = items.index("lung")
        outfile.write("%s\t%s\t" % (items[id+1], items[id+2]))
    else:
        outfile.write("0\t0\t")
    if ("lung_normal" in items):
        id = items.index("lung_normal")
        outfile.write("%s\t%s\t" % (items[id+1], items[id+2]))
    else:
        outfile.write("0\t0\t")
    outfile.write("\n")

outfile.close()