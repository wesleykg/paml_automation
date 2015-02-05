import re, tempfile, sys
from Bio import AlignIO

## Prep the file for PAML by removing stop codons and standardizing gap characters
with open(sys.argv[1], "r") as file: # Opens the file
    data1 = file.read() # Reads the file into memory as a string
    data1 = re.sub("TAA(?=\n>|\n\Z)|TAG(?=\n>|\n\Z)|TGA(?=\n>|\n\Z)", "???", data1, flags = re.IGNORECASE) # Replaces stop codons with ???
    data1 = data1.replace("~", "-") # Replaces all '~' with '-'

## Writes the above changes into a temporary file then converts the file into a relaxed interleaved phylip file
with tempfile.TemporaryFile() as temp: # Creates the tempfile and opens it
    temp.write(data1) # Writes the above changes into the tempfile
    temp.seek(0) # Repositions the reading frame of Python
    temp = AlignIO.read(temp, "fasta") # Reads the tempfile into AlignIO
    AlignIO.write(temp, sys.argv[2], "phylip-relaxed") # Converts the tempfile

## Adds the 'I' signifier to the file so PAML
## knows the file is interleaved
with open(sys.argv[2], "r") as file: # Opens the file
    data2 = file.readlines() # Reads the file into memory as a list composed of each line
    data2[0] = data2[0].rstrip("\r\n") # Removes newline characters from the first line; should be OS nonspecific, but I haven't tested that
    data2[0] = data2[0] + " I\n" # Adds an 'I' and a newline character to the first line

# Writes the above changes into the file
with open(sys.argv[2], "w") as file:
    file.writelines( data2 )
