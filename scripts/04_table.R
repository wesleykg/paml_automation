suppressPackageStartupMessages(library(dplyr))

lnL_results <- read.csv(file = "results/results.csv", header = FALSE, 
												col.names = c("gene", "method", "lnL")
												)

lnL_results %>%
  select(method) %>%
  

lnL_results %>%
  filter(method %in% c("alternative", "null")) %>%
  group_by(gene) %>%
  mutate(LRT = -2*(lnL - lnL))


If data contains "null" and "alternative":
	mutate() a new column of an LRT between each alternative and null
	then compare data in that column to chi square distribution 
	to produce p value

