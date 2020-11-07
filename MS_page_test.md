# M$ leírás

# Data Preparation for BERT Pretraining
The following steps are to prepare Wikipedia corpus for pretraining. However, these steps can be used with little or no modification to preprocess other datasets as well:

1. Download wiki dump file from https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2.
   This is a zip file and needs to be unzipped.
2. Clone [Wikiextractor](https://github.com/attardi/wikiextractor), and run:
   ```
   git clone https://github.com/attardi/wikiextractor
   python3 wikiextractor/WikiExtractor.py -o out -b 1000M enwiki-latest-pages-articles.xml
   ```  
   Running time can be 5-10 minutes/GB.  
   _output:_ `out` directory
3. Run:
   ```
   ln -s out out2`
   python3 AzureML-BERT/pretrain/PyTorch/dataprep/single_line_doc_file_creation.py
   ```
   This script removes html tags and empty lines and outputs to one file where each line is a paragraph.
   (`pip install tqdm` if needed.)
    _output:_ `wikipedia.txt`
4. Run:
   ```
   python3 AzureML-BERT/pretrain/PyTorch/dataprep/sentence_segmentation.py wikipedia.txt wikipedia.segmented.nltk.txt
   ```
   This script converts `wikipedia.txt` to one file where each line is a sentence.
   (`pip install nltk` if needed.)
    _output:_ `wikipedia.segmented.nltk.txt`
5. Split the above output file into ~100 files by line with:
   ```
   mkdir data_shards
   python3 AzureML-BERT/pretrain/PyTorch/dataprep/split_data_into_files.py
   ```
   _output:_ `data_shards` directory
6. Run:
   ```python3 AzureML-BERT/pretrain/PyTorch/dataprep/create_pretraining.py --input_dir=data_shards --output_dir=pickled_pretrain_data --do_lower_case=true
   ```
   This script will convert each file into pickled `.bin` file.
   _output:_ `pickled_pretrain_data` directory

# kód megy felsorolásba? MEGY! :)

1. sdfsf
   asdfsdfsdf
2. sdfsdfsdf
gfdfgdfgf
3. erwerr
```
code
```
4. asdf sdf
   ```
   code
   ```
   

# outputs

Az _outputs_ mappa tartalmazza a projektben használt scriptek _kisebb méretű_ kimeneteit (a segédanyag-jellegűeket, pl. különféle listákat). Ezek a következők:

### MAIN STUFF

- #6 __splt_errs.txt__: Példák az elválasztási hibákra. A sorok formátuma: `{eredeti}>>{javított}`.
- #10 __ocr*/ocr_some_errors.out__: A `make ocr` kimenete, a vélt OCR hibák gyűjteménye, tanulmányozás céljára.
Formátuma:
  - [1.] oszlop: mindig "1", figyelmen kívül hagyandó;
  - [2.] oszlop: a szó
  - [3.] oszlop: `@3,10,11` = a 3-as, 10-es és 11-es bigramnál vél hibát az `ocr.py`.\
Azaz:
`1 MAqyARORSzÁqi @3,10,11` esetén a `qy` és  `zÁ` és `Áq` bigramoknál.\
(A szavak eleje/vége a bigramok miatt jelölve van, így:  `→MAqyARORSzÁqi←`.
A bigramok számozása 0-tól kezdődik, szóval a 0-ás a `→M`, így jön ki, hogy a 3-as a `qy` lesz.)
- #10 __ocr*/ocr_categories.out__: A `make ocr` kimenete, a feldolgozási fajták összesített száma (by type).
- #10 __ocr*/ocr_token_categories.out__: A `make ocr` kimenete, a feldolgozási fajták összesített száma (by token).

__ocr*__ könyvtárak:
* `ocr_ACTUAL` -> `ocr_tok` mindig a legfrissebre mutat (mutasson...)
* `ocr_tok` tokenizálással (tok+OOV+OCR)
* `ocr_no_tok` tokenizálás nélkül (OOV+OCR) 
* `ocr_small` régi futtatás a régi kicsi mintán

`make ocr` a kimenetét ide az `outputs` könyvtárba teszi :arrow_right:
ez diffelhető a kívánt korábbi `ocr*` könyvtár tartalmával.

(Sorrend #17 szerint.)

_Figyelem!_ A nagy (500 MB+) listák az _arcanum\_trg_ szubmodulban találhatók, ezen belül az _outputs\_bigstore_ mappában. Ld. az ottani README-t a részletekért.

