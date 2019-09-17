# FunVCF
Fun Tools for VCF
## VCF Cutter
VCF cutter reads a VCF and writes a new VCF which only contains SNV.

### Run with Python
#### 1. Get Docker from Docker Hub 
```bash
   docker pull oxfordmmm/funvcf:v0.1.0
```
#### 2. Install nextflow if not exists
See [Nextflow Documentation](https://www.nextflow.io/docs/latest/getstarted.html)

#### 3. Run tests
```bash
nextflow run vcf-python.nf --input data/ --pattern *.vcf --output tests-python -profile docker
nextflow run vcf-python.nf --input data/ --pattern *.vcf --output tests-python -with-singularity funvcf-v0.1.0.img
```

### Run with C++
#### 1. Install nextflow if not exists
See [Nextflow Documentation](https://www.nextflow.io/docs/latest/getstarted.html)

#### 2. Run tests
```bash
nextflow run vcf-cpp.nf --input data/ --pattern *.vcf --output tests-cpp -profile standard
```
