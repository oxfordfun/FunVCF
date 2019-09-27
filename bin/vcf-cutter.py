#!/usr/bin/env python3
 
import vcfpy
import os
import csv
import time
import argparse
from pathlib import Path

def write_dict(dict_to_dump, csv_file):
    '''
    write dictionary(dict_to_dump) to file(csv_file)
    '''
    with open(csv_file, 'w') as f:
        w = csv.writer(f)
        w.writerows(dict_to_dump.items())

def files_in_path(path):
    '''
    Get a list of vcf files from a given path 
    '''
    vcfs = []
    for root, directories, files in os.walk(path):
        for file in files:
            if '.vcf' in file:
                vcfs.append(os.path.join(root, file)) 
    return vcfs

def readVCF(input_vcf):
    '''
    Read a VCF file, return all the header lines and the record of SNVs
    '''
    reader = vcfpy.Reader.from_path(input_vcf)
    header = reader.header
    new_record = []
    count = 0
    for record in reader:
        if record.ALT == []:
            continue
        new_record.append(record)
        count += 1
    return (input_vcf, count, header, new_record)

def writeVCF(output_vcf, header, records):
    '''
    Write a VCF file, given the header and records
    '''
    writer = vcfpy.Writer.from_path(output_vcf, header)
    for record in records:
        writer.write_record(record)

    
if __name__ == '__main__':
    '''
    python3 -d DIRECTORY-WITH-VCF-FILES -t OUTPUT-DIRECTORY
    python3 -i VCF-FILE -t OUT-VCF-FILE
    '''
    parser = argparse.ArgumentParser(description="VCF reader")

    parser.add_argument("-d", dest="input_directory", required=False, help="input directory")
    parser.add_argument("-t", dest="output_directory", required=False, help="output directory")

    parser.add_argument("-i", dest="input_file", required=False, help="input file")
    parser.add_argument("-o", dest="output_file", required=False, help="output file")

    args = parser.parse_args()
    
    if (args.input_directory and args.output_directory):
        in_vcfs = files_in_path(args.input_directory)
        out_vcfs_path = Path(args.output_directory)
        stats_file = str(out_vcfs_path / 'stats.csv')
        stats = {}
        for vcf in in_vcfs:
            vcf_file = vcf.split('/')[-1]
            new_vcf_file = vcf_file.split('.')[0] + '_new.vcf'
            name, count, header, records = readVCF(vcf)
            writeVCF(str(out_vcfs_path / new_vcf_file), header, records)
        write_dict(stats,stats_file)
    elif (args.input_file and args.output_file):
        name, count, header, records = readVCF(args.input_file)
        writeVCF(args.output_file, header,records)
    else:
        print('======================= Examples of Run =======================')
        print('Batch run')
        print('python3 -d ~/Data/vcfs_tests -t ~/Data/vcfs_tests_slim')
        print('Single run')
        print('python3 bin/vcf-cutter.py -i ~/Data/vcfs_tests/SRR8662666.vcf -o ~/Data/vcfs_tests_slim/SRR8662666_new.vcf')
        print('===============================================================')