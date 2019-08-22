#! /usr/bin/env nextflow
/* 
nextflow run vcf-slimmer.nf --input /home/docker/Data/vcfs_tests --pattern *.vcf --output /home/docker/Data/vcfs_tests_output
nextflow run vcf-slimmer.nf --input /home/docker/Data/vcfs_tests --pattern *.vcf --output /home/docker/Data/vcfs_tests_output -profile docker
nextflow run vcf-slimmer.nf --input /home/docker/Data/vcfs_tests --pattern *.vcf --output /home/docker/Data/vcfs_tests_output -profile singularity
nextflow run vcf-slimmer.nf --input /home/docker/Data/vcfs_tests --pattern *.vcf --output /home/docker/Data/vcfs_tests_output -with-singularity /data/images/funvcf-v0.1.0.img
*/

params.input = "/home/docker/Data/vcfs_tests/"

params.pattern = "*.vcf"

params.output = "/home/docker/Data/vcfs_tests_output"

vcf_path = params.input + params.pattern

vcf_files_channel = Channel.fromPath(vcf_path)

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
    vcf-cutter.py -i ${vcf_file.getBaseName()}.vcf -o ${vcf_file.getBaseName()}_new.vcf
    """
}
