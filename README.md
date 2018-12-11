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
data
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

the outputs of the whole process can be found in:

```
terrier/var
├── evaluation            # contains the results obtained by trec_eval by running the runs against qrels.trec7.txt 
│   ├── bm25_full.txt         # results using bm25 as the retrieval model and 'full' as index
│   ├── tf_idf_full.txt       # results using tf_idf as retrieval model and 'full' as index
│   ├── bm25_nostop.txt       # results using bm25 as the retrieval model and 'nostop' as index
│   └── tf_idf_none.txt       # results using tf_idf as the retrieval model and 'none' as index
├── indexes               # contains the indexes produced by terrier's indexing process
│   ├── full                  # index with PorterStemmer + Stopwords removal
│   ├── none                  # index with neither PorterStemmer nor Stopwords removal
│   └── nostop                # index with ONLY PorterStemmer, no Stopwords removal
└── results               # contains the run files produced by terrier's retrieval process, one for each system
    ├── bm25_full.res    
    ├── bm25_nostop.res
    ├── tf_idf_full.res
    └── tf_idf_none.res


figures
├── distr_maps.png        # boxplots of MAPs (APs) values across the 50 topics for the 4 systems
├── distr_precs_10.png    # boxplots of P@10s values across the 50 topics for the 4 systems
├── distr_rprecs.png      # boxplots of RPrecs values across the 50 topics for the 4 systems
├── iprc.png              # interpolated precision-recall curve (for topic=all) at different recall values
├── prc.png               # precision recall curve (for topic=all), cutoffs at [5,10,15,20,30,50,100,200,500,1000]
├── tukey_maps.png        # TODO:
├── tukey_precs_10.png    # TODO:
└── tukey_rprecs.png      # TODO:
```

## Documentation

`main.sh` will sequentially execute

1. `_preprocessing.sh`
1. `_indexing.sh`
1. `_retrieval.sh`
1. `_evaluation.sh`

### `_preprocessing.sh`
This script performs some basic sanity checks and creates the folders needed for the correct execution. It also renames `.1Z, .2Z, .3Z` files to `_{1,2,3}.Z` files and uncompresses them  using `uncompress`. If something goes wrong with these commands then `sanitize_z_format.py` is executed, this python script will rename and uncompress the files in the same way but will not trigger parsing errors (which may happen on some OS + Shell configuration).
