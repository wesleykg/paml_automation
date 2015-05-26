gene_name <- commandArgs(trailingOnly = TRUE)[1]

path <- commandArgs(trailingOnly = TRUE)[2]

type <- commandArgs(trailingOnly = TRUE)[3]

filename <- paste0(path, "/lnL_", type, "_", gene_name, ".csv")

data_name <- read.csv(filename)

print (data_name)
