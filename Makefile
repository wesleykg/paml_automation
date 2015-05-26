all: branchsites2 branchsites1 results.csv

branchsites2: alternative null results.csv

branchsites1: alternative m1 results.csv

branch: m0 nratios results.csv

alternative: $(patsubst %.fasta, lnL_alternative_%.csv, $(wildcard *.fasta))

null: $(patsubst %.fasta, lnL_null_%.csv, $(wildcard *.fasta))

m1: $(patsubst %.fasta, lnL_m1_%.csv, $(wildcard *.fasta))

m0: $(patsubst %.fasta, lnL_m0_%.csv, $(wildcard *.fasta))

nratios: $(patsubst %.fasta, lnL_nratios_%.csv, $(wildcard *.fasta))

clean:
	rm -drf paml

VPATH = ./sequences

%.phy: %.fasta
	python ./scripts/01_converter.py $< $@
	mkdir -p paml/$*
	mv $@ paml/$*

lnL_alternative_%.csv: %.phy
	mkdir paml/$*/alternative
	python ./scripts/02a_alternative.py $< *.tre

lnL_null_%.csv: %.phy
	mkdir paml/$*/null
	python ./scripts/02b_null.py $< *.tre

lnL_m1_%.csv: %.phy
	mkdir paml/$*/m1
	python ./scripts/02c_m1.py $< *.tre

lnL_m0_%.csv: %.phy
	mkdir paml/$*/m0
	python ./scripts/02d_m0.py $< *.tre

lnL_nratios_%.csv: %.phy
	mkdir paml/$*/nratios
	python ./scripts/02e_nratios.py $< *.tre

lnL_results = $(wildcard lnL_*.csv)

results.csv: $(lnL_results)
	find ./paml/ -type f -wholename *.csv -exec cat {} \; > ./paml/$@

.PHONY: all branchsites2 branchsites1 alternative null m1 clean
.DELETE_ON_ERROR:
.SECONDARY:
