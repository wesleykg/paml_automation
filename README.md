#paml_automation#
---

This set of scripts allows you to run Branch-Sites Test 1 and 2 in PAML and in the future analyze these results and put them into a table.

##Requirements##

1. Python and BioPython Installed
2. GNU Make and base UNIX commands installed
3. Multi-sequence alignments in FASTA format (filetype ending .fasta)
4. A single Newick style phylogenetic tree (filetype ending .tre) with the same tip names as sequence identifiers in your FASTA file

###Usage###

1. Clone/download this repository
2. Place all sequence files and tree file in the root directory of the project
  * FASTA files must use the .fasta filetype
  * Tree files must use the .tre filetype
3. Open a terminal window and `cd` to the project directory
4. Type `make` followed by any of the following commands to execute the program
  * `all`: Runs Branch-Sites Test 1 & 2
  * `branchsites1`: Run Branch-Sites Test 1
  * `branchsites2`: Run Branch-Sites Test 2
  * `alternative`: Run the alternative model of Branch-Sites Test 1 & 2
  * `null`: Run the null model of Branch-Sites Test 2
  * `m1`: Run the null model of Branch-Sites Test1
  * `clean`: Removes any files created by make

---

###Completed features:###

* Input a fasta file with any name and convert it into a phylip file suitable for use in PAML

* Run Branch-Sites Test 1 & 2

###Features to be added:###

* Write results into csv or tsv (or .xlsx)
* Analyze results using R
* Create a table with results
