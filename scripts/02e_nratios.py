from Bio.Phylo.PAML import codeml
import sys, os

gene_name = sys.argv[1] # Store the gene filename as a string
gene_name = gene_name[:-4] # Removes the .phy suffix from the gene filename

project_dir = os.getcwd() # Absolute path to the project directory
gene_dir = os.path.join("results", gene_name) # Relative path to the gene directory
working_dir = os.path.join(project_dir, gene_dir) # Absolute path to the gene directory

## Initializes codeml module
cml = codeml.Codeml()
cml.working_dir = os.path.join(working_dir, "nratios")
cml.alignment = os.path.join(working_dir, sys.argv[1])
cml.tree = os.path.join(project_dir, sys.argv[2])
cml.out_file = os.path.join(cml.working_dir, "mlc")

## Sets codeml options
cml.set_options(CodonFreq = 2)
cml.set_options(NSsites = [0])
cml.set_options(fix_omega = 0)
cml.set_options(clock = 0)
cml.set_options(ncatG = 5)
cml.set_options(runmode = 0)
cml.set_options(fix_kappa = 0)
cml.set_options(fix_alpha = 1)
cml.set_options(Small_Diff = 5e-08)
cml.set_options(method = 0)
cml.set_options(Malpha = 0)
cml.set_options(RateAncestor = 0)
cml.set_options(icode = 0)
cml.set_options(alpha = 0.0)
cml.set_options(seqtype = 1)
cml.set_options(omega = 1)
cml.set_options(getSE = 0)
cml.set_options(noisy = 9)
cml.set_options(Mgene = 0)
cml.set_options(kappa = 2)
cml.set_options(model = 2)
cml.set_options(ndata = 1)
cml.set_options(cleandata = 0)
cml.set_options(fix_blength = 0)

## Runs codeml
results = cml.run(verbose = True)

## Stores the results_filename
results_filename = os.path.join(working_dir, "lnL_nratios_" + gene_name + ".csv")

with open(results_filename, "w") as file: # Creates the file for writing
    data = gene_name + ",nratios," + str(results["NSsites"][0]["lnL"]) + '\n' # Adds the data as a second line
    file.write(data) # Writes the log-likelihood to file
