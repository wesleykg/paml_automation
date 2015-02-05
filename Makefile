all: alternative null

alternative: $(patsubst %.fasta, lnL_alternative_%, $(wildcard *.fasta))

null: $(patsubst %.fasta, lnL_null_%, $(wildcard *.fasta))

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

.PHONY: all alternative null clean
.DELETE_ON_ERROR:
.SECONDARY:
