```bash
# spostarsi sulla home directory di terrier
# creare la cartella ./terrier/data
# copiare la cartella TIPSTER e i file qrels.trec7.txt, topics.351-400_trec7 dentro la cartella ./terrier/data

######### [STEP 0: PREPROCESSING] ##########

# eseguire sanitize_z_format.py
python3 sanitize_z_format.py ./data/TIPSTER

# creare le cartelle necessarie al task
mkdir var/indexes
mkdir var/results

# creare le sottocartelle per gli indici
mkdir var/indexes/full var/indexes/nostop var/indexes/none


######### [STEP 1: SETUP] ##########
sh bin/trec_setup.sh data/TIPSTER


######### [STEP 2: INDEXING] ##########

sh bin/trec_terrier.sh -i \
-Dterrier.index.path=indexes/full \
-Dtermpipelines=Stopwords,PorterStemmer

sh bin/trec_terrier.sh -i \
-Dterrier.index.path=indexes/nostop \
-Dtermpipelines=PorterStemmer

sh bin/trec_terrier.sh -i \
-Dterrier.index.path=indexes/none \
-Dtermpipelines=


######### [STEP 3: RETRIEVAL] ##########


sh bin/trec_terrier.sh -r \
-Dterrier.index.path=indexes/full \
-Dterrier.results=results/bm25_full \
-Dtrec.model=BM25 \
-Dtermpipelines=Stopwords,PorterStemmer

sh bin/trec_terrier.sh -r \
-Dterrier.index.path=indexes/full \
-Dterrier.results=results/tf_idf_full \
-Dtrec.model=TF_IDF \
-Dtermpipelines=Stopwords,PorterStemmer

sh bin/trec_terrier.sh -r \
-Dterrier.index.path=indexes/nostop \
-Dterrier.results=results/bm25_nostop \
-Dtrec.model=BM25 \
-Dtermpipelines=PorterStemmer

sh bin/trec_terrier.sh -r \
-Dterrier.index.path=indexes/none \
-Dterrier.results=results/tf_idf_none \
-Dtrec.model=TF_IDF \
-Dtermpipelines=

######### [STEP 3: EVALUATION] ##########

sh bin/trec_terrier.sh -r -Dterrier.index.path=none -Dtrec.model=TF_IDF -Dtrec.results=results

```

