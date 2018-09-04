#!/usr/bin/env python2.7

import sys

def vcf2bed(vcfinput, bedoutput=None):
    lines = open(vcfinput).readlines()
    snps = [l.split()[:2] for l in lines if not l.startswith("#")]
    ## If bedoutput file not passed in, just use the same input, but swap the filetype from vcf to bed
    if not bedoutput:
        bedoutput = vcfinput.split(".")[0] + ".bed"
    with open(bedoutput, 'w') as outfile:
        for snp in snps:
            ## bed is 0 indexed, vcf is 1 indexed
            outfile.write("{}\t{}\t{}\n".format(snp[0], int(snp[1])-1, snp[1]))

if __name__ == "__main__":
    if len(sys.argv) == 3:
        bedoutput = sys.argv[2]
    elif len(sys.argv) == 2:
        bedoutput = sys.argv[1].split(".")[0] + ".bed"
    else:
        sys.exit("vcf2bed requires 2 arguments; input vcf file and optional output bed file")

    vcf2bed(sys.argv[1], bedoutput)
