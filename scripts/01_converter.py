import re, tempfile
from Bio import AlignIO

## Prep the file for PAML by removing stop codons and standardizing gap characters
with open("seq1.fasta", "r") as file: # Opens the file
    data1 = file.read() # Reads the file into memory as a string
    data1 = re.sub("TAA(?=\n>|\n\Z)|TAG(?=\n>|\n\Z)|TGA(?=\n>|\n\Z)", "???", data1, flags = re.IGNORECASE) # Replaces stop codons with ???
    data1 = data1.replace("~", "-") # Replaces all '~' with '-'

## Writes the above changes into a temporary file then converts the file into a relaxed interleaved phylip file
with tempfile.TemporaryFile() as temp:
    temp.write(data1)
    temp.seek(0)
    temp = AlignIO.read(temp, "fasta")
    AlignIO.write(temp, "seq1.phy", "phylip-relaxed")

## Adds the 'I' signifier to the file so PAML
## knows the file is interleaved, not sequential
with open("seq1.phy", "r+") as file: # Opens the file
    data2 = file.readlines() # Reads the file into memory as a list composed of each line
    data2[0] = data2[0].rstrip("\r\n") # Removes newline characters from the first line; should be OS nonspecific, but I haven't tested that
    data2[0] = data2[0] + " I\n" # Adds an 'I' and a newline character to the first line

# Writes the above changes into the file
with open("seq1.phy", "r+") as file:
    file.writelines( data2 )
