import argparse
from Bio import AlignIO

#argparse module
parser = argparse.ArgumentParser() #Initializes argparse
parser.add_argument('alignment_path', help = 'Path to the alignment file')
parser.add_argument('out_phyname', help = 'Name for the phylip file')
parser.add_argument('-f', '--filetype', help = 'Specify the filetype', 
                    default = 'fasta')
args, unknown = parser.parse_known_args() #Read valid arguments into 'args'

#Set command-line arguments to variables
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
    '''Convert the alignment into phylip format for PAML'''
    AlignIO.convert(in_alignment_file, in_filetype, out_phy_file, out_filetype)

    #Adds an 'I' character to the first line for PAML    
    with open(out_phy_file, "r+") as phy_file:
        alignment = phy_file.readlines() #List comprising each line
        alignment[0] = alignment[0].rstrip("\r\n") #Remove newline from line 1
        alignment[0] = alignment[0] + " I\n" #Add 'I' and newline
        phy_file.seek(0) #Go back to the start of the file
        phy_file.writelines(alignment) #Rewrite the file

if __name__ == '__main__':
    file_check(in_alignment_file, in_filetype)
    converter(in_alignment_file, in_filetype, out_phy_file, out_filetype)