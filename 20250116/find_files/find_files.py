import os
import sys

def search_filenames(base_path, search_terms):
    """
    Search for files with names containing all of the specific terms inside a given directory.

    :param base_path: The directory to start searching.
    :param search_terms: A list of terms to search for in filenames.
    """
    for root, dirs, files in os.walk(base_path):
        for file in files:
            match = True
            for term in search_terms:
                if term not in file:
                    match = False
                    break
            if match:
                print(f"Found matching file: {os.path.join(root, file)}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python find_files.py <directory> <query_term1> [<query_term2> ...]")
        sys.exit(1)

    # Base directory to search
    base_directory = sys.argv[1]

    # Terms to search in filenames
    search_terms = sys.argv[2:]

    # Start searching
    search_filenames(base_directory, search_terms)
