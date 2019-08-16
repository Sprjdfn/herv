import re

name = input()

infile = open("../data/tumor/%s/%s_abu.gtf" % (name, name), "r")
outfile = open("../data/tumor/%s/%s_abu_cutoff.gtf" % (name, name), "w")

infile.readline()
infile.readline()

while True:
    line = infile.readline()
    if (line == ""):
        break
    items = re.split(r"[\s]", re.sub(r"[\";\n]", "", line))
    if ("ref_gene_name" in items and "FPKM" in items):
        if (float(items[items.index("FPKM") + 1]) >= 0.05):
            outfile.write("%s" % line)

infile.close()
outfile.close()