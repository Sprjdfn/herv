import requests;
import re;

downloadlist = open("entities.tsv", "r");

st = int(input());

n = 1;

while True:
    line = downloadlist.readline();
    if (n < st):
        n = n + 1;
        continue;
    print("downloading %d/519060, %f%%" % (n, n / 519060.0 * 100.0));
    items = re.split(r"\t", line);
    url = "https://rest.ensembl.org/sequence/region/human/%s:%s-%s:1?content-type=text/x-fasta" % (items[10], items[11], items[12]);
    r = requests.get(url);
    while (r.content[0] != 62):
        print("error, retry");
        r = requests.get(url);
    with open("./fas/%s.fasta" % items[1], "wb") as fo:
        fo.write(r.content);
    fo.close();
    n = n + 1;

downloadlist.close();