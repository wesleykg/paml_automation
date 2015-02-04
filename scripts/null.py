from Bio.Phylo.PAML import codeml
import sys, os

cml = codeml.Codeml()
cml.alignment = sys.argv[1]
cml.tree = "simple.tre"
cml.out_file = "mlc"

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

name = os.path.split(os.getcwd())[1]
print name
results_file = "lnL_null_" + name + ".txt"

with open(results_file, "w") as file:
    file.write(str(lnL))
