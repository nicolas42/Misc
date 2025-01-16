import os
import sys
import glob
import shutil

def ls(path='.', pattern='*'):
    """List files in the current directory or given path."""
    return glob.glob(os.path.join(path, pattern))

def mkdir(directory):
    """Create a directory."""
    os.makedirs(directory, exist_ok=True)

def rm(file_path):
    """Remove a file."""
    if os.path.isfile(file_path):
        os.remove(file_path)

def rmdir(directory):
    """Remove a directory and its contents."""
    if os.path.exists(directory):
        shutil.rmtree(directory)

def cp(src, dest):
    """Copy a file or directory."""
    if os.path.isdir(dest):
        dest = os.path.join(dest, os.path.basename(src))
    shutil.copy2(src, dest)

def mv(src, dest):
    """Move/rename a file or directory."""
    if os.path.isdir(dest):
        dest = os.path.join(dest, os.path.basename(src))
    shutil.move(src, dest)

def cat(file_path):
    """Print contents of a file to stdout."""
    with open(file_path, 'r') as file:
        print(file.read(), end='')

def echo(*args, file=None):
    """Echo arguments to stdout or file."""
    output = ' '.join(map(str, args))
    if file:
        with open(file, 'a') as f:
            f.write(output + '\n')
    else:
        print(output)

def touch(file_path):
    """Create an empty file or update the access/modified time of an existing file."""
    with open(file_path, 'a'):
        os.utime(file_path, None)

def pwd():
    """Print working directory."""
    return os.getcwd()

def cd(path):
    """Change directory."""
    os.chdir(path)

    
# To automatically load this into interactive Python
#if __name__ == '__main__':
#    import IPython
#    IPython.start_ipython(argv=[])
