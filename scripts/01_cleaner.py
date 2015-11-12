import re, sys

gene_file = "../genes/simple.fasta" #Temp test file location

def cleaner(gene_file):
    with open(gene_file, "r") as gene_file: # pens the file
        gene_data = gene_file.read() #Reads the file into memory as a string
        
        ## Check for spaces in gene names/identifiers
        if " " in gene_data:
            sys.exit("Can't read files with spaces in gene names/identifiers")
        
        ## Check gene is in multiple of threes
            
        ## Convert to Unix line endings
        if "\r" in gene_data:
            if "\n" in gene_data:
                gene_data = gene_data.replace("\r\n", "\n") #Windows
            if "\n" not in gene_data:
                gene_data = gene_data.replace("\r", "\n") #Classic Mac
                
        ## Convert stop codons to ambiguity characters
        gene_data = re.sub("TAA(?=\n>|\n\n|\n\Z)|TAG(?=\n>|\n\n|\n\Z)|TGA(?=\n>|\n\n|\n\Z)", "???", gene_data, flags = re.IGNORECASE) # Replaces stop codons with ???
        gene_data = gene_data.replace("~", "-") # Replaces all '~' with '-'

if __name__ == '__main__':
    file_cleaner_converter(sys.argv[1])