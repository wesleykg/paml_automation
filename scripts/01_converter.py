import argparse
from Bio import AlignIO

parser = argparse.ArgumentParser()
parser.add_argument('alignment_path', help = 'Path to the alignment file')
parser.add_argument('-f', '--filetype', help = 'Select filetype', 
                    default = 'fasta')
args = parser.parse_args()

alignment_file = args.alignment_path
in_filetype = args.filetype
out_filetype = 'phylip-relaxed'

def file_check(alignment_file, in_filetype):
    '''Check for common FASTA file problems'''
    
    #Base Python
    with open(alignment_file, 'r') as alignment:
        for line in alignment:
            
            #Check for spaces in gene names/identifiers
            assert (" " not in line), 'Spaces in gene names/identifiers'
    
    #Biopython
    alignment = AlignIO.read(alignment_file, in_filetype)
    for record in alignment:
        
        #Checks that the genes are in reading frame for PAML (multiples of 3)
        assert (len(record.seq) % 3 == 0), 'Incorrect reading frame for PAML'
        
        #Checks that genes don't end with stop codons
        ##KNOWN BUG: CAN"T DEAL WITH LOWERCASE
        assert (not record.seq.endswith(('TAA', 
                                        'TGA', 
                                        'TAG')) \
                                        ), 'Stop codon(s) present'

##INCOMPLETE; NOT WORKING
#def I_adder(alignment_file):
#    with open(alignment_file, "r+") as alignment_file: # Opens the file
#        alignment = alignment_file.readlines() # Reads the file into memory as a list composed of each line
#        alignment[0] = alignment[0].rstrip("\r\n") # Removes newline characters from the first line
#        alignment[0] = alignment[0] + " I\n" # Adds an 'I' and a newline character to the first line
#        alignment_file.seek(0)
#        alignment_file.writelines(alignment) # Writes the above changes into the file

if __name__ == '__main__':
    file_check(alignment_file, in_filetype)