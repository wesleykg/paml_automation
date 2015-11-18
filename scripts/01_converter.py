import argparse
from Bio import AlignIO

#argparse module
parser = argparse.ArgumentParser()
parser.add_argument('alignment_path', help = 'Path to the alignment file')
parser.add_argument('out_phyname', help = 'Name for the phylip file')
parser.add_argument('-f', '--filetype', help = 'Specify the filetype', 
                    default = 'fasta')
args = parser.parse_args()

#Variables
in_alignment_file = args.alignment_path
in_filetype = args.filetype

out_phy_file = args.out_phyname
out_filetype = 'phylip-relaxed'

def file_check(in_alignment_file, in_filetype):
    '''Check for common FASTA file problems'''
    
    #Base Python
    with open(in_alignment_file, 'r') as alignment:
        for line in alignment:
            
            #Check for spaces in gene names/identifiers
            assert (" " not in line), 'Spaces in gene names/identifiers'
    
    #Biopython
    alignment = AlignIO.read(in_alignment_file, in_filetype)
    for record in alignment:
        
        #Checks that the genes are in reading frame for PAML (multiples of 3)
        assert (len(record.seq) % 3 == 0), 'Incorrect reading frame for PAML'
        
        #Checks that genes don't end with stop codons
        ##KNOWN BUG: CAN"T DEAL WITH LOWERCASE
        ##FIX: Translate first, then check for '*' characters
        assert (not record.seq.endswith(('TAA', 
                                        'TGA', 
                                        'TAG')) \
                                        ), 'Stop codon(s) present'

def converter(in_alignment_file, in_filetype, out_phy_file, out_filetype):
    print in_alignment_file
    print in_filetype
    print out_phy_file
    print out_filetype
##INCOMPLETE; NOT WORKING
#def I_adder(in_alignment_file):
#    with open(in_alignment_file, "r+") as in_alignment_file: # Opens the file
#        alignment = in_alignment_file.readlines() # Reads the file into memory as a list composed of each line
#        alignment[0] = alignment[0].rstrip("\r\n") # Removes newline characters from the first line
#        alignment[0] = alignment[0] + " I\n" # Adds an 'I' and a newline character to the first line
#        in_alignment_file.seek(0)
#        in_alignment_file.writelines(alignment) # Writes the above changes into the file

if __name__ == '__main__':
    file_check(in_alignment_file, in_filetype)
    converter(in_alignment_file, in_filetype, out_phy_file, out_filetype)