#!/usr/bin/env python2.7

import sys

def vcf2bed(vcfinput, bedoutput):
    lines = open(vcfinput).readlines()
    snps = [l.split()[:2] for l in lines if not l.startswith("#")]
    with open(bedoutput, 'w') as outfile:
        for snp in snps:
            outfile.write("{}\t{}\t{}\n".format(snp[0], snp[1], int(snp[1])+1))

if __name__ == "__main__":
    if not len(sys.argv) == 3:
        sys.exit("vcf2bed requires 2 arguments; input vcf file, output bed file")
    vcf2bed(sys.argv[1], sys.argv[2])
