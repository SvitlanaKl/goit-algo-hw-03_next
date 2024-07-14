import os
import shutil
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Recursive file copier and sorter by extension.")
    parser.add_argument("source_dir", help="Path to the source directory.")
    parser.add_argument("dest_dir", nargs="?", default="dist", help="Path to the destination directory (default: dist).")
    return parser.parse_args()

def copy_and_sort_files(source_dir, dest_dir):
    print(f"Copying and sorting files from {source_dir} to {dest_dir}")
    try:
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        
        for item in os.listdir(source_dir):
            source_path = os.path.join(source_dir, item)
            if os.path.isdir(source_path):
                copy_and_sort_files(source_path, dest_dir)
            else:
                file_extension = os.path.splitext(item)[1][1:]  # get the file extension without the dot
                if not file_extension:
                    file_extension = "no_extension"
                extension_dir = os.path.join(dest_dir, file_extension)
                if not os.path.exists(extension_dir):
                    os.makedirs(extension_dir)
                dest_path = os.path.join(extension_dir, item)
                try:
                    shutil.copy2(source_path, dest_path)
                    print(f"Copied {source_path} to {dest_path}")
                except Exception as e:
                    print(f"Failed to copy {source_path} to {dest_path}: {e}")
    except Exception as e:
        print(f"Error accessing directory {source_dir}: {e}")

def main():
    args = parse_arguments()
    source_dir = args.source_dir
    dest_dir = args.dest_dir
    
    print(f"Source directory: {source_dir}")
    print(f"Destination directory: {dest_dir}")

    if not os.path.exists(source_dir):
        print(f"Source directory {source_dir} does not exist.")
        return
    
    copy_and_sort_files(source_dir, dest_dir)
    print(f"All files from {source_dir} have been copied and sorted into {dest_dir}")

if __name__ == "__main__":
    main()

