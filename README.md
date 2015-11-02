#paml_automation#
---

This set of scripts allows you to automate running codeml from PAML and in the future analyze these results and put them into a table.

##Program Requirements##

1. Python & Biopython
3. R & dplyr
4. GNU Make and base UNIX commands

##Data Requirements##

1. Multi-sequence alignments in FASTA format (filetype ending .fasta)
2. A single Newick style phylogenetic tree (filetype ending .tre) with the same tip names as sequence identifiers in your FASTA file

###Usage###

1. Clone/download this repository
2. Place all sequence files and tree file in the root directory of the project
  * FASTA files must use the .fasta filetype
  * Tree files must use the .tre filetype
3. Open a terminal window and `cd` to the project directory
4. Type `make` followed by `method=` any of the following commands to execute the program
  * `branchsites1`: Run Branch-Sites Test 1
  * `branchsites2`: Run Branch-Sites Test 2
  * `both`: Runs Branch-Sites Test 1 & 2
  * `branch`: Run Branch Test
  * `alternative`: Run the alternative model of Branch-Sites Test 1 & 2
  * `null`: Run the null model of Branch-Sites Test 2
  * `m1`: Run the null model of Branch-Sites Test 1
  * `m0`: Run the one-ratio model of Branch Test
  * `nratios`: Run the n-ratio model of Branch Test
  * `clean`: Removes any files created by make

---

###Completed features:###

* Input a fasta file with any name and convert it into a phylip file suitable for use in PAML
* Run Branch-Sites Test 1 & 2
* Write results into a .csv file

###Features to be added:###

* Analyze results using R
* Create a table with results
A line I wrote on my mac-air
A second line I wrote on my mac-air
