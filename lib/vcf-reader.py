#!/usr/bin/env python3
 
import vcfpy
import os
import csv

def write_dict(dict_to_dump, csv_file):
    with open(csv_file, 'w') as f:
        w = csv.writer(f)
        w.writerows(dict_to_dump.items())

# def files_in_path(path):
#     vcfs = []
#     for root, directories, files in os.walk(path):
#         for file in files:
#             if '.vcf' in file:
#                 files.append(os.path.join(root, file)) 
#     return vcfs

def readVCF(input_vcf):
    reader = vcfpy.Reader.from_path(input_vcf)
    header = ['CHROM', 'POS','ID', 'REF', 'ALT', 'QUAL','FILTER','INFO','FORMAT'] + reader.header.samples.names
    print('\t'.join(header))

    count = 0
    for record in reader:
        if not record.is_snv():
            continue
        count += 1
        line = [record.CHROM, record.POS, record.REF]
        line += [alt.value for alt in record.ALT]
        line += [call.data.get('GT') or './.' for call in record.calls]
        #print('\t'.join(map(str, line)))
    return (reader.header.samples.names, count)

def writeVCF(output_vcf, header):
    pass
    

if __name__ == '__main__':   
    #vcfs = files_in_path('/home/compass/Data/vcfs_test')
    vcfs = ['/home/compass/Data/vcfs_test/SRR8662666.vcf','/home/compass/Data/vcfs_test/SRR8662667.vcf','/home/compass/Data/vcfs_test/SRR8662668.vcf']
    stats = {}
    print(stats)
    for vcf in vcfs:
        sample, count  = readVCF(vcf)
        print(sample)
        print(count)
        stats[sample[0]] = count
    write_dict(stats,'/home/compass/Data/vcfs_test/stats.csv')
