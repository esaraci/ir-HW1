# author: Eugen Saraci
# date  : 03/12/18


if [ ! -d terrier ]; then
    echo "[-] terrier directory not found!"
    echo "[-] Please be sure to execute this script just outside of the terrier directory."
    exit 1
fi

if [ ! -d data/TIPSTER ]; then
    echo "[-] data/TIPSTER not found!"
    echo "[-] Please put the TIPSTER directory inside the data/ directory"
    exit 1
fi

if [ ! -f data/qrels.trec7.txt ]; then
    echo "[-] data/qrels.trec7.txt not found!"
    echo "[-] Please put qrels.trec7.txt inside the data/ directory"
    exit 1
fi

if [ ! -f data/topics.351-400_trec7.txt ]; then
    echo "[-] data/topics.351-400_trec7.txt not found!"
    echo "[-] Please put topics.351-400_trec7.txt inside the data/ directory"
    exit 1
fi


# echo "[+] Renaming .1Z .2Z .3Z files to .Z"
find data/TIPSTER -name "*.0Z" -exec rename .0Z _0.Z {} ';'
find data/TIPSTER -name "*.1Z" -exec rename .1Z _1.Z {} ';'
find data/TIPSTER -name "*.2Z" -exec rename .2Z _2.Z {} ';'

# echo "[+] Uncomrpessing .Z files"
find data/TIPSTER -name "*.Z" -exec uncompress {} ';'

# echo "[+] Moving terrier.properties"
mv terrier/etc/terrier.properties terrier/etc/terrier.properties.bak
mv terrier.properties terrier/etc/terrier.properties

echo "[+] -- PREPROCESSING IS OVER --"