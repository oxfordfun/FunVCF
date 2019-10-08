Run with Nim
============

nim language can be found here: https://nim-lang.org/

1. Install nextflow if not exists, go Nextflow_.

.. _Nextflow: https://www.nextflow.io/docs/latest/getstarted.html


2. Run test 

.. code-block:: bash

    cd tests
    sh test-nim.sh

3. Run test with Nextflow (files in folder data)

.. code-block:: bash
   
   nextflow run vcf-nim.nf --input data/ --pattern *.vcf --output tests-nim -profile standard
