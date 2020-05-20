
all: glue_punctuation

# XXX works on 0bfca68 as input
FILE=OsirisKonyvek_M156.txt
glue_punctuation:
	cat $(FILE) | python3 glue_punctuation.py | sed "s/| |/ /g;s/| //g;s/ |//g;s/^|//;s/|$$//" > $(FILE).glued_punct

