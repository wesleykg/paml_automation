import sys

gene_file = sys.argv[1]

def fasta_checker(gene_file):
    '''Report common FASTA file problems'''
    with open(gene_file, "r") as gene_file:
        ##Check for spaces in gene names/identifiers
        if " " in gene_file:
            sys.exit("Can't read files with spaces in gene names/identifiers")
            
        ##Check for '~' in place of '-'
        if '~' in gene_file:
            sys.exit("Replace '~' chracters with '-' characters")

     
if __name__ == '__main__':
    fasta_checker(gene_file)