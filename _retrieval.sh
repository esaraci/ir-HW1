# author: Eugen Saraci
# date  : 03/12/18


# checking if it's being executed from the correct dir
if [ ! -f terrier/bin/trec_terrier.sh ]; then
    echo "[-] terrier/bin/trec_terrier.sh not found!"
    echo "[-] Please be sure to execute this script from just outside of the terrier directory."
    exit 1
fi

# overwriting current properties
# i need to do this again in this step
cp terrier.properties data/etc/terrier.properties


echo "[+] -- RETRIEVAL IS STARTING --"

# command params
# 
# -Dterrier.index.path  --> index we are referring to               
# -Dterrier.results     --> where to save output files
# -Dtrec.results.file   --> name of the output file
# -Dtrec.model          --> retrieval model
# -Dtermpipelines       --> pipeline steps (stemmer, stopwords)
#


# performing retrieval for each system
sh terrier/bin/trec_terrier.sh -r \
-Dterrier.index.path=indexes/full \
-Dtrec.results.file=bm25_full.res \
-Dtrec.model=BM25 \
-Dtermpipelines=Stopwords,PorterStemmer

sh terrier/bin/trec_terrier.sh -r \
-Dterrier.index.path=indexes/full \
-Dtrec.results.file=tf_idf_full.res \
-Dtrec.model=TF_IDF \
-Dtermpipelines=Stopwords,PorterStemmer

sh terrier/bin/trec_terrier.sh -r \
-Dterrier.index.path=indexes/nostop \
-Dtrec.results.file=bm25_nostop.res \
-Dtrec.model=BM25 \
-Dtermpipelines=PorterStemmer

sh terrier/bin/trec_terrier.sh -r \
-Dterrier.index.path=indexes/none \
-Dtrec.results.file=tf_idf_none.res \
-Dtrec.model=TF_IDF \
-Dtermpipelines=

echo "[+] -- INDEXING IS OVER --"
