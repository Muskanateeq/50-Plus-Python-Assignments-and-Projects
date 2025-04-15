import os
import sys

def bulk_rename_files(directory, prefix):
    # List all items in the directory
    files = os.listdir(directory)
    
    # Counter to check if any file was renamed
    renamed_count = 0
    
    for file in files:
        file_path = os.path.join(directory, file)
        
        # Process only files (skip directories)
        if os.path.isfile(file_path):
            # Check your condition: here we rename only .txt files
            if file.lower().endswith('.txt'):
                new_name = prefix + file
                new_path = os.path.join(directory, new_name)
                try:
                    os.rename(file_path, new_path)
                    print(f"Renamed '{file}' to '{new_name}'")
                    renamed_count += 1
                except Exception as e:
                    print(f"Error renaming '{file}': {e}")
    
    if renamed_count == 0:
        print("No files matched the renaming criteria.")
    else:
        print(f"\nTotal files renamed: {renamed_count}")

def main():
    # Prompt user for the directory path
    directory = input("Enter the full path to the folder: ").strip()
    
    # Validate directory
    if not os.path.isdir(directory):
        print("Error: The provided directory does not exist.")
        sys.exit(1)
    
    # Prompt user for a prefix to add (you can change this condition as needed)
    prefix = input("Enter the prefix to add to each .txt file: ").strip()
    
    bulk_rename_files(directory, prefix)

if __name__ == "__main__":
    main()
