#!/bin/bash
#PBS -q production
#PBS -N SaltMar2Tum
#PBS -l select=1:ncpus=1:ngpus=1
#PBS -l place=free
#PBS -V

# change to the working directory 
cd $PBS_O_WORKDIR
echo "pbsworkdir"
echo $PBS_O_WORKDIR
EXECDIR=`pwd`
WCSWORKDIR=/scratch/isaac.overcast/MarTum/Saltator
cd $WCSWORKDIR
export PATH=./:$PATH
echo $PATH

export OMP_NUM_THREADS=8
#/scratch/isaac.overcast/WCS-fsc2/withhybrids/run_fsc.sh -p nomigration -t -m > wcs-fsc.out 2>&1
./run_fsc.sh -p unimigration-MarToTum  -m -n 5  > martum-fsc.out 2>&1 $EXECDIR/martum.out
#./run_fsc.sh -p symmetricalmigration -m -n 50 > wcs-fsc.out 2>&1 $EXECDIR/wcs.out

echo ">>>> Hoggy!..."
