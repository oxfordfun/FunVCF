#! /bin/bash

# Test nim binary
echo "Testing nim binary: vcfprocessor"
../bin/vcfprocessor  ../data/test.vcf > test_new.vcf 

echo "Checking ......"
output=$(diff test_new.vcf ../data/test_new.vcf)

if [ "$output" = "" ]
then
  echo "Test pass! The output file is same as expected."
fi

rm "test_new.vcf"