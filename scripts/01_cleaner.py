import re, sys
from Bio import SeqIO

gene_file = sys.argv[1]

## Fix common FASTA file problems
def fasta_cleaner(gene_file):
    with open(gene_file, "r+") as gene_file:
        gene_data = gene_file.read() #Reads the file into memory as a string
        
        ##Check for spaces in gene names/identifiers
        if " " in gene_data:
            sys.exit("Can't read files with spaces in gene names/identifiers")

        ##Convert '~' to '-'
        gene_data = gene_data.replace("~", "-")

        ##Convert to Unix line endings
        if "\r" in gene_data:
            if "\n" in gene_data:
                gene_data = gene_data.replace("\r\n", "\n") #Windows
            if "\n" not in gene_data:
                gene_data = gene_data.replace("\r", "\n") #Classic Mac
                
if __name__ == '__main__':
    fasta_cleaner(gene_file)