import os
import pathlib
from collections import defaultdict

def find_and_sort_duplicates(folder_A, folder_B, output_path):
    """
    Scans two folders, finds duplicate filenames, and writes their full paths
    to an output file, sorted by filename for easy review.

    Args:
        folder_A (str): The path to the first folder to scan.
        folder_B (str): The path to the second folder to scan.
        output_path (str): The path for the output file where duplicates will be written.
    """
    try:
        # Step 1: Scan both folders and collect filenames and their full paths
        print("Scanning folders for files...")
        files_A = defaultdict(list)
        for dirpath, dirnames, filenames in os.walk(folder_A):
            for f in filenames:
                full_path = pathlib.Path(dirpath) / f
                files_A[f].append(str(full_path))

        files_B = defaultdict(list)
        for dirpath, dirnames, filenames in os.walk(folder_B):
            for f in filenames:
                full_path = pathlib.Path(dirpath) / f
                files_B[f].append(str(full_path))

        # Step 2: Find common filenames between the two folders
        print("Comparing files to find duplicates...")
        duplicate_filenames = set(files_A.keys()) & set(files_B.keys())

        # Step 3: Collect all full paths for the common filenames
        all_duplicate_paths = defaultdict(list)
        for filename in duplicate_filenames:
            all_duplicate_paths[filename].extend(files_A[filename])
            all_duplicate_paths[filename].extend(files_B[filename])

        # Step 4: Write the found paths to the output file, sorted by filename
        if all_duplicate_paths:
            with open(output_path, 'w', encoding='utf-8') as out_f:
                for filename in sorted(all_duplicate_paths.keys()):
                    # Sort the full paths for each filename for consistency
                    for path in sorted(all_duplicate_paths[filename]):
                        out_f.write(f"{path}\n")
            print(f"Successfully found {len(all_duplicate_paths)} duplicate files and wrote their full paths to {output_path}")
        else:
            print("No matching full paths were found based on filenames.")

    except FileNotFoundError as e:
        print(f"Error: A specified folder was not found. Please check the paths. {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Define the paths for the two folders and the output file
folder_A = r'D:\Training'
folder_B = r'D:\!-RoadMap'
output_file = 'found_duplicates_full_paths_sorted.txt'

# Run the function
find_and_sort_duplicates(folder_A, folder_B, output_file)