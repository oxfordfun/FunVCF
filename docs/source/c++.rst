Run with C++
============

1. Install nextflow if not exists, go Nextflow_.

.. _Nextflow: https://www.nextflow.io/docs/latest/getstarted.html

2. Run test 

    ``cd tests``

    ``sh test-cpp.sh``

3. Run test with Nextflow (files in folder data)

    ``nextflow run vcf-cpp.nf --input data/ --pattern *.vcf --output tests-cpp -profile standard``