# author: Eugen Saraci
# date  : 03/12/18


# checking if it's being executed from the correct dir
if [ ! -f terrier/bin/trec_eval.sh ]; then
    echo "[-] terrier/bin/trec_eval.sh not found!"
    echo "[-] Please be sure to execute this script just outside of the terrier directory."
    exit 1
fi

# creating/deleting folders for evaluation
if [ -d terrier/var/evaluation ]
then
	rm -r terrier/var/evaluation
fi
mkdir terrier/var/evaluation

echo "[+] -- EVALUATION IS STARTING --"

# command params
# 
# trec_eval has 2 positional arguments: .qrels path and .res path
# -m specificies which measures to compute
# stdout is redirected to > terrier/var/evaluation/*system_name*.txt
# 

sh terrier/bin/trec_eval.sh -q -m all_trec \
data/qrels.trec7.txt \
terrier/var/results/bm25_full.res > terrier/var/evaluation/bm25_full.txt

sh terrier/bin/trec_eval.sh -q -m all_trec \
data/qrels.trec7.txt \
terrier/var/results/tf_idf_full.res > terrier/var/evaluation/tf_idf_full.txt

sh terrier/bin/trec_eval.sh -q -m all_trec \
data/qrels.trec7.txt \
terrier/var/results/bm25_nostop.res > terrier/var/evaluation/bm25_nostop.txt

sh terrier/bin/trec_eval.sh -q -m all_trec \
data/qrels.trec7.txt \
terrier/var/results/tf_idf_none.res > terrier/var/evaluation/tf_idf_none.txt

echo "[+] -- EVALUATION IS OVER --"
