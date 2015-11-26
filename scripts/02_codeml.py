from Bio.Phylo.PAML import codeml
import os, argparse

#argparse module
parser = argparse.ArgumentParser() #Initializes argparse
parser.add_argument('alignment_path', help = 'Path to the alignment file')
parser.add_argument('tree_path', help = 'Path to the tree file')
parser.add_argument('model', help = 'Specify which model to test')
parser.add_argument('-c', '--cleandata', help = 'Ignore gap-columns', 
                    default = 0)
parser.add_argument('-f', '--fix_blength', help = '''Modify initial 
                    likelihood estimate''', default = 0)
parser.add_argument('-SE', '--getSE', help = 'Test for standard errors', 
                    default = 0)
parser.add_argument('-a', '--RateAncestor', help = '''Test for rates and 
                    ancestral sequences''', default = 0)
parser.add_argument('-i', '--icode', help = '''Specify the genetic code for 
                    ancestral state''', default = 0)
args, unknown = parser.parse_known_args() #Read valid arguments into 'args'

##Set command-line arguments to variables
#Alignment
alignment_file = args.alignment_path
gene_name = alignment_file[:-4] #Filename without .phy suffix
alignment_dir = os.path.join('results/' + gene_name)

#Tree
tree_file = args.tree_path

#Method
method = args.model
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

#Optionals
cleandata = args.cleandata
fix_blength = args.fix_blength
getSE = args.getSE
RateAncestor = args.RateAncestor
icode = args.icode

#codeml module
cml = codeml.Codeml()
cml.working_dir = os.path.join(alignment_dir, method)
cml.alignment = os.path.join(alignment_dir, alignment_file)
cml.tree = tree_file
cml.out_file = os.path.join(cml.working_dir, "mlc")

##Sets codeml options
#Model-specific
cml.set_options(model = model)
cml.set_options(NSsites = NSsites)
cml.set_options(fix_omega = fix_omega)

#Optional settings
cml.set_options(cleandata = cleandata)
cml.set_options(fix_blength = fix_blength)
cml.set_options(getSE = getSE)
cml.set_options(RateAncestor = RateAncestor)
cml.set_options(icode = icode)

#Permanent settings
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
results = cml.run(verbose = False)

#Retrieves results
NSsites_dict = results.get('NSsites')
if method == "alternative":
    alternative_dict = NSsites_dict.get(2)
    lnL_value = alternative_dict.get('lnL')
elif method == "null":
    null_dict = NSsites_dict.get(2)
    lnL_value = null_dict.get('lnL')
elif method == "m1":
    m1_dict = NSsites_dict.get(1)
    lnL_value = m1_dict.get('lnL')
elif method == "m0":
    m0_dict = NSsites_dict.get(0)
    lnL_value = m0_dict.get('lnL')
elif method == "nratios":
    nratios_dict = NSsites_dict.get(0)
    lnL_value = nratios_dict.get('lnL')

results_filename = os.path.join(alignment_dir, method + 
                                "_" + gene_name + ".csv")
                                
codeml_data = gene_name + "," + method + "," + str(lnL_value) + '\n'

with open(results_filename, "w") as lnL_file:
    lnL_file.write(codeml_data)