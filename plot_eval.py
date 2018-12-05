# author    : Eugen Saraci
# date      : 05/12/2018
# comments  : i dont know what the DRY principle is

import itertools
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

files = ["bm25_full.txt", "tf_idf_full.txt", "bm25_nostop.txt", "tf_idf_none.txt"]

# topic 'all' contains 94 metrics --> map = map
# every other topic t in [351, 400] cotains 91 metrics --> map = AP

# cheatsheet for trec_eval metrics
# num_ret     = [int(x[2]) for x in evals if x[1] == topic and x[0] == "num_ret"][0]
# num_rel     = [int(x[2]) for x in evals if x[1] == topic and x[0] == "num_rel"][0]
# num_rel_ret = [int(x[2]) for x in evals if x[1] == topic and x[0] == "num_rel_ret"][0]
# mean_ap     = [float(x[2]) for x in evals if x[1] == topic and x[0] == "map"][0]
# rprec       = [float(x[2]) for x in evals if x[1] == topic and x[0] == "Rprec"][0]
# prec_10     = [float(x[2]) for x in evals if x[1] == topic and x[0] == "P_10"][0]
# precisions  = [float(x[2]) for x in evals if x[1] == topic and x[0][:2] == "P_"]
# recalls     = [float(x[2]) for x in evals if x[1] == topic and x[0][:7] == "recall_"]
# iprecs      = [float(x[2]) for x in evals if x[1] == topic and x[0][:6] == "iprec_"]
# irecs       = np.linspace(0, 1.01, 11)
# cutoffs     = [5, 10, 15, 20, 30, 100, 200, 500, 1000]

markers         = itertools.cycle(("v", "^", "s", "o"))
legend_label    = itertools.cycle(("BM25 - PorterStemmer + Stopwords",
                                    "TF_IDF - PorterStemmer + Stopwords",
                                    "BM25 - PorterStemmer, NO Stopwords",
                                    "TF_IDF - NO PorterStemmer, NO Stopwords"))


########################################
# INTERPOLATED PR CURVE for TOPIC = ALL
########################################
topic = "all"
plt.xticks(np.linspace(0, 1, 11))
plt.yticks(np.linspace(0, 1, 11))
plt.xlim(-0.05, 1.05)
plt.ylim(-0.05, 1.05)
plt.xlabel("Recall")
plt.ylabel("Precision")
plt.title("Interpolated Precision-Recall Curve - Topic: {}".format(topic))

for fname in files:
    evals   = np.loadtxt("./terrier/var/evaluation/{}".format(fname), skiprows=2, dtype=str)
    iprecs  = [float(x[2]) for x in evals if x[1] == topic and x[0][:6] == "iprec_"]
    irecs   = np.linspace(0, 1.01, 11)
    plt.plot(irecs, iprecs, marker=next(markers), label=next(legend_label))

plt.axvline(0.2, ls="--", c="black", lw=0.2)
plt.axvline(0.8, ls="--", c="black", lw=0.2)
plt.legend()
plt.show()
# plt.savefig("./figures/iprc.png")
plt.clf()


#############################
# PR CURVE for TOPIC = ALL
#############################
topic = "all"
plt.xlim(0, 0.6)
plt.ylim(0, 0.6)
plt.xlabel("Recall")
plt.ylabel("Precision")
plt.title("Precision-Recall Curve - Topic: '{}'".format(topic))

for fname in files:
    evals       = np.loadtxt("./terrier/var/evaluation/{}".format(fname), skiprows=2, dtype=str)
    precisions  = [float(x[2]) for x in evals if x[1] == topic and x[0][:2] == "P_"]
    recalls     = [float(x[2]) for x in evals if x[1] == topic and x[0][:7] == "recall_"]
    plt.plot(recalls, precisions, marker=next(markers), label=next(legend_label))

plt.legend()
# plt.savefig("./figures/prc.png")
plt.show()
plt.clf()


#############################
# METRICS REQUIRED BY HW1
#############################

aps         = []
rprecs      = []
precs_10    = []

for fname in files:
    evals       = np.loadtxt("./terrier/var/evaluation/{}".format(fname), skiprows=2, dtype=str)
    aps.append([float(x[2]) for x in evals if x[1] == topic and x[0] == "map"][0])
    rprecs.append([float(x[2]) for x in evals if x[1] == topic and x[0] == "Rprec"][0])
    precs_10.append([float(x[2]) for x in evals if x[1] == topic and x[0] == "P_10"][0])


print(tabulate(list(zip(legend_label, aps, rprecs, precs_10)), ["Modello", "MAP", "RPrec", "P@10"], tablefmt="latex"))
"""
evals = np.loadtxt("./terrier/var/evaluation/{}".format(files[0]), skiprows=2, dtype=str)

aps = []
for topic in range(351, 401):
    aps.append([float(x[2]) for x in evals if x[1] == str(topic) and x[0] == "map"][0])

print(aps)
plt.figure()
plt.bar(np.arange(351, 401), aps)
plt.show()
"""
