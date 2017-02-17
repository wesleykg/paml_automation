'''Usage: 01_converter.py <alignment>'''

import os  # Manipulating filenames
from Bio import AlignIO  # Converting alignments


# Check if running interactively in an iPython console, or in a script
# from the command-line
def in_ipython():
    try:
        __IPYTHON__
        return True
    except NameError:
        return False
# Run in a script from the command-line
if in_ipython() is False:
    from docopt import docopt  # Command-line argument handler
    cmdln_args = docopt(__doc__)
    in_alignment_file = cmdln_args.get('<alignment>')
# Run interatively in an iPython console
if in_ipython() is True:
    in_alignment_file = '../cpSECA2_1865_aligned_paml.fasta'

alignment_name = os.path.splitext(in_alignment_file)[0]
out_alignment_filename = alignment_name + '.phy'
filetype = os.path.splitext(in_alignment_file)[1]
filetype = filetype[1:]  # remove the '.' of the file type

# Check for problems using Base Python
#with open(in_alignment_file, 'r') as alignment:
#    for line in alignment:

        # Check for spaces in gene names/identifiers
        #assert (" " not in line), 'Spaces in gene names/identifiers'

# Check for problems using Biopython
alignment = AlignIO.read(in_alignment_file, filetype)
for record in alignment:

    assert (len(record.seq) < 51), 'One or more species names are too long'

    #Checks that the genes are in reading frame for PAML (multiples of 3)
    assert (len(record.seq) % 3 == 0), 'Incorrect reading frame for PAML'

    # Checks that genes don't end with stop codons
    # KNOWN BUG: CAN"T DEAL WITH LOWERCASE
    # FIX: Translate first, then check for '*' characters
    assert (not record.seq.endswith(('TAA', 'TGA', 'TAG'))), \
        'Stop codon(s) present'

# Converts the file
AlignIO.convert(in_alignment_file, filetype, out_alignment_filename,
                'phylip-relaxed')

# Adds an 'I' character to the first line for PAML
with open(out_alignment_filename, "r+") as phy_file:
    alignment = phy_file.readlines()  # List comprising each line
    alignment[0] = alignment[0].rstrip("\r\n")  # Remove first newline
    alignment[0] = alignment[0] + " I\n"  # Add 'I' and newline
    phy_file.seek(0)  # Go back to the start of the file
    phy_file.writelines(alignment)  # Rewrite the file
