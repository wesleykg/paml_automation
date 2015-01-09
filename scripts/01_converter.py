## Converts any '~' characters into '-' characters
with open("seq1.fasta", "r+") as file: # Opens the file
	data = file.read() # Reads the file into memory as a string

data = data.replace("~", "-") # Replaces all '~' with '-'

# Writes the above changes into the file
with open("seq1.fasta", "r+") as file:
	file.writelines( data )

from Bio import AlignIO

## Converts aligned FASTA file into an interleaved relaxed phylip file
AlignIO.convert("seq1.fasta", "fasta", "seq1.phy", "phylip-relaxed")

## Adds the 'I' signifier to the file so PAML
## knows the file is interleaved, not sequential
with open("seq1.phy", "r+") as file: # Opens the file
	data = file.readlines() # Reads the file into memory as a list composed of each line

data[0] = data[0].rstrip("\r\n") # Removes newline characters from the first line; should be OS nonspecific, but I haven't tested that
data[0] = data[0] + " I\n" # Adds an 'I' and a newline character to the first line

# Writes the above changes into the file
with open("seq1.phy", "r+") as file:
	file.writelines( data )
