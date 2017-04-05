library(tidyr)

paml_results_dat <- read.csv(file = '../results/results.csv', header = FALSE, 
                       col.names = c(
                         'gene', 'method','lnL')
                       )

paml_results_dat <- spread(paml_results_dat, method, lnL)

paml_results_dat$BS2_LRT <- (paml_results_dat$alternative - 
                               paml_results_dat$null)*2

paml_results_dat$nratios_LRT <- (paml_results_dat$nratios - 
                               paml_results_dat$m0)*2

chisq_1df <- qchisq(.95, df = 1)

if (paml_results_dat$BS2_LRT > chisq_1df) {
  paml_results_dat$BS2_result = 'Significant'
} else {
  paml_results_dat$BS2_result = 'Not significant'
}

if (paml_results_dat$nratios_LRT > chisq_1df) {
  paml_results_dat$nratios_result = 'Significant'
} else {
  paml_results_dat$nratios_result = 'Not significant'
}

write.csv(paml_results_dat, file = '../results/results_significant.csv')