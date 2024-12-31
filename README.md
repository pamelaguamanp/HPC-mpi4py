# HPC-mpi4py

This project is the final assignment for the HPC course, leveraging the `mpi4py` library to perform parallel image processing. The application applies convolutions on RGB channels with different kernel sizes, distributing the workload across multiple MPI processes.

## Files

1. **`finalproject.py`**  
   This Python script contains the main code that:
   - Loads a test image.
   - Divides the image among MPI processes.
   - Applies convolutions with different kernel sizes to each color channel.
   - Gathers results and saves both the original and processed images.

2. **`finalproject.sh`**  
   This shell script is used to execute the Python program in an HPC environment with MPI.

## Requirements

Before running this project, ensure your environment meets the following requirements:

- Python 3.7 or higher
- Libraries: `mpi4py`, `numpy`, `scipy`, `Pillow`
- MPI environment installed (e.g., OpenMPI or MPICH)

## Execution

### 1. Configure your environment
Ensure you have access to an HPC cluster with MPI support and load the necessary modules:

```bash
module load python/3.8
module load mpi
