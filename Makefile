all: branchsites2 branchsites1

test: results.csv

branchsites2: alternative null

branchsites1: alternative m1

branch: m0 nratios

alternative: $(patsubst %.fasta, lnL_alternative_%, $(wildcard *.fasta))

null: $(patsubst %.fasta, lnL_null_%, $(wildcard *.fasta))

m1: $(patsubst %.fasta, lnL_m1_%, $(wildcard *.fasta))

m0: $(patsubst %.fasta, lnL_m0_%, $(wildcard *.fasta))

nratios: $(patsubst %.fasta, lnL_nratios_%, $(wildcard *.fasta))

clean:
	rm -drf paml

%.phy: %.fasta
	python ./scripts/01_converter.py $< $@
	mkdir -p paml
	mkdir -p paml/$*
	mv $@ paml/$*

lnL_alternative_%: %.phy
	mkdir paml/$*/alternative
	python ./scripts/02a_alternative.py $< *.tre

lnL_null_%: %.phy
	mkdir paml/$*/null
	python ./scripts/02b_null.py $< *.tre

lnL_m1_%: %.phy
	mkdir paml/$*/m1
	python ./scripts/02c_m1.py $< *.tre

lnL_m0_%: %.phy
	mkdir paml/$*/m0
	python ./scripts/02d_m0.py $< *.tre

lnL_nratios_%: %.phy
	mkdir paml/$*/nratios
	python ./scripts/02e_nratios.py $< *.tre

results.csv: *.csv
	find ./paml/ -type f -wholename $< -exec cat {} \; > ./paml/$@

.PHONY: all branchsites2 branchsites1 alternative null m1 clean *.csv
.DELETE_ON_ERROR:
.SECONDARY:
