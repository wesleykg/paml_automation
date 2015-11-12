import re, tempfile, sys
from Bio import AlignIO

## Writes fasta_data into a temporary file then converts the file into a relaxed interleaved phylip file
        with tempfile.TemporaryFile() as temp_fasta: # Creates the tempfile and opens it
            temp_fasta.write(fasta_data) # Writes the above changes into the tempfile
            temp_fasta.seek(0) # Repositions the file reading frame of Python to the beginning
            temp_fasta_AlignIO = AlignIO.read(temp_fasta, "fasta") # Reads the tempfile into AlignIO
            AlignIO.write(temp_fasta_AlignIO, sys.argv[2], "phylip-relaxed") # Converts the tempfile

def paml_modifier(phylip_file):
    with open(phylip_file, "r+") as phylip_file: # Opens the file
        phylip_data = phylip_file.readlines() # Reads the file into memory as a list composed of each line
        phylip_data[0] = phylip_data[0].rstrip("\r\n") # Removes newline characters from the first line
        phylip_data[0] = phylip_data[0] + " I\n" # Adds an 'I' and a newline character to the first line
        phylip_file.seek(0)
        phylip_file.writelines(phylip_data) # Writes the above changes into the file

if __name__ == '__main__':
    file_cleaner_converter(sys.argv[1])
    paml_modifier(sys.argv[2])
