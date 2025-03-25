# list all files in the list of folders that user provides
# input --> list of folder names
# output --> files in the provided folders
#############################################################
#############################################################
import os
folders = input("Enter a list of folder paths separated by spaces: ").split()
for folder in folders:
    try:
        files=os.listdir(folder)
        #print(files) this will print output in list format 
    except FileNotFoundError:
        print(f"folder not found --> {folder}")
        continue
    except PermissionError:
        print(f"not enough permissions on folder --> {folder}")
        continue
    print("====listing files for folder===", folder)
    for file in files:
        print(file)


#############################################################
#############################################################
############### same code using functions ###################

'''

import os

def list_files_in_folder(folder_path):
    try:
        files = os.listdir(folder_path)
        return files, None
    except FileNotFoundError:
        return None, "Folder not found"
    except PermissionError:
        return None, "Permission denied"

def main():
    folder_paths = input("Enter a list of folder paths separated by spaces: ").split()
    
    for folder_path in folder_paths:
        files, error_message = list_files_in_folder(folder_path)
        if files:
            print(f"Files in {folder_path}:")
            for file in files:
                print(file)
        else:
            print(f"Error in {folder_path}: {error_message}")

if __name__ == "__main__":
    main()


'''