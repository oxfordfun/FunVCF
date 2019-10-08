Run with Python
===============

We use python library, vcfpy_.

.. _vcfpy: https://pypi.org/project/vcfpy/


1. Get Docker from Docker Hub 

.. code-block:: bash

    docker pull oxfordmmm/funvcf:v0.1.0

2. Install nextflow if not exists, go Nextflow_.

    .. _Nextflow: https://www.nextflow.io/docs/latest/getstarted.html


3. Run tests

.. code-block:: bash

    nextflow run vcf-python.nf --input data/ --pattern *.vcf --output tests-python -profile docker
    nextflow run vcf-python.nf --input data/ --pattern *.vcf --output tests-python -with-singularity funvcf-v0.1.0.img

