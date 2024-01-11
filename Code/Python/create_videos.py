import cv2
import os
import glob

def create_video_from_frames(frames_folder, output_video_file, fps=5):
    # Get all frame file paths
    frame_paths = sorted(glob.glob(os.path.join(frames_folder, '*.jpg')))  # Adjust the extension if needed

    if not frame_paths:
        print(f"No frames found in {frames_folder}. Skipping...")
        return

    # Read the first frame to determine width and height
    frame = cv2.imread(frame_paths[0])
    height, width, _ = frame.shape

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can use 'XVID' for AVI
    out = cv2.VideoWriter(output_video_file, fourcc, fps, (width, height))

    # Write each frame to the video
    for frame_path in frame_paths:
        frame = cv2.imread(frame_path)
        out.write(frame)

    # Release everything when job is finished
    out.release()

def process_all_experiments(root_folder, output_folder, fps=30):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over each strain folder
    for strain_folder in os.listdir(root_folder):
        strain_path = os.path.join(root_folder, strain_folder)
        
        if os.path.isdir(strain_path):
            # Iterate over each experiment folder within the strain folder
            for experiment_folder in os.listdir(strain_path):
                experiment_path = os.path.join(strain_path, experiment_folder)
                
                if os.path.isdir(experiment_path):
                    output_video_file = os.path.join(output_folder, f"{strain_folder}_{experiment_folder}.mp4")
                    create_video_from_frames(experiment_path, output_video_file, fps)

# Usage
root_folder = '/Volumes/TOSHIBA_EXT/Phenotype_features_collective/Data/ExtractedFrames'
output_folder = '/Volumes/TOSHIBA_EXT/Phenotype_features_collective/Data/videos'
process_all_experiments(root_folder, output_folder)
