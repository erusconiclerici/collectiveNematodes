import os
import glob
import h5py
import cv2

def ensure_directory_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)

def extract_experiment_name(file_path):
    # Assuming the experiment's name is part of the file's name
    base_name = os.path.basename(file_path)
    name_parts = base_name.split('_')
    experiment_name = '_'.join(name_parts[:-1])  # Exclude the extension and any other parts
    return experiment_name

def create_output_directories_for_experiments(root_path):
    output_dirs = {}
    strain_folders = [d for d in os.listdir(root_path) if os.path.isdir(os.path.join(root_path, d))]
    
    for strain in strain_folders:
        hdf5_files = glob.glob(os.path.join(root_path, strain, '*.hdf5'))
        for file_path in hdf5_files:
            experiment_name = extract_experiment_name(file_path)
            output_dir = os.path.join(root_path, strain, experiment_name)
            ensure_directory_exists(output_dir)
            output_dirs[file_path] = output_dir

    return output_dirs

def extract_frames_from_hdf5(file_path, output_directory, step=500):
    with h5py.File(file_path, 'r') as hdf:
        img_ds2 = hdf['/mask']
        for i in range(0, img_ds2.shape[0], step):
            name = f"{i:06d}.jpg"
            cv2.imwrite(os.path.join(output_directory, name), img_ds2[i, :])

# Set the root path where the HDF5 files are stored
root_path = '/Volumes/TOSHIBA_EXT/Phenotype_features_collective/Data'

# Create output directories for each experiment under each strain
output_directories = create_output_directories_for_experiments(root_path)

# Extract frames from HDF5 files
for file_path, output_dir in output_directories.items():
    extract_frames_from_hdf5(file_path, output_dir)

print("Frame extraction completed.")
