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
    in_alignment_file = '../ALB4_3968_aligned.fasta'

# Retrieves filename to produce the name for the converted alignment and the
# filetype
alignment_name = os.path.splitext(in_alignment_file)[0]
out_alignment_filename = alignment_name + '.phy'
filetype = os.path.splitext(in_alignment_file)[1]
filetype = filetype[1:]  # remove the '.' of the file type

# Check for PAML input problems
alignment = AlignIO.read(in_alignment_file, filetype)
for record in alignment:

    # Check for species names longer than 50 characters
    assert (len(record.id) < 51), 'One or more species names are too long'

    # Checks that the genes are in the correct reading frame
    assert (len(record.seq) % 3 == 0), 'Bases in the alignment must be a \
multiple of 3, your alignment is in an incorrect reading frame'

    # Checks for stop codons
    assert (not record.seq.endswith(
            ('TAA', 'taa', 'TGA', 'tga', 'TAG', 'tag'))), \
        'Stop codon(s) present'

# Converts the file into an interleaved phylip file.
AlignIO.convert(in_alignment_file, filetype, out_alignment_filename,
                'phylip-relaxed')

# Adds an 'I' character to the first line for PAML. This indicates to PAML that
# the alignment is interleaved.
with open(out_alignment_filename, "r+") as phy_file:
    alignment = phy_file.readlines()  # List comprising each line
    alignment[0] = alignment[0].rstrip("\r\n")  # Remove first newline
    alignment[0] = alignment[0] + " I\n"  # Add 'I' and a newline character
    phy_file.seek(0)  # Go back to the start of the file
    phy_file.writelines(alignment)  # Rewrite the file
