all: branchsites2 branchsites1

branchsites2: alternative null

branchsites1: alternative m1

alternative: $(patsubst %.fasta, lnL_alternative_%, $(wildcard *.fasta))

null: $(patsubst %.fasta, lnL_null_%, $(wildcard *.fasta))

m1: $(patsubst %.fasta, lnL_m1_%, $(wildcard *.fasta))

clean:
	rm -drf paml

%.phy: %.fasta
	python ./scripts/01_converter.py $< $@
	mkdir -p paml
	mkdir paml/$*
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

.PHONY: all branchsites2 branchsites1 alternative null m1 clean
.DELETE_ON_ERROR:
.SECONDARY:
