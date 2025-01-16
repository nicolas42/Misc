import os
import sys
import glob
import shutil

def list_files(path='.', pattern='*'):
    """
    List all files matching the pattern in the specified directory.
    
    :param path: Directory path to search in
    :param pattern: File pattern to match (uses glob syntax)
    :return: List of file paths
    """
    return glob.glob(os.path.join(path, pattern))

def make_dir(directory):
    """
    Create a directory if it doesn't exist.
    
    :param directory: Path to the directory to create
    """
    os.makedirs(directory, exist_ok=True)

def remove_file(file_path):
    """
    Remove a file if it exists.
    
    :param file_path: Path to the file to be removed
    """
    if os.path.isfile(file_path):
        os.remove(file_path)

def remove_dir(directory):
    """
    Remove a directory and all its contents if it exists.
    
    :param directory: Path to the directory to remove
    """
    if os.path.exists(directory):
        shutil.rmtree(directory)

def copy_file(src, dest):
    """
    Copy a file from src to dest. If dest is a directory, 
    the file will be copied into that directory with the same name.
    
    :param src: Source file path
    :param dest: Destination path or directory
    """
    if os.path.isdir(dest):
        dest = os.path.join(dest, os.path.basename(src))
    shutil.copy2(src, dest)

def move_file(src, dest):
    """
    Move a file from src to dest. If dest is a directory, 
    the file will be moved into that directory with the same name.
    
    :param src: Source file path
    :param dest: Destination path or directory
    """
    if os.path.isdir(dest):
        dest = os.path.join(dest, os.path.basename(src))
    shutil.move(src, dest)

def get_file_size(file_path):
    """
    Get the size of a file in bytes.
    
    :param file_path: Path to the file
    :return: File size in bytes
    """
    return os.path.getsize(file_path)

def read_file(file_path):
    """
    Read the entire content of a file as a string.
    
    :param file_path: Path to the file
    :return: Content of the file as a string
    """
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, content, mode='w'):
    """
    Write content to a file. Mode can be 'w' for write or 'a' for append.
    
    :param file_path: Path to the file
    :param content: String content to write
    :param mode: Write mode ('w' or 'a')
    """
    with open(file_path, mode) as file:
        file.write(content)

def rename_file(old_name, new_name):
    """
    Rename or move a file.
    
    :param old_name: Current file name or path
    :param new_name: New file name or path
    """
    os.rename(old_name, new_name)

def get_current_dir():
    """
    Get the current working directory.
    
    :return: Current working directory path
    """
    return os.getcwd()

def change_dir(path):
    """
    Change the current working directory to the specified path.
    
    :param path: New directory path
    """
    os.chdir(path)

# Example usage
if __name__ == "__main__":
    print(list_files())
    make_dir('new_directory')
    copy_file('source.txt', 'new_directory')
    print(get_file_size('source.txt'))
    content = read_file('source.txt')
    write_file('destination.txt', content)
    rename_file('destination.txt', 'renamed.txt')
    remove_file('renamed.txt')
    remove_dir('new_directory')
    print(get_current_dir())
    change_dir('..')
    print(get_current_dir())
