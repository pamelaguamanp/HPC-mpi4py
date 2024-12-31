# **Distributed Image Processing with MPI**

This repository contains a Python project that performs distributed image processing using **Message Passing Interface (MPI)**, enabling parallel processing of an image across multiple computing nodes. The project applies a convolution filter to an image, which is distributed across multiple processes. The convolution is applied separately to the red, green, and blue channels of the image.

## **Project Overview**

The main purpose of this project is to demonstrate the use of parallel processing for image manipulation using **MPI**. The image is split across multiple processes, and each process applies a convolution filter to a specific color channel. Once the image is processed, the results are gathered and saved.

### **Key Components**:
1. **MPI (Message Passing Interface)** for distributed computation.
2. **NumPy** for handling the image data and array manipulations.
3. **Scipy.ndimage** for applying the convolution filter.
4. **Pillow (PIL)** for saving the output image in JPEG format.

## **Installation and Setup**

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/your-repository-name.git
    cd your-repository-name
    ```

2. **Create and activate a Conda environment**:
    ```bash
    conda create -n myenv python=3.8 numpy mpi4py scipy pillow
    conda activate myenv
    ```

3. **Install additional dependencies**:
    If you are using any other dependencies, you can install them here, but the necessary ones are already included in the environment.

4. **Load MPI and Conda modules**:
    If you're running the code on an HPC system, make sure to load the required modules (as specified in the SLURM job script).

    ```bash
    module load openmpi/4.1.3
    module load any/python/3.8.3-conda
    ```

## **Input**

The input image used in this project is a test image that is loaded directly from the **`scipy.datasets.face`** function. It is a grayscale image of a face, which is split and processed across MPI processes.

- **Input Image**: The input is a **test image** of a face from `scipy.datasets.face()`.

- **File**: `original_image.jpg` (generated and saved as part of the processing workflow)

## **Output**

The output of this project is the **processed version of the input image**. After applying a convolution filter to each RGB channel (using a predefined kernel size), the processed image is saved.

- **Processed Image**: The result is a smoothed version of the original image with applied convolution filters. The output image is stored as `processed_image.jpg`.

- **File**: `processed_image.jpg` (saved at the end of the processing)

### **Sample Input and Output**

**Input Image:**

- `original_image.jpg`: A test image of a face loaded from SciPy datasets.

**Output Image:**

- `processed_image.jpg`: The same image after applying a convolution filter (smoothing effect applied to each color channel).

---

## **Running the Code**

### **On Local Machine**

1. After activating the Conda environment, simply run the following command:
    ```bash
    python finalproject.py
    ```

### **On HPC with SLURM**

1. To run the script on an HPC cluster using SLURM, you can submit a job using the following command:
    ```bash
    sbatch finalproject.sh
    ```
   
   This will execute the Python script using the specified number of MPI tasks. The SLURM job script (`finalproject.sh`) specifies:
   - Number of tasks (`--ntasks=3`), which determines the number of MPI processes.
   - Memory (`--mem=2G`) and time (`-t 10:00`) allocated for the job.
   - The working directory and required modules for the job.

2. Once the job completes, the results will be stored in the directory where the SLURM job was run.

---

## **File Structure**

```bash
.
├── finalproject.py           # Python script for distributed image processing using MPI
├── finalproject.sh           # SLURM job submission script
├── original_image.jpg        # Input image (generated automatically from scipy datasets)
└── processed_image.jpg       # Output image (after applying convolution)
