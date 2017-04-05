library(tidyr)
suppressPackageStartupMessages(library(dplyr))

## Read in the raw results file
paml_results_dat <- read.csv(file = 'results/results.csv', header = FALSE, 
                       col.names = c(
                         'gene', 'method','lnL', 'bg-omega', 'fg-omega')
                       )

## Select just the LRT columns and make them wide format
LRTdat <- paml_results_dat %>% select(gene, method, lnL)
LRTdat <- spread(LRTdat, method, lnL)

## Record LRT result for each test type
LRTdat$BS2_LRT <- (LRTdat$alternative - LRTdat$null)*2
LRTdat$nratios_LRT <- (LRTdat$nratios - LRTdat$m0)*2

## Record chi^2 significance threshold for later tests
chisq_1df <- qchisq(.95, df = 1)

## Compare LRT to chi^2 value to test for significance. Write the significance
## result into the table
if (LRTdat$BS2_LRT > chisq_1df) {
  LRTdat$BS2_result = 'Significant'
} else {
  LRTdat$BS2_result = 'Not significant'
}

if (LRTdat$nratios_LRT > chisq_1df) {
  LRTdat$nratios_result = 'Significant'
} else {
  LRTdat$nratios_result = 'Not significant'
}

## Write significance results to file
write.csv(LRTdat, file = 'results/results_significant.csv')