# import os
# import glob
# import h5py
# import cv2
# import numpy as np

# def ensure_directory_exists(path):
#     if not os.path.exists(path):
#         os.makedirs(path)

# def extract_experiment_name(file_path):
#     base_name = os.path.basename(file_path)
#     experiment_name = os.path.splitext(base_name)[0]  # Removes the file extension
#     return experiment_name

# def create_output_directories_for_experiments(root_path, common_folder='ExtractedFrames'):
#     output_dirs = {}
#     strain_folders = [d for d in os.listdir(root_path) if os.path.isdir(os.path.join(root_path, d))]
    
#     for strain in strain_folders:
#         hdf5_files = glob.glob(os.path.join(root_path, strain, '*.hdf5'))
#         for file_path in hdf5_files:
#             experiment_name = extract_experiment_name(file_path)
#             output_dir = os.path.join(root_path, common_folder, strain, experiment_name)
#             ensure_directory_exists(output_dir)
#             output_dirs[file_path] = output_dir

#     return output_dirs

# def convert_hdf5_to_mp4(file_path, output_directory, step=1):
#     with h5py.File(file_path, 'r') as hdf:
#         # Assuming '/mask' is the dataset path containing frames
#         dataset = hdf['/mask']
#         num_frames, height, width = dataset.shape
#         output_video_path = os.path.join(output_directory, extract_experiment_name(file_path) + '.mp4')
        
#         # Define the codec and create VideoWriter object
#         fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec used to compress the frames
#         video = cv2.VideoWriter(output_video_path, fourcc, 20.0, (width, height))
        
#         for i in range(0, num_frames, step):
#             frame = dataset[i, :, :]
#             if frame.ndim == 2:  # If grayscale, convert to BGR for video
#                 frame = cv2.cvtColor(frame.astype(np.uint8), cv2.COLOR_GRAY2BGR)
#             video.write(frame)
        
#         video.release()

# # Set the root path where the HDF5 files are stored
# root_path = '/Volumes/TOSHIBA_EXT/Phenotype_features_collective/Data'

# # Assuming you want to convert all HDF5 files within the specified root_path
# output_directories = create_output_directories_for_experiments(root_path)

# # Convert HDF5 files to MP4
# for file_path, output_dir in output_directories.items():
#     convert_hdf5_to_mp4(file_path, output_dir)

# print("Conversion to MP4 completed.")

### Converting only one file ###########################

import h5py
import cv2
import numpy as np

def convert_hdf5_to_mp4(file_path, output_video_path, step=1):
    with h5py.File(file_path, 'r') as hdf:
        # Assuming '/mask' is the dataset path containing frames
        dataset = hdf['/mask']
        num_frames, height, width = dataset.shape
       
        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec used to compress the frames
        video = cv2.VideoWriter(output_video_path, fourcc, 20.0, (width, height))
        
        for i in range(0, num_frames, step):
            frame = dataset[i, :, :]
            # Check if the frame is grayscale and convert it to BGR (OpenCV uses BGR by default)
            if frame.ndim == 2:  # If grayscale, convert to BGR for video
                frame = cv2.cvtColor(frame.astype(np.uint8), cv2.COLOR_GRAY2BGR)
            video.write(frame)
        
        video.release()

# Specific HDF5 file path
hdf5_file_path = '/Volumes/TOSHIBA_EXT/Phenotype_features_collective/Data/CB4856/1.1_3_cb4856_oo_Set0_Pos0_Ch3_14012018_114743.hdf5'
# Output MP4 file path
output_video_path = '/Volumes/TOSHIBA_EXT/Phenotype_features_collective/ExtractedVideos/1.1_3_cb4856_oo_Set0_Pos0_Ch3_14012018_114743.mp4'

# Convert the specific HDF5 file to MP4
convert_hdf5_to_mp4(hdf5_file_path, output_video_path)

print("Conversion to MP4 completed.")
