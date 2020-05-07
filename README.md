# sandbox

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

---

https://github.com/sassbalint/double-cube-jump-and-stay/commit/f3ca1ec
https://github.com/sassbalint/double-cube-jump-and-stay/commit/f3ca1ec648c3635fdfb17a42be0c7ceebc867f42
[link commitra](https://github.com/sassbalint/double-cube-jump-and-stay/commit/f3ca1ec)
[link commitra](https://github.com/sassbalint/double-cube-jump-and-stay/commit/f3ca1ec648c3635fdfb17a42be0c7ceebc867f42)

`span` color not allowed:
<span style="color: orange">sdlkfdslkfdsklf</span>

`div` color not allowed:
<div style="color: orange">sdlkfdslkfdsklf</div>

[link to Work in progress](#work-in-progress)

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

# Work in progress

:)

