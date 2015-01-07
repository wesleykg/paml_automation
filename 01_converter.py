from Bio import AlignIO

## Converts aligned FASTA file into an interleaved relaxed phylip file
AlignIO.convert("seq1.fasta", "fasta", "seq1.phy", "phylip-relaxed")

## Adds the 'I' signifier to the file so PAML
## knows the file is interleaved, not sequential

with open("seq1.phy", "r+") as file: # Opens the file
	data = file.readlines() # Reads the file into memory

data[0] = data[0].rstrip("\n") # Removes the newline character from the first line
data[0] = data[0] + " I\n" # Adds an I and a newline character to the first line

# Writes the above changes into the file
with open("seq1.phy", "r+") as file:
	file.writelines( data )
