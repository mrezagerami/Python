import os
from collections import defaultdict

def find_and_sort_full_paths(common_duplicates_file, file1_path, file2_path, output_path):
    """
    Reads a list of filenames from common_duplicates_file, finds all full paths for
    each of those filenames in file1_path and file2_path, and writes them to an
    output file, sorted so that all paths for a single filename are grouped together.
    
    Args:
        common_duplicates_file (str): Path to the file containing a list of filenames.
        file1_path (str): Path to the first file to search in.
        file2_path (str): Path to the second file to search in.
        output_path (str): Path for the output file to write the found and sorted full paths.
    """
    try:
        # Read the filenames from the common_duplicates.txt into a set for efficient lookup
        with open(common_duplicates_file, 'r', encoding='utf-8') as f:
            duplicate_filenames = set(os.path.basename(line.strip()) for line in f if line.strip())

        # Use a defaultdict to group full paths by filename
        duplicate_paths_by_name = defaultdict(list)
        
        print(f"Searching for {len(duplicate_filenames)} duplicate filenames...")

        # Search for matching filenames in the first file
        with open(file1_path, 'r', encoding='utf-8') as f1:
            for line in f1:
                full_path = line.strip()
                if full_path:
                    filename = os.path.basename(full_path)
                    if filename in duplicate_filenames:
                        duplicate_paths_by_name[filename].append(full_path)
        
        # Search for matching filenames in the second file
        with open(file2_path, 'r', encoding='utf-8') as f2:
            for line in f2:
                full_path = line.strip()
                if full_path:
                    filename = os.path.basename(full_path)
                    if filename in duplicate_filenames:
                        duplicate_paths_by_name[filename].append(full_path)
        
        # Write the found paths to the output file, sorted by filename
        if duplicate_paths_by_name:
            with open(output_path, 'w', encoding='utf-8') as out_f:
                # Iterate through sorted filenames
                for filename in sorted(duplicate_paths_by_name.keys()):
                    # Sort the full paths for each filename for consistency
                    for path in sorted(duplicate_paths_by_name[filename]):
                        out_f.write(f"{path}\n")
            print(f"Successfully found and sorted duplicate paths and wrote them to {output_path}")
        else:
            print("No matching full paths were found based on the filenames.")

    except FileNotFoundError as e:
        print(f"Error: One of the specified files was not found. Please check the paths. {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Define file paths
common_duplicates_file = 'common_duplicates.txt'
file1 = 'all_files_with_full_path1.txt'
file2 = 'all_files_with_full_path2.txt'
output_file = 'found_duplicates_full_paths_sorted.txt'

# Run the function
find_and_sort_full_paths(common_duplicates_file, file1, file2, output_file)