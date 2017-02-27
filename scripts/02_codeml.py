'''Usage: 02_codeml.py <alignment> <tree> <method> [<clean_data>] \
[<fix_blength>]'''

from Bio.Phylo.PAML import codeml
import os


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
    alignment_file = cmdln_args.get('<alignment>')
    tree_file = cmdln_args.get('<tree>')
    method = cmdln_args.get('<method>')
    clean_data = cmdln_args.get('[<clean_data>]')
    fix_blength = clean_data = cmdln_args.get('[<fix_blength>]')
# Run interatively in an iPython console
if in_ipython() is True:
    alignment_file = 'ALB4_3968_aligned.phy'
    tree_file = '../RAxML_bestTree.ALB4_3968_aligned_ML_2017-01-31.tre'
    method = 'm0'
    clean_data = 0
    fix_blength = 0

gene_name = os.path.splitext(alignment_file)[0]  # Filename without .phy suffix
alignment_dir = os.path.join('../results/' + gene_name)

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

# codeml module
cml = codeml.Codeml()
cml.working_dir = os.path.join(alignment_dir, method)
cml.alignment = os.path.join(alignment_dir, alignment_file)
cml.tree = tree_file
cml.out_file = os.path.join(cml.working_dir, "mlc")

# Sets codeml options:
# 1.Model-specific
cml.set_options(model=model)
cml.set_options(NSsites=NSsites)
cml.set_options(fix_omega=fix_omega)

# 2. Optional settings
cml.set_options(cleandata=clean_data)
cml.set_options(fix_blength=fix_blength)

# 3. Permanent settings
cml.set_options(getSE=0)
cml.set_options(RateAncestor=0)
cml.set_options(icode=0)
cml.set_options(CodonFreq=2)
cml.set_options(clock=0)
cml.set_options(ncatG=5)
cml.set_options(runmode=0)
cml.set_options(fix_kappa=0)
cml.set_options(fix_alpha=1)
cml.set_options(Small_Diff=5e-08)
cml.set_options(method=0)
cml.set_options(Malpha=0)
cml.set_options(alpha=0.0)
cml.set_options(seqtype=1)
cml.set_options(omega=1)
cml.set_options(noisy=9)
cml.set_options(Mgene=0)
cml.set_options(kappa=2)
cml.set_options(ndata=1)

# Runs codeml and stores the results
results = cml.run(verbose=True)

# Retrieve results
NSsites_dict = results.get('NSsites')
if method == "alternative":
    model_dict = NSsites_dict.get(2)
    lnL_value = model_dict.get('lnL')
    codeml_data = gene_name + ',' + method + ',' + str(lnL_value) + '\n'
elif method == "null":
    model_dict = NSsites_dict.get(2)
    lnL_value = model_dict.get('lnL')
    codeml_data = gene_name + ',' + method + ',' + str(lnL_value) + '\n'
elif method == "m1":
    model_dict = NSsites_dict.get(1)
    lnL_value = model_dict.get('lnL')
    codeml_data = gene_name + ',' + method + ',' + str(lnL_value) + '\n'
elif method == "m0":
    model_dict = NSsites_dict.get(0)
    lnL_value = model_dict.get('lnL')
    param_dict = model_dict.get('parameters')
    bg_omega_value = param_dict.get('omega')
    codeml_data = gene_name + ',' + method + ',' + str(lnL_value) + ',' + \
        str(bg_omega_value) + '\n'
elif method == "nratios":
    model_dict = NSsites_dict.get(0)
    lnL_value = model_dict.get('lnL')
    param_dict = model_dict.get('parameters')
    omega_values = param_dict.get('omega')
    bg_omega_value = omega_values[0]
    fg_omega_value = omega_values[1]
    codeml_data = gene_name + ',' + method + ',' + str(lnL_value) + ',' + \
        str(bg_omega_value) + ',' + str(fg_omega_value) + '\n'

results_filename = os.path.join(alignment_dir, method +
                                "_" + gene_name + ".csv")

with open(results_filename, "w") as lnL_file:
    lnL_file.write(codeml_data)
