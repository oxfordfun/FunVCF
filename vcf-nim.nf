#! /usr/bin/env nextflow
/*
nextflow run vcf-nim.nf --input /home/docker/Data/vcfs_tests --pattern *.vcf --output /home/docker/Data/vcfs_tests_output
nextflow run vcf-nim.nf --input /home/docker/Data/vcfs_tests --pattern *.vcf.gz --output /home/docker/Data/vcfs_tests_output
*/

params.input = "/home/docker/Data/vcfs_tests/"

params.pattern = "*.vcf.gz"

params.output = "/home/docker/Data/vcfs_tests_output"

vcf_path = params.input + params.pattern

if (params.pattern == "*.vcf.gz"){

gzip_files_channel = Channel.fromPath(vcf_path)

process unzip_vcf {

   tag {gzip_file.getBaseName()}

   input:
   file gzip_file from gzip_files_channel

   output:
   set file("${gzip_file.getBaseName()}.vcf") into vcf_files_channel

   """
   gunzip -c ${gzip_file} > ${gzip_file.getBaseName()}.vcf
   """
}}

if (params.pattern == "*.vcf"){

   vcf_files_channel = Channel.fromPath(vcf_path)
}


process process_vcf {
    echo true
    scratch true

    publishDir "${params.output}", mode: "copy"

    tag {vcf_file.getBaseName()}

    input:
    file vcf_file from vcf_files_channel

    output:
    set val("${vcf_file.getBaseName()}"), file("${(vcf_file.getBaseName())}_new.vcf") into output

    """
    vcfprocessor  ${vcf_file.getBaseName()}.vcf > ${vcf_file.getBaseName()}_new.vcf    
    """
}
