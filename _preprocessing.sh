# author: Eugen Saraci
# date  : 03/12/18


# checking if it's being executed from the correct dir
if [ ! -d terrier ]; then
    echo "[-] terrier directory not found!"
    echo "[-] Please be sure to execute this script just outside of the terrier directory."
    exit 1
fi

# checking if docs, qrels, and topics are present
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

echo "[+] -- PREPROCESSING IS STARTING --"

# the next 4 'find' commands might not work on some OS/shell config
# if so comment the find commands and uncomment the python command
# you can also let them both execute 
# either way will work as long as one of the two commands works

# echo "[+] Renaming .1Z .2Z .3Z files to .Z"
find data/TIPSTER -name "*.0Z" -exec rename \.0Z _0.Z {} ';'
find data/TIPSTER -name "*.1Z" -exec rename \.1Z _1.Z {} ';'
find data/TIPSTER -name "*.2Z" -exec rename \.2Z _2.Z {} ';'
find data/TIPSTER -name "*.Z" -exec uncompress {} ';'

# the following command will perform the same steps as the find commands above
# repeating it wont change anything except computation time
# this is needed because the find commands do not work on all OS/shell config
python sanitize_z_format.py

# overwriting current properties
mv terrier/etc/terrier.properties terrier/etc/terrier.properties.bak
cp terrier.properties terrier/etc/terrier.properties

# updating etc/collection.spec
sh terrier/bin/trec_setup.sh data/TIPSTER/

echo "[+] -- PREPROCESSING IS OVER --"
