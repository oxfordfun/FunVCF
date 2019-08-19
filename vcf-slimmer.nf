#! /usr/bin/env nextflow

params.input = "/home/docker/Data/vcfs_tests"

params.output = "/home/docker/Data/vcfs_tests_output"

vcf_files_channel = Channel.fromPath(params.input)

process process_vcf {
    echo true
    scratch true

    publishDir "${params.output}", mode: "copy"

    tag {vcf_file.getBaseName()}

    input:
    file vcf_file from vcf_files_channel

    output:

    """
    python3 /home/docker/Code/FunVCF/bin/vcf-reader.py -i ${params.input} -o ${params.output}
    """

}
