# Individual Motility and Collective Behaviour

This repository contains the code and analyses related to the main project of my PhD, focusing on the individual motility and collective behaviour of nematodes.

## Repository Structure

- **Analysis/**
  - Contains documents and plots related to the analysis of the data.
  - `Analalysis 10.09.23.docx`: Detailed analysis document.
  - `plots/`: Directory containing various plots generated from the analysis.

- **Code/**
  - Contains the code used for data processing and analysis.
  - **Python/**
    - `requirements.txt`: List of Python dependencies.
    - `create_videos.py`: Script to create videos from frames.
    - `swarming_segmentation.ipynb`: Jupyter notebook for segmentation analysis.
    - `hdf5_frame_extractor.py`: Script to extract frames from HDF5 files.
    - `Strain_Comparison_Study.ipynb`: Jupyter notebook for strain comparison study.
    - `wavelet_transform.ipynb`: Jupyter notebook for wavelet transformation.
    - `testWaveletTheory.ipynb`: Jupyter notebook to test wavelet theory.
    - `frames_to_video.ipynb`: Jupyter notebook for creating videos from frames.
    - `README.txt`: Additional information about the Python code.
    - `wavelet_umap.ipynb`: Jupyter notebook for UMAP visualization of wavelet transforms.
    - `hdf5_to_mp4.py`: Script to convert HDF5 files to MP4 videos.
  - **Matlab_code/**
    - `ch2_Antonio.mlx`: Matlab live script for analysis.
    - `asWindow_New.m`: Matlab script for window analysis.
    - `getMSD_X.m`: Matlab script to get Mean Squared Displacement.
    - `inidvidual_cm_quantification.mlx`: Matlab live script for individual center of mass quantification.
    - `ch2_Antonio_thesis_collective_state.mlx`: Matlab live script for collective state analysis.
    - `getMSD_vec.m`: Matlab script to get Mean Squared Displacement vector.

## How to Use

1. **Installation:**
   - For Python code, install dependencies using:
     ```bash
     pip install -r Code/Python/requirements.txt
     ```

2. **Running the Notebooks:**
   - Open the Jupyter notebooks in `Code/Python/` using JupyterLab or Jupyter Notebook and execute the cells to perform the analyses.

3. **Matlab Code:**
   - Open the Matlab scripts in `Code/Matlab_code/` using Matlab and run the scripts as needed.
