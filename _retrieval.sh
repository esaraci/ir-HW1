# author: Eugen Saraci
# date  : 03/12/18


if [ ! -f terrier/bin/trec_terrier.sh ]; then
    echo "[-] terrier/bin/trec_terrier.sh not found!"
    echo "[-] Please be sure to execute this script just outside of the terrier directory."
    exit 1
fi

echo "[+] -- RETRIEVAL IS STARTING --"

sh terrier/bin/trec_terrier.sh -r \
-Dterrier.index.path=indexes/full \
-Dterrier.results=results \
-Dtrec.results.file=bm25_full.res \
-Dtrec.model=BM25 \
-Dtermpipelines=Stopwords,PorterStemmer

sh terrier/bin/trec_terrier.sh -r \
-Dterrier.index.path=indexes/full \
-Dterrier.results=results \
-Dtrec.results.file=tf_idf_full.res \
-Dtrec.model=TF_IDF \
-Dtermpipelines=Stopwords,PorterStemmer

sh terrier/bin/trec_terrier.sh -r \
-Dterrier.index.path=indexes/nostop \
-Dterrier.results=results \
-Dtrec.results.file=bm25_nostop.res \
-Dtrec.model=BM25 \
-Dtermpipelines=PorterStemmer

sh terrier/bin/trec_terrier.sh -r \
-Dterrier.index.path=indexes/none \
-Dterrier.results=results \
-Dtrec.results.file=tf_idf_none.res \
-Dtrec.model=TF_IDF \
-Dtermpipelines=

echo "[+] -- INDEXING IS OVER --"
