# combine_files
Python utility to combine all the files in a nested folder structure into a single flat directory. Uses `shutil.copytree` to copy all the files in `source_dir` that do not match a file extension in `ignore` to a new directory `target_dir`. The directory structure in `target_dir` is then flattened.
## How to use the utility
1. Edit `source_dir` to be the path to the root folder of the source files you want to combine
2. Edit `target_dir` to be the path to the folder you want combined files to be outputted to
3. Edit `ignore` to include any file extentions of files you don't want to include
4. Run `python main.py`
