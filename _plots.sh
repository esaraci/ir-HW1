# author: Eugen Saraci
# date  : 11/12/18


# checking if it's being executed from the correct dir
if [ ! -f plot_eval.py ]; then
    echo "[-] plot_eval.py not found!"
    echo "[-] Please be sure to execute this script just outside of the terrier directory."
    exit 1
fi


echo "[+] -- PLOTTING TABLES AND IMAGES --"

# creating/deleting figures folder
if [ -d figures ]
then
	rm -r figures
fi
mkdir figures

# calling script to print tables and graphs
python -W ignore plot_eval.py

echo "[+] -- PLOT IS OVER --"
