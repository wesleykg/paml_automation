from Bio.Phylo.PAML import codeml
import os, argparse

#argparse module
parser = argparse.ArgumentParser() #Initializes argparse
parser.add_argument('alignment_path', help = 'Path to the alignment file')
parser.add_argument('tree_path', help = 'Path to the tree file')
parser.add_argument('model', help = 'Specify which model to test')
args, unknown = parser.parse_known_args() #Read valid arguments into 'args'

#Setting command-line arguments to variables
alignment_file = args.alignment_path
gene_name = alignment_file[:-4] #Filename without .phy suffix
tree_file = args.tree_path
method = args.model

project_dir = os.getcwd() # Absolute path to the project directory
gene_dir = os.path.join("results", gene_name) # Relative path to the gene directory
working_dir = os.path.join(project_dir, gene_dir) # Absolute path to the gene directory

if method == "alternative":
    model = 2
    NSsites = [2]
    fix_omega = 0
elif method == "null":
    model = 2
    NSsites = [2]
    fix_omega = 1
elif method == "m1":
    model = 0
    NSsites = [1]
    fix_omega = 0
elif method == "m0":
    model = 0
    NSsites = [0]
    fix_omega = 0
elif method == "nratios":
    model = 2
    NSsites = [0]
    fix_omega = 0

#codeml module
cml = codeml.Codeml()
cml.working_dir = os.path.join(working_dir, method)
cml.alignment = os.path.join(working_dir, alignment_file)
cml.tree = os.path.join(project_dir, tree_file)
cml.out_file = os.path.join(cml.working_dir, "mlc")

##Sets codeml options
#Specified above
cml.set_options(model = model)
cml.set_options(NSsites = NSsites)
cml.set_options(fix_omega = fix_omega)

#Change sometimes
cml.set_options(cleandata = 0) #Remove gap columns
cml.set_options(fix_blength = 0) #Modify starting likelihood estimate
cml.set_options(getSE = 0) #Print standard errors
cml.set_options(RateAncestor = 0)
cml.set_options(icode = 0) #Set genetic code

#Change never
cml.set_options(CodonFreq = 2)
cml.set_options(clock = 0)
cml.set_options(ncatG = 5)
cml.set_options(runmode = 0)
cml.set_options(fix_kappa = 0)
cml.set_options(fix_alpha = 1)
cml.set_options(Small_Diff = 5e-08)
cml.set_options(method = 0)
cml.set_options(Malpha = 0)
cml.set_options(alpha = 0.0)
cml.set_options(seqtype = 1)
cml.set_options(omega = 1)
cml.set_options(noisy = 9)
cml.set_options(Mgene = 0)
cml.set_options(kappa = 2)
cml.set_options(ndata = 1)

#Runs codeml and stores the results
results = cml.run(verbose = True)

#Retrieves final lnL
if method == "alternative":
    lnL_result = results["NSsites"][2]["lnL"]
elif method == "null":
    lnL_result = results["NSsites"][2]["lnL"]
elif method == "m1":
    lnL_result = results["NSsites"][1]["lnL"]
elif method == "m0":
    lnL_result = results["NSsites"][0]["lnL"]
elif method == "nratios":
    lnL_result = results["NSsites"][0]["lnL"]

## Stores the results_filename
results_filename = os.path.join(working_dir, "lnL_" + method + "_" + gene_name + ".csv")

with open(results_filename, "w") as file: # Creates the file for writing
    data = gene_name + "," + method + "," + str(lnL_result) + '\n' # Adds the data as a second line
    file.write(data) # Writes the log-likelihood to file
