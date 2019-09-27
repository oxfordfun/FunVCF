#! /bin/bash

# Test cpp binary
echo "Testing CPP binary: vcf-cutter"
../bin/vcf-cutter  <../data/test.vcf > test_new.vcf 

echo "Checking ......"
output=$(diff test_new.vcf ../data/test_new.vcf)

if [ "$output" = "" ]
then
  echo "Test pass! The output file is same as expected."
fi

rm "test_new.vcf"