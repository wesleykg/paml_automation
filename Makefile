all: $(patsubst %.fasta, $(method)_%.csv, $(wildcard *.fasta)) results.csv

clean:
	rm -drf results

%.phy: %.fasta
	python ./scripts/01_converter.py $< $@
	mkdir -p results/$*
	mv $@ results/$*

$(method)_%.csv: %.phy
ifeq ($(method),branchsites2)
	mkdir results/$*/alternative
	python ./scripts/02_codeml.py $< *.tre alternative
	mkdir results/$*/null
	python ./scripts/02_codeml.py $< *.tre null
else
ifeq ($(method),branchsites1)
	mkdir -p results/$*/alternative
	python ./scripts/02_codeml.py $< *.tre alternative
	mkdir -p results/$*/m1
	python ./scripts/02_codeml.py $< *.tre m1
else
ifeq ($(method),both)
	mkdir -p results/$*/alternative
	python ./scripts/02_codeml.py $< *.tre alternative
	mkdir -p results/$*/null
	python ./scripts/02_codeml.py $< *.tre null
	mkdir -p results/$*/m1
	python ./scripts/02_codeml.py $< *.tre m1
else
ifeq ($(method),branch)
	mkdir -p results/$*/m0
	python ./scripts/02_codeml.py $< *.tre m0
	mkdir -p results/$*/nratios
	python ./scripts/02_codeml.py $< *.tre nratios
else
	mkdir -p results/$*/$(method)
	python ./scripts/02_codeml.py $< *.tre $(method)
endif
endif
endif
endif

results = $(wildcard $(method)_*.csv)

results.csv: $(results)
	find ./results -mindepth 2 -wholename *.csv -exec cat {} \; > ./results/$@

.PHONY: all clean
.DELETE_ON_ERROR:
.SECONDARY:
