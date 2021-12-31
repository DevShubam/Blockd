# This script gets all .txt files in the folder, and merges them. 

import glob

read_files = glob.glob("*.txt")

with open("blockd.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
