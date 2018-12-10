# ir-HW1

## Usage

Clone the repository
```
$ git clone https://github.com/esaraci/ir-HW1.git && cd ir-HW1
```

extract Terrier and rename it
```
$ tar -xzvf terrier-core-4.4-bin.tar.gz
$ mv terrier-core-4.4 terrier
```

make sure that the `data` folder has the following structure. The `TIPSTER` directory is not included in this repository and must be downloaded from somewhere else.

```
data/
  ├── qrels.trec7.txt
  ├── TIPSTER
  │   ├── TREC_VOL4
  │   └── TREC_VOL5
  └── topics.351-400_trec7.txt

```

execute `main.sh`
```
$ chmod +x main.sh && ./main.sh
```

the outputs of the whole process can be found in

```
terrier/var
├── evaluation
│   ├── bm25_full.txt
│   ├── bm25_nostop.txt
│   ├── tf_idf_full.txt
│   └── tf_idf_none.txt
├── indexes
│   ├── full
│   ├── none
│   └── nostop
└── results
    ├── bm25_full.res
    ├── bm25_nostop.res
    ├── tf_idf_full.res
    └── tf_idf_none.res 

figures
├── distr_maps.png
├── distr_precs_10.png
├── distr_rprecs.png
├── iprc.png
├── prc.png
├── tukey_maps.png
├── tukey_precs_10.png
└── tukey_rprecs.png

```

`main.sh` will sequentially execute

1. `_preprocessing.sh`
1. `_indexing.sh`
1. `_retrieval.sh`
1. `_evaluation.sh`
