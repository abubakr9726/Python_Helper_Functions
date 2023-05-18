import os
import argparse
import sys
import shutil


parser = argparse.ArgumentParser()
parser.add_argument("--Type1", default=".png", type=str)
parser.add_argument("--Type2", default=".txt", type=str)
parser.add_argument("--Input", default="F:\\data annotation\\train\\", type=str)
parser.add_argument("--Output1", default="F:\\data annotation\\images\\", type=str)
parser.add_argument("--Output2", default="F:\\data annotation\\annotations\\", type=str)
args =parser.parse_args()

FileType01 = args.Type1
FileType02 = args.Type2
InputDirectory = args.Input
OutputFile01 = args.Output1
OutputFile02 = args.Output2

if not os.path.exists(OutputFile01):
    os.mkdir(OutputFile01)

if not os.path.exists(OutputFile02):
    os.mkdir(OutputFile02)

if not os.path.exists(InputDirectory):
    print("Invalid Input Directory")
    sys.exit()


for file1 in sorted(os.listdir(InputDirectory)):
    if file1.endswith(FileType01):
        source = InputDirectory + file1
        destination = OutputFile01 + file1
        shutil.copy(source, destination)
        print(source, " ---->   ", destination, " ---->   Copied")

for file2 in sorted(os.listdir(InputDirectory)):
    if file2.endswith(FileType02):
        source = InputDirectory + file2
        destination = OutputFile02 + file2
        shutil.copy(source, destination)
        print(source, " ---->   ", destination, " ---->   Copied")