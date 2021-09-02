# UniprotScraper

UniprotScraper is a web scraping tool that specialized for Uniprot Database. It requires only
the uniprot entry number of relevant protein. The included methods can return the fasta file,
only the header, only the sequence, first three, five and ten amino acids of protein.

## Installation

with pip:

```bash
pip install UniprotScraper
```

for latest version:

```bash
pip install UniprotScraper --upgrade
```

## Usage

Get FASTA file of protein that entered Uniprot Entry Number,

Input:
```python
import bs4
import urllib.request
from urllib.error import HTTPError, URLError
import UniprotScraper as us

fasta = us.get_with_header("P04418")
print(fasta)
```

Output:
```python
>sp|P04418|END5_BPT4 Endonuclease V OS=Enterobacteria phage T4 OX=10665 PE=1 SV=1
MTRINLTLVSELADQHLMAEYRELPRVFGAVRKHVANGKRVRDFKISPTFILGAGHVTFF
YDKLEFLRKRQIELIAECLKRGFNIKDTTVQDISDIPQEFRGDYIPHEASIAISQARLDE
KIAQRPTWYKYYGKAIYA
```
Get only the protein sequence,

Input:
```python
sequence = us.get_without_header("P04418")
print(sequence)
```

Output:
```python
MTRINLTLVSELADQHLMAEYRELPRVFGAVRKHVANGKRVRDFKISPTFILGAGHVTFF
YDKLEFLRKRQIELIAECLKRGFNIKDTTVQDISDIPQEFRGDYIPHEASIAISQARLDE
KIAQRPTWYKYYGKAIYA
```

Get only the header of FASTA file,

Input:
```python
header = us.get_only_header("P04418")
print(header)
```

Output:
```python
>sp|P04418|END5_BPT4 Endonuclease V OS=Enterobacteria phage T4 OX=10665 PE=1 SV=1
```

Get first three amino acids,

Input:
```python
three_aa = us.get_first_three_aa("P04418")
print(three_aa)
```

Output:
```python
MTR
```

Get first five amino acids,

Input:
```python
five_aa = us.get_first_five_aa("P04418")
print(five_aa)
```

Output:
```python
MTRIN
```

Get first ten amino acids,

Input:
```python
ten_aa = us.get_first_ten_aa("P04418")
print(ten_aa)
```

Output:
```python
MTRINLTLVS
```

Get amino acid composition,

Input:
```python
content_aa = us.get_aa_content("P04418")
print(content_aa)
```

Output:
```python
{'M': 2, 'T': 7, 'R': 12, 'I': 13, 'N': 3, 'L': 11, 'V': 7, 'S': 5, 'E': 9, 'A': 12, 'D': 8, 'Q': 6, 'H': 4, 'Y': 7, 'P': 5, 'F': 8, 'G': 7, 'K': 10, '\n': 2, 'C': 1, 'W': 1}
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
