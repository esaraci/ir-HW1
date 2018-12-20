# Information Retrieval - Homework 1

### Usage

1. Clone the repository and rename Terrier:
```
$ git clone https://github.com/esaraci/ir-HW1.git && cd ir-HW1
$ tar -xzvf terrier-core-4.4-bin.tar.gz
$ mv terrier-core-4.4 terrier
```
2. put the `TIPSTER` folder (qrels and topics too) in the `data` directory; make sure that the `data` directory has now the following structure:

```
data
├── qrels.trec7.txt
├── TIPSTER
│   ├── TREC_VOL4
│   └── TREC_VOL5
└── topics.351-400_trec7.txt
```

3. execute `main.sh` after giving it exec permission
```
$ chmod +x main.sh && ./main.sh
```
___

Some tables will be printed to `stdout` while the output files of the whole process can be found in the follwing folders:

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
├── iprc.png              # interpolated precision-recall curve (for topic=all) at different recall levels
├── prc.png               # precision recall curve (for topic=all), cutoffs at [5,10,15,20,30,50,100,200,500,1000]
├── tukey_maps.png        # tukey's HSD test on MAPs (APs) on all systems
├── tukey_precs_10.png    # tukey's HSD test on P@10s on all systems
└── tukey_rprecs.png      # tukey's HSD test on RPrecs on all systems
```
___
- Main documentation [you are here]
- Scripts documentation [HERE](docs/SCRIPTS.md)
- Figures documentation [HERE](docs/FIGURES.md)
- Tables documentation [HERE](docs/TABLES.md)
- `terrier.properties` [HERE](terrier.properties)
