
# Project Title: Nematode Behavior Analysis

## Overview

This project is dedicated to the analysis of collective behavior in nematodes. It involves processing HDF5 video files to extract relevant frames and then conducting detailed image analysis on these frames. The workflow is divided into two main parts:

1. **Frame Extraction**: Implemented in a Python script (`hdf5_frame_extractor.py`).
2. **Data Analysis**: Conducted in a Jupyter Notebook.

## Workflow

### 1. hdf5_frame_extractor.py

This script is responsible for the initial data processing stage. It extracts frames from HDF5 files and organizes these frames into separate folders for each strain and experiment.

#### Features:
- Extracts frames from HDF5 video files.
- Saves frames in structured directories based on strain and experiment.
- Designed to be run as needed for new data or re-extraction.

#### Usage:
Run the script in a Python environment. Ensure that the root path for HDF5 files is correctly set in the script.

### 2. Data Analysis (Jupyter Notebook)

After frame extraction, the Jupyter Notebook is used for subsequent data analysis. This interactive environment is ideal for loading images, processing data, and visualizing results.

#### Capabilities:
- Loads images from the output directories created by `hdf5_frame_extractor.py`.
- Allows for interactive manipulation, analysis, and visualization of data.
- Supports documentation alongside code for clarity and comprehensibility.

#### Running the Analysis:
Open the Jupyter Notebook in your preferred environment and execute the cells. The notebook assumes that the frames are already extracted and available in the specified directories.

## Best Practices

- **Version Control**: Use Git for version control to manage and track changes in your scripts.
- **Documentation**: Leverage the documentation capabilities of Jupyter Notebook. Clearly describe each analysis step for future reference.
- **Modular Coding**: Structure your analysis code into functions or modules for better readability and reusability.

## Contributing

Feel free to fork this project and contribute. If you find any bugs or have suggestions for improvement, please open an issue or submit a pull request.
