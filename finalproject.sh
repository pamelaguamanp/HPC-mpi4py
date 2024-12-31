import numpy as np
from mpi4py import MPI
from scipy.ndimage import convolve
from scipy.datasets import face  # Updated to use scipy.datasets
from PIL import Image  # To save images

# MPI Initialization
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Load the test image
image = face()
global_shape = image.shape
local_shape = global_shape[0] // size
#!/bin/bash
#SBATCH -J finalproject
#SBATCH --partition=testing
#SBATCH -A ealloc_e430d_hpc_pamela1
#SBATCH -t 10:00
#SBATCH --ntasks=3
#SBATCH --cpus-per-task=1
#SBATCH --mem=2G
#SBATCH --output=%x-%j.out

# Set the working directory
#cd /path/to/your/directory
cd  /gpfs/space/projects/hpc-course/hpc_pamelama/lab7y8
# Load required modules
# Load MPI and Conda
module purge
module load any/python/3.8.3-conda
module load openmpi/4.1.3
#module load opencv/3.4.12
# Activate Conda environment
source activate myenvlab7y8

# Execute the script
#mpirun -np ${SLURM_NTASKS} python script.py
mpirun -np ${SLURM_NTASKS} /gpfs/helios/home/etais/hpc_pamelama/.conda/envs/myenvlab7y8/bin/python finalproject.py

