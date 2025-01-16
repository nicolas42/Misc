import os
import shutil
import argparse

def copy_and_rename_files(input_dir, output_dir):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Walk through the directory structure
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            # Construct the full path of the file
            file_path = os.path.join(root, file)
            
            # Get the relative path from the base directory
            relative_path = os.path.relpath(file_path, input_dir)
            
            # Convert the path to the new filename (replacing slashes with underscores)
            new_name = relative_path.replace(os.sep, '_')
            
            # Construct the new file path in the output directory
            new_file_path = os.path.join(output_dir, new_name)
            
            # Copy the file with the new name
            shutil.copy(file_path, new_file_path)
            print(f"Copied: {file_path} to {new_file_path}")

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Copy and rename files based on their path.")
    parser.add_argument("input_dir", help="The directory containing files to be processed")
    parser.add_argument("output_dir", help="The directory to which renamed files will be copied")
    args = parser.parse_args()

    # Process files with provided directories
    copy_and_rename_files(args.input_dir, args.output_dir)