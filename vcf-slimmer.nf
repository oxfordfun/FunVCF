#! /usr/bin/env nextflow

params.input_folder = "/home/docker/Data/vcfs_tests"

params.output_folder = "/home/docker"

vcf_files_channel = Channel.fromPath(params.input_folder)

process process_vcf {
    echo true

    publishDir "${params.output_folder}", mode: "copy"

    tag {vcf_file.getBaseName()}

    input:
    file vcf_file from vcf_files_channel

    output:

    """
    vcf-reader.py ${param.input_folder} ${params.output_folder}
    """

}
