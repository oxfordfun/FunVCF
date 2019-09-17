# FunVCF
Fun Tools for VCF
## VCF Cutter
VCF cutter reads a VCF and writes a new VCF which only contains SNV.

### Installation
#### 1. Get Docker from Docker Hub (Only needed to test out python version)
```bash
   docker pull oxfordmmm/funvcf:v0.1.0
```
#### 2. Install nextflow if not exists
See [Nextflow Documentation](https://www.nextflow.io/docs/latest/getstarted.html)

#### 3. Run tests
```bash
nextflow run vcf-slimmer.nf --input tests --pattern *.vcf --output tests -profile docker
```
