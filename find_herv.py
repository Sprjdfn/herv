import re;

infile = open("gencode.v31.annotation.gff3", "r");
outfile = open(".\herv_list.txt", "w");

itemlist = ("gene_id", "gene_name", "chr", "source", "type", "start_position", "end_position", "score", "strand", "phase", "parent", "gene_type", "transcript_id", "gene_status", "transcript_type", "transcript_status", "transcript_name", "level", "transcript_support_level", "tag")

for itemname in itemlist:
    outfile.write("%s, " % itemname);
outfile.write("\n");

while True:
    line = infile.readline();
    if (line == ""):
        break;
    if (re.match(r"#", line) != None):
        continue;
    items = re.split(r"[\t;=]", line);
    #print(items);
    index = items.index("gene_name");
    if (re.search(r"ERV", items[index+1]) == None):
        continue;
    for itemname in itemlist:
        if (itemname in items):
            index = items.index(itemname);
        elif (itemname == "chr"):
            index = -1;
        elif (itemname == "source"):
            index = 0;
        elif (itemname == "type"):
            index = 1;
        elif (itemname == "start_position"):
            index = 2;
        elif (itemname == "end_position"):
            index = 3;
        elif (itemname == "score"):
            index = 4;
        elif (itemname == "strand"):
            index = 5;
        elif (itemname == "phase"):
            index = 6;
        else:
            outfile.write(", ");
            continue;
        value = items[index + 1];
        if (itemlist.count(value) == 0):
            outfile.write("%s, " % re.sub(",", " ", value));
        else:
            outfile.write(", ");
    outfile.write("\n");

infile.close();
outfile.close();