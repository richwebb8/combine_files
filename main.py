# Public imports
import os
import shutil

# Function to flatten directory
def flatten(directory):
    for dirpath, _, filenames in os.walk(directory, topdown=False):
        for filename in filenames:
            i = 0
            source = os.path.join(dirpath, filename)
            target = os.path.join(directory, filename)

            while os.path.exists(target):
                i += 1
                file_parts = os.path.splitext(os.path.basename(filename))

                target = os.path.join(
                    directory,
                    file_parts[0] + "_" + str(i) + file_parts[1],
                )

            shutil.move(source, target)

            # print("Moved ", source, " to ", target)

        if dirpath != directory:
            os.rmdir(dirpath)

            # print("Deleted ", dirpath)

if __name__ == "__main__":
    source_dir = "/Users/my_user/Documents/test_folder/in" # path to root folder of source files
    target_dir = "/Users/my_user/Documents/test_folder/out"  # path to folder you want combined files to be outputted to
    ignore = '*.txt', '*.svg', '.DS_Store' # file extensions of files you want to ignore
    # Delete target_dir if exists otherwise copytree will error
    if os.path.exists(target_dir) and os.path.isdir(target_dir):
        shutil.rmtree(target_dir)
    shutil.copytree(src = source_dir, dst = target_dir, ignore = shutil.ignore_patterns(*ignore)) # copy all files except those with ignore file types
    flatten(directory = target_dir) # flatten output directory