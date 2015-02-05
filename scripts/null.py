from Bio.Phylo.PAML import codeml
import sys, os

script_rel_dir = os.getcwd()
paml_dir = os.path.join(os.path.relpath(os.path.dirname('paml/simple')), os.path.basename("paml/simple"))
working_dir = os.path.join(script_rel_dir, paml_dir)

cml = codeml.Codeml()
cml.working_dir = working_dir
print cml.working_dir
cml.alignment = os.path.join(working_dir, "simple.phy")
print cml.alignment
cml.tree = "simple.tre"
print cml.tree
cml.out_file = os.path.join(working_dir, "mlc")
print cml.out_file

cml.set_options(CodonFreq = 2)
cml.set_options(NSsites = [2])
cml.set_options(fix_omega = 1)
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

results = cml.run(verbose = True)

lnL = results["NSsites"][2]["lnL"]

name = os.path.split(working_dir)[1]
results_file = os.path.join(working_dir, "lnL_null_" + name + ".txt")

with open(results_file, "w") as file:
    file.write(str(lnL))
