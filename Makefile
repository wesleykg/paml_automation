all: $(patsubst %.fasta, $(method)_%.csv, $(wildcard *.fasta))

clean:
	rm -drf results

%.phy: %.fasta
	python ./scripts/01_converter.py $<
	mkdir -p results/$*
	mv $@ results/$*

$(method)_%.csv: %.phy
ifeq ($(method),branchsites)
	mkdir results/$*/bsA_alternative
	python ./scripts/02_codeml.py --clean_data=0 --fix_blength=1 $< *.tre \
	bsA_alternative 
	mkdir results/$*/bsA_null
	python ./scripts/02_codeml.py --clean_data=0 --fix_blength=1 $< *.tre \
	bsA_null
else
ifeq ($(method),clademodelC)
	mkdir -p results/$*/m2a_rel
	python ./scripts/02_codeml.py --clean_data=0 --fix_blength=1 $< *.tre \
	m2a_rel
	mkdir -p results/$*/CmC
	python ./scripts/02_codeml.py --clean_data=0 --fix_blength=1 $< *.tre \
	CmC
else
ifeq ($(method),clademodelD)
	mkdir -p results/$*/m3
	python ./scripts/02_codeml.py --clean_data=0 --fix_blength=1 $< *.tre \
	m3
	mkdir -p results/$*/CmD
	python ./scripts/02_codeml.py --clean_data=0 --fix_blength=1 $< *.tre \
	CmD
else
ifeq ($(method),clademodels)
	mkdir -p results/$*/m2a_rel
	python ./scripts/02_codeml.py --clean_data=0 --fix_blength=1 $< *.tre \
	m2a_rel
	mkdir -p results/$*/CmC
	python ./scripts/02_codeml.py --clean_data=0 --fix_blength=1 $< *.tre \
	CmC
	mkdir -p results/$*/m3
	python ./scripts/02_codeml.py --clean_data=0 --fix_blength=1 $< *.tre \
	m3
	mkdir -p results/$*/CmD
	python ./scripts/02_codeml.py --clean_data=0 --fix_blength=1 $< *.tre \
	CmD
else
ifeq ($(method),branch)
	mkdir -p results/$*/m0
	python ./scripts/02_codeml.py --clean_data=0 --fix_blength=1 $< *.tre m0
	mkdir -p results/$*/nratios
	python ./scripts/02_codeml.py --clean_data=0 --fix_blength=1 $< *.tre \
	nratios
else
ifeq ($(method),all)
	mkdir results/$*/bsA_alternative
	python ./scripts/02_codeml.py --clean_data=0 --fix_blength=1 $< *.tre \
	bsA_alternative 
	mkdir results/$*/bsA_null
	python ./scripts/02_codeml.py --clean_data=0 --fix_blength=1 $< *.tre \
	bsA_null
	mkdir -p results/$*/m0
	python ./scripts/02_codeml.py --clean_data=0 --fix_blength=1 $< *.tre m0
	mkdir -p results/$*/nratios
	python ./scripts/02_codeml.py --clean_data=0 --fix_blength=1 $< *.tre \
	nratios
	mkdir -p results/$*/m2a_rel
	python ./scripts/02_codeml.py --clean_data=0 --fix_blength=1 $< *.tre \
	m2a_rel
	mkdir -p results/$*/CmC
	python ./scripts/02_codeml.py --clean_data=0 --fix_blength=1 $< *.tre \
	CmC
	mkdir -p results/$*/m3
	python ./scripts/02_codeml.py --clean_data=0 --fix_blength=1 $< *.tre \
	m3
	mkdir -p results/$*/CmD
	python ./scripts/02_codeml.py --clean_data=0 --fix_blength=1 $< *.tre \
	CmD
else
	mkdir -p results/$*/$(method)
	python ./scripts/02_codeml.py --clean_data=0 --fix_blength=1 $< *.tre \
	$(method)
#endif
#endif
endif
endif
endif
endif
endif
endif

results = $(wildcard $(method)_*.csv)

results.csv: $(results)
	find ./results -mindepth 2 -wholename *.csv -exec cat {} \; > ./results/$@
	Rscript ./scripts/03_table.R ./results/$@

.PHONY: all clean
.DELETE_ON_ERROR:
.SECONDARY:
