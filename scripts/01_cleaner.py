import sys
from Bio import AlignIO

alignment_file = sys.argv[1]
in_filetype = 'fasta'

def fasta_check_python(alignment_file):
    '''Report common FASTA file problems using base python libraries'''
    with open(alignment_file, "r") as alignment:
        for line in alignment:
            
            ##Check for spaces in gene names/identifiers
            if " " in line:
                sys.exit('''Can't read files with spaces 
                            in gene names/identifier''')
            
            ##Check for '~' in place of '-'
            if '~' in line:
                sys.exit("Please replace '~' chracters with '-' characters.")

def fasta_check_biopython(alignment_file, in_filetype):
    '''Report common FASTA file problems using Biopython libraries'''
    alignment = AlignIO.read(alignment_file, in_filetype)
    print(alignment)
    

if __name__ == '__main__':
    fasta_check_python(alignment_file)
    fasta_check_biopython(alignment_file, in_filetype)