import argparse
from Bio import AlignIO

parser = argparse.ArgumentParser()
parser.add_argument('alignment_path', help = 'Path to the alignment file')
parser.add_argument('-f', '--filetype', help = 'Select filetype', 
                    default = 'fasta')
args = parser.parse_args()

alignment_file = args.alignment_path
in_filetype = args.filetype

def fasta_check_python(alignment_file):
    '''Report common FASTA file problems using base python libraries'''
    with open(alignment_file, 'r') as alignment:
        for line in alignment:
            
            #Check for spaces in gene names/identifiers
            assert (" " not in line), 'Spaces in gene names/identifiers'
            #Check for '~' in place of '-'
            assert("~" not in line), "Invalid character '~'"
                
def fasta_check_biopython(alignment_file, in_filetype):
    '''Report common FASTA file problems using Biopython libraries'''
    alignment = AlignIO.read(alignment_file, in_filetype)
    for record in alignment:
        
        #Checks that the genes are in reading frame for PAML (multiples of 3)
        assert (len(record.seq) % 3 == 0), 'Incorrect reading frame for PAML'
        
        #Checks that genes don't end with stop codons
        assert (not record.seq.endswith(('TAA', 
                                        'TGA', 
                                        'TAG')) \
                                        ), 'Stop codon present'

if __name__ == '__main__':
    fasta_check_python(alignment_file)
    fasta_check_biopython(alignment_file, in_filetype)