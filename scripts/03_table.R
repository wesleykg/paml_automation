library(tidyr)

paml_results.dat <- read.csv(file = '../results/results.csv', header = FALSE, 
                       col.names = c(
                         'gene', 'method','lnL')
                       )

paml_results.dat <- spread(paml_results.dat, method, lnL)

paml_results.dat$BS2_LRT <- (paml_results.dat$alternative - 
                               paml_results.dat$null)*2

paml_results.dat$nratios_LRT <- (paml_results.dat$nratios - 
                               paml_results.dat$m0)*2

chisq_1df <- qchisq(.95, df = 1)

if (paml_results.dat$BS2_LRT > chisq_1df) {
  paml_results.dat$BS2_result = 'Significant'
} else {
  paml_results.dat$BS2_result = 'Not significant'
}

if (paml_results.dat$nratios_LRT > chisq_1df) {
  paml_results.dat$nratios_result = 'Significant'
} else {
  paml_results.dat$nratios_result = 'Not significant'
}
