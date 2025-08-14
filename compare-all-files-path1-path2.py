import os

def find_duplicates_between_files(file1_path, file2_path, output_path):
    """
    Compares two text files line by line and writes duplicate lines
    to a new output file.

    Args:
        file1_path (str): The path to the first input file.
        file2_path (str): The path to the second input file.
        output_path (str): The path for the output file where duplicates will be written.
    """
    try:
        # Read all lines from the first file into a set for efficient lookup
        with open(file1_path, 'r', encoding='utf-8') as f1:
            file1_lines = set(line.strip() for line in f1 if line.strip())

        # Create a set to store duplicates to avoid writing them more than once
        duplicates = set()

        # Read the second file line by line and check for duplicates
        with open(file2_path, 'r', encoding='utf-8') as f2:
            for line in f2:
                stripped_line = line.strip()
                if stripped_line and stripped_line in file1_lines:
                    duplicates.add(stripped_line)

        # Write the unique duplicate lines to the output file
        if duplicates:
            with open(output_path, 'w', encoding='utf-8') as out_f:
                for duplicate_line in sorted(list(duplicates)):
                    out_f.write(f"{duplicate_line}\n")
            print(f"Successfully found {len(duplicates)} duplicate lines and wrote them to {output_path}")
        else:
            print("No duplicate lines were found between the two files.")

    except FileNotFoundError as e:
        print(f"Error: One of the files was not found. Please check the paths. {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Define the paths for the two input files and the output file
file1 = 'all_files_only_name1.txt'
file2 = 'all_files_only_name2.txt'
output_file = 'common_duplicates.txt'

# Run the function
find_duplicates_between_files(file1, file2, output_file)