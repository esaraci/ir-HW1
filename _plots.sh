# author: Eugen Saraci
# date  : 11/12/18


if [ ! -f terrier/bin/trec_eval.sh ]; then
    echo "[-] terrier/bin/trec_eval.sh not found!"
    echo "[-] Please be sure to execute this script just outside of the terrier directory."
    exit 1
fi


echo "[+] -- PLOTTING IMAGES --"

if [ -d figures ]
then
	rm -r figures
fi
mkdir figures

python plot_eval.py

echo "[+] -- EVALUATION IS OVER --"
