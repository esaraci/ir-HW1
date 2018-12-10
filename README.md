# ir-HW1

## Usage

Clone the repository
```
$ git clone https://github.com/esaraci/ir-HW1.git
```

unzip Terrier and rename it
```
$ tar -xzvf terrier-core-4.4-bin.tar.gz
$ mv terrier-core-4.4 terrier
```

make sure that the `data` folder has the following structure, the `TIPSTER` directory is not included in this repository and must be downloaded.
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

`main.sh` will sequentially execute

1. `_preprocessing.sh`
1. `_indexing.sh`
1. `_retrieval.sh`
1. `_evaluation.sh`
