all: $(patsubst %.fasta, %.phy, $(wildcard *.fasta))

clean:
	rm -drf paml

%.phy: %.fasta
	python ./scripts/01_converter.py $< $@
	mkdir -p paml
	mkdir paml/$(*F)
	mv $@ paml/$(*F)


.PHONY: all clean
.DELETE_ON_ERROR:
.SECONDARY:
