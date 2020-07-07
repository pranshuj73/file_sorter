# my picture folder is cluttered thanks to so many screenshots that i take
# this script is supposed to move all the screenshots to a folder named 'Screenshots'
# so that my picures folder doesnt get filled with all the screenshots i take

import os, shutil

def file_sorter(source_path, target_path):
	if not os.path.isdir(target_path):
		os.mkdir(target_path)

	file_list = [filename for filename in os.listdir(source_path) if filename.startswith("Screenshot")]

	for file in file_list:
		shutil.move(source_path + '/' + file, target_path)

	print("Files moved successfully.")

if __name__ == '__main__':
	file_sorter('/home/volt/Pictures', '/home/volt/Pictures/Screenshots')