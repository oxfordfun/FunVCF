Run with C++
============

1. Install nextflow if not exists, go Nextflow_.

.. _Nextflow: https://www.nextflow.io/docs/latest/getstarted.html

2. Run test 

.. code-block:: bash

    cd tests
    sh test-cpp.sh

3. Run test with Nextflow (files in folder data)

.. code-block:: bash

    nextflow run vcf-cpp.nf --input data/ --pattern *.vcf --output tests-cpp -profile standard
