##### Template per `etc/terrier.properties`

```
#default controls for query expansion
querying.postprocesses.order=QueryExpansion
querying.postprocesses.controls=qe:QueryExpansion
#default controls for the web-based interface. SimpleDecorate
#is the simplest metadata decorator. For more control, see Decorate.
querying.postfilters.order=SimpleDecorate,SiteFilter,Scope
querying.postfilters.controls=decorate:SimpleDecorate,site:SiteFilter,scope:Scope

#default and allowed controls
querying.default.controls=
querying.allowed.controls=scope,qe,qemodel,start,end,site,scope

#document tags specification
#for processing the contents of
#the documents, ignoring DOCHDR
TrecDocTags.doctag=DOC
TrecDocTags.idtag=DOCNO
TrecDocTags.skip=DOCHDR
#set to true if the tags can be of various case
TrecDocTags.casesensitive=false

#query tags specification
TrecQueryTags.doctag=top
TrecQueryTags.idtag=num
TrecQueryTags.process=top,num,title
TrecQueryTags.skip=desc,narr

#stop-words file
stopwords.filename=stopword-list.txt

#the processing stages a term goes through
#termpipelines=Stopwords,PorterStemmer
termpipelines=

#retrieval model
trec.topics=data/topics.351-400_trec7.txt
trec.qrels=data/qrels.trec7.txt

# self explaing, default is true, changes between different versions
ignore.low.idf.terms=true

```





#### Esecuzione script


```bash
# spostarsi sulla home directory di terrier
# creare la cartella ./data
# copiare la cartella TIPSTER e i file qrels.trec7.txt, topics.351-400_trec7 dentro la cartella ./terrier/data

######### [STEP 0: PREPROCESSING] ##########

# eseguire sanitize_z_format.py
python3 sanitize_z_format.py

# decompressione dei dati
uncompress data/TIPSTER/**/**/*

# creare le cartelle necessarie al task
mkdir var/indexes
mkdir var/results
mkdir var/evaluation

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
-Dterrier.results=results \
-Dtrec.results.file=bm25_full.res \
-Dtrec.model=BM25 \
-Dtermpipelines=Stopwords,PorterStemmer

sh bin/trec_terrier.sh -r \
-Dterrier.index.path=indexes/full \
-Dterrier.results=results \
-Dtrec.results.file=tf_idf_full.res \
-Dtrec.model=TF_IDF \
-Dtermpipelines=Stopwords,PorterStemmer

sh bin/trec_terrier.sh -r \
-Dterrier.index.path=indexes/nostop \
-Dterrier.results=results \
-Dtrec.results.file=bm25_nostop.res \
-Dtrec.model=BM25 \
-Dtermpipelines=PorterStemmer

sh bin/trec_terrier.sh -r \
-Dterrier.index.path=indexes/none \	
-Dterrier.results=results \
-Dtrec.results.file=tf_idf_none.res \
-Dtrec.model=TF_IDF \
-Dtermpipelines=

######### [STEP 4: EVALUATION] ##########
sh bin/trec_eval.sh -q -m all_trec \
data/qrels.trec7.txt \
var/results/bm25_full.res > var/evaluation/bm25_full.txt

sh bin/trec_eval.sh -q -m all_trec \
data/qrels.trec7.txt \
var/results/tf_idf_full.res > var/evaluation/tf_idf_full.txt

sh bin/trec_eval.sh -q -m all_trec \
data/qrels.trec7.txt \
var/results/bm25_nostop.res > var/evaluation/nostop.txt

sh bin/trec_eval.sh -q -m all_trec \
data/qrels.trec7.txt \
var/results/tf_idf_none.res > var/evaluation/tf_idf_none.txt

######### [STEP 4: ANALYSIS] ##########
```
