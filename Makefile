
all:
	 @echo "choose explicit target = type 'make ' and press TAB"

# !!! git diff-et nem zavarja, hogy másképp vannak a sortörések! (ugye a sota az spl)
diff:
	@echo
	@echo 'diff "raw / no space at the end of lines" 8465ae2 vs "sota / glued punctuation 2" 0d6ee3f'
	@echo
	@sleep 2
	git diff --word-diff -U10000 8465ae2 0d6ee3f

FILE=OsirisKonyvek_M156.txt

# XXX works on "raw / no space at the end of lines" 8465ae2 as input
to_trivial_spl:
	cat $(FILE) | python3 to_trivial_spl.py > $(FILE).trivial_spl

# XXX works on "sota" 0bfca68 as input
# |nem| |volt| ,| |csak| |ült|
# =>
# nem volt, csak ült
# azaz:
# '| |' = ' '
# '| '  = ''
# ' |'  = ''
# plusz még a sorok elejéről/végéről is lekerül a '|'
glue_punctuation:
	cat $(FILE) | python3 glue_punctuation.py | sed "s/| |/ /g;s/| //g;s/ |//g;s/^|//;s/|$$//" > $(FILE).glued_punct

