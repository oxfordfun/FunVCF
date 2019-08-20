#! /usr/bin/env nextflow
/* 
nextflow run vcf-slimmer.nf --input /home/docker/Data/vcfs_tests --output /home/docker/Data/vcfs_tests_output
nextflow run vcf-slimmer.nf --input /home/docker/Data/vcfs_tests --output /home/docker/Data/vcfs_tests_output -profile docker
*/

params.input = "/home/docker/Data/vcfs_tests"

params.output = "/home/docker/Data/vcfs_tests_output"

vcf_path = params.input + "/*.vcf"

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
    python3 ${SCRIPT}/vcf-reader.py -i ${vcf_file.getBaseName()}.vcf -o ${vcf_file.getBaseName()}_new.vcf
    """
}
