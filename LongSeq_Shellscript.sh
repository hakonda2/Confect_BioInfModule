#!/bin/sh

# Run python script
echo "Running complex program... Please be patient"
echo ""
sleep 4
./GetLongSeq.py GreatData.fasta > LongSeq.fasta

# Make a directory
echo "Making new directory..."
echo ""
sleep 3
mkdir LongSeqDir

# Move output from script to directory
echo "moving file..."
echo ""
sleep 3
mv LongSeq.fasta LongSeqDir
echo "DONE!"

