library(tidyr)
suppressPackageStartupMessages(library(dplyr))

## Read in the raw results file
paml_results_dat <- read.csv(file = 'results/results.csv', header = FALSE, 
                       col.names = c(
                         'gene', 'method','lnL', 'nratios_bg-omega', 
                         'nratios_fg-omega', 'site_classes_0_proportion', 
                         'site_classes_0_bg_omega', 'site_classes_0_fg_omega',
                         'site_classes_1_proportion', 'site_classes_1_bg_omega',
                         'site_classes_1_fg_omega', 
                         'site_classes_2a_proportion',
                         'site_classes_2a_bg_omega', 'site_classes_2a_fg_omega',
                         'site_classes_2b_proportion', 
                         'site_classes_2b_bg_omega', 'site_classes_2b_fg_omega'
                                    )
                            )

## Select just the LRT columns and make them wide format
LRTdat <- paml_results_dat %>% select(gene, method, lnL)
LRTdat <- spread(LRTdat, method, lnL)

## Record LRT result for each test type
if ("bsA_alternative" %in% colnames(LRTdat)) {
  LRTdat$bsA_LRT <- (LRTdat$bsA_null - LRTdat$bsA_alternative)*-2
}
if ("nratios" %in% colnames(LRTdat)){
  LRTdat$branch_LRT <- (LRTdat$m0 - LRTdat$nratios)*-2
}
if ("CmC" %in% colnames(LRTdat)){
  LRTdat$CmC_LRT <- (LRTdat$m2a_rel - LRTdat$CmC)*-2
}
if ("CmD" %in% colnames(LRTdat)){
  LRTdat$CmD_LRT <- (LRTdat$m3 - LRTdat$CmD)*-2
}
## Record chi^2 significance threshold for later tests
# chisq_1df <- qchisq(.95, df = 1)

## Compare LRT to chi^2 value to test for significance. Write the significance
## result into the table
# if (LRTdat$BS2_LRT > chisq_1df) {
#   LRTdat$BS2_result = 'Significant'
# } else {
#   LRTdat$BS2_result = 'Not significant'
# }
# 
# if (LRTdat$branch_LRT > chisq_1df) {
#   LRTdat$branch_result = 'Significant'
# } else {
#   LRTdat$branch_result = 'Not significant'
# }

## Write significance results to file
write.csv(LRTdat, file = 'results/results_LRT.csv', row.names = FALSE)