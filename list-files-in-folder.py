import os

def list_files_in_folder(folder_path):
    try:
        files = os.listdir(folder_path)
        return files, None
    except FileNotFoundError:
         return None, "Folder not Found"
    except PermissionError:
         return None, "Permission denied"


def main():
    folders_path = input("Enter a list of folder paths seperated by spaces:").list()

    for  folder in folders_path:
        files ,error_message = list_files_in_folder(folder)
        if files:
            print(f"Files in {folder}: ")
            for file in files:
                print(file) 
        else:
            print(f"Error in {folder} : {error_message}")        

    if __name__ == "__main__":
        main()       