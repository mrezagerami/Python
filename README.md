# Python

You can find the Python course with the implemented codes here.
Ask me if you have any questions.
mr.gerami@gmail.com

-----
Note:
This tutorial is from two years ago and some instructions may have changed.
Be careful during execution.



--------------------------------------------------------------------------
Duplicate File Finder Script
This Python script is a comprehensive tool for identifying duplicate files across two different directories. It scans two folders and their subfolders, finds all files with identical names, and generates a single, organized list of their full paths. This list is sorted by filename, making it easy to review and manage the duplicates.

Features
Single Script: All functionality is contained in one easy-to-run file.
Recursive Scan: The script efficiently scans all files and subfolders in the two specified directories.
Duplicate Identification: It accurately identifies files with matching names across the two locations.
Organized Output: The final output file lists all full paths for a single duplicate file consecutively, simplifying the review and deletion process.
Error Handling: Includes robust error handling for missing directories or other unexpected issues.

How to Use
Clone or Download: Get the find_and_sort_duplicates.py file to your local machine.
Edit the Script: Open the script in a text editor. Locate the following lines and update the folder paths to match your directories:

Python
folder_A = r'E:\BackupD'
folder_B = r'F:\New-2024-aug'
output_file = 'found_duplicates_full_paths_sorted.txt'
Run the Script: Open your terminal or command prompt, navigate to the directory where the script is located, and run it using Python:

Bash
python find_and_sort_duplicates.py
Review the Output: The script will create a file named found_duplicates_full_paths_sorted.txt in the same directory. Open this file to see the sorted list of all duplicate files and their full paths.
