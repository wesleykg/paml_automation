all: $(patsubst %.fasta, %_paml.phy, $(wildcard *.fasta))

clean:
	rm -f $(patsubst %.fasta, %_paml.phy, $(wildcard *.fasta))

%_paml.phy: %.fasta
	python ./scripts/01_fasta_to_phylip $< $@


.PHONY: all clean
.DELETE_ON_ERROR:
.SECONDARY:
