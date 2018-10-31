#!/bin/bash
#SBATCH -p medium
#SBATCH --mem=32GB
#SBATCH --mincpus=8
#SBATCH -o output_%a.log
CMD=$(head -n $SLURM_ARRAY_TASK_ID task.list | tail -1)
/home/onalant/source/privileged_residues/conda/bin/python $CMD
