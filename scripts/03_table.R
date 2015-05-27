lnL_results <- read.csv(file = "results/results.csv", 
												header = FALSE, 
												col.names = c("gene", "method", "lnL")
												)

If data contains "null" and "alternative":
	mutate() a new column of an LRT between each alternative and null
	then compare data in that column to chi square distribution 
	to produce p value