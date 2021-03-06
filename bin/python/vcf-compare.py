 
import vcfpy
import os
import csv
import time
import argparse
import json
from pathlib import Path

def sub_to_string(substitution):
    '''
    convert vcfpy.Substitution to string
    '''
    result = []
    for sub in substitution:
        result.append(sub.value)
    return "".join(result)

def write_csv(rows, csv_file):
    '''
    write dictionary(rows) to file(csv_file)
    '''
    header = 'POS', 'REF', 'ALT1', 'ALT2'
    with open(csv_file, 'w') as f:
        w = csv.writer(f)
        w.writerow(header)
        for row in rows:
            w.writerow(row)
    
def readVCF(input_vcf):
    '''
    Read a VCF file, return POS as set, ALT and REF as dictionary
    '''
    reader = vcfpy.Reader.from_path(input_vcf)
    header = reader.header
    POS = set()
    REF = {}
    ALT = {}
    count = 0
    for record in reader:
        POS.add(record.POS)
        ALT[str(record.POS)] = sub_to_string(record.ALT)
        REF[str(record.POS)] = record.REF
    return (POS, REF, ALT)

def compareVCFs(vcf_1, vcf_2):
    '''
    Compare 2 VCFs, reporting differnt positions and different ALTs
    Return dictionary : {'POS': [REF, ALT1, ALT2]}
    '''
    pos1, ref1, alt1 = readVCF(vcf_1)
    pos2, ref2, alt2 = readVCF(vcf_2)

    all_pos = sorted(pos1 | pos2)
    both_pos = pos1 & pos2
    sym_diff = pos1 ^ pos2
    
    diff_all = {}
    for pos in all_pos:
        if pos in sym_diff: # report all symmatric differences
            if pos in pos1:
                alt = ref1[str(pos)], alt1[str(pos)], ""
            if pos in pos2:
                alt = ref2[str(pos)], "" , alt2[str(pos)]
            diff_all[str(pos)] = alt
        else:  # only report the different ALT of intersection
            if alt1[str(pos)] != alt2[str(pos)]:
                alt = ref1[str(pos)], alt1[str(pos)], alt2[str(pos)]
                diff_all[str(pos)] = alt
    
    stats = {}  
    stats['all_pos']  = len(all_pos)
    stats['both_pos'] = len(both_pos)
    stats['diff1_2']  = len(pos1.difference(pos2))
    stats['diff2_1']  = len(pos2.difference(pos1))
    stats['sym_diff'] = len(sym_diff)
    stats['all_diff'] = len(diff_all)

    return diff_all, stats


if __name__ == "__main__":
    '''
    Compare 2 VCFs, reporting differnt positions and different ALTs, output to stdout and file
    python3 bin/vcf-compare.py -f1 data/test.vcf -f2 data/test_new.vcf -o /tmp/output.csv
    '''
    parser = argparse.ArgumentParser(description="VCF reader")
    parser.add_argument("-f1", dest="vcf_1", required=True, help="first vcf file ")
    parser.add_argument("-f2", dest="vcf_2", required=True, help="second vcf file")
    parser.add_argument("-o", dest="output", required=True, help="output files")

    args = parser.parse_args()
    diff_all, stats = compareVCFs(args.vcf_1, args.vcf_2)
    print(json.dumps(stats))

    rows = []
    for key in diff_all:
        row = key, diff_all[key][0], diff_all[key][1], diff_all[key][2]
        rows.append(row)
    write_csv(rows,args.output)