import os
import pathlib

def scan_folders(folder_A, folder_B):
    files_A = set()
    files_B = set()

    for dirpath, dirnames, filenames in os.walk(folder_A):
        for f in filenames:
            full_path = pathlib.Path(dirpath) / f
            files_A.add((f, full_path))

    for dirpath, dirnames, filenames in os.walk(folder_B):
        for f in filenames:
            full_path = pathlib.Path(dirpath) / f
            files_B.add((f, full_path))

    with open('all_files_with_full_path.txt', 'w', encoding='utf-8') as f:
        all_files = sorted(list(files_A | files_B))
        for filename, full_path in all_files:
            f.write(f'{full_path}\n')

    with open('all_files_only_name.txt', 'w', encoding='utf-8') as f:
        all_file_names = sorted(list(set(item[0] for item in files_A | files_B)))
        for filename in all_file_names:
            f.write(f'{filename}\n')

    duplicate_files = files_A & files_B
    with open('duplicate_files.txt', 'w', encoding='utf-8') as f:
        sorted_duplicates = sorted(list(duplicate_files))
        for filename, full_path in sorted_duplicates:
            f.write(f'{full_path}\n')

folder_A = r'E:\BackupD'
folder_B = r'F:\New-2024-aug'

scan_folders(folder_A, folder_B)
print("Output files created.")
