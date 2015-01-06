from Bio import AlignIO

## Converts aligned FASTA file into an interleaved relaxed phylip file
AlignIO.convert("seq1.fasta", "fasta", "seq1.phy", "phylip-relaxed")


def chomps(s):
    return s.rstrip('\n')
## Adds the 'I' signifier to the file so PAML
## knows the file is interleaved, not sequential
with open("seq1.phy", "r+") as foo:
	data = foo.readlines()
	chomps(data)
	data[0] += " I"
