#!/usr/bin/env python3
 
import vcfpy
import os
import csv
import time

def write_dict(dict_to_dump, csv_file):
    with open(csv_file, 'w') as f:
        w = csv.writer(f)
        w.writerows(dict_to_dump.items())

def files_in_path(path):
    vcfs = []
    for root, directories, files in os.walk(path):
        print(directories)
        for file in files:
            if '.vcf' in file:
                vcfs.append(os.path.join(root, file)) 
    return vcfs

def readVCF(input_vcf):
    reader = vcfpy.Reader.from_path(input_vcf)
    header = reader.header
    new_record = []
    count = 0
    for record in reader:
        if record.ALT == []:
            continue
        new_record.append(record)
        count += 1
        line = [record.CHROM, record.POS, record.REF]
        line += [alt.value for alt in record.ALT]
        line += [call.data.get('GT') or './.' for call in record.calls]
    return (input_vcf, count, header, new_record)

def writeVCF(output_vcf, header, records):
    writer = vcfpy.Writer.from_path(output_vcf, header)
    for record in records:
        writer.write_record(record)
    
if __name__ == '__main__':
    #vcfs = files_in_path('/home/compass/Data/vcfs_test')
    
    vcfs = files_in_path('/home/compass/Data/vcfs_compass')
    print(vcfs)
    stats = {}
    print(stats)
    for vcf in vcfs:
        new_vcf = 'new_' + vcf
        name, count, header, records = readVCF(vcf)
        stats[name] = count
        writeVCF(new_vcf, header, records)
    write_dict(stats,'/home/compass/Data/vcfs_compass/stats.csv')