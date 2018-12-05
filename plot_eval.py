# author    : Eugen Saraci
# date      : 05/12/2018


import itertools
import numpy as np
import matplotlib.pyplot as plt

files = ["bm25_full.txt", "tf_idf_full.txt", "bm25_nostop.txt", "tf_idf_none.txt"]

# topic 'all' contains 94 metrics --> map = map
# every other topic t in [351, 400] cotains 91 metrics --> map = AP

# cheatsheet for trec_eval metrics
# num_ret     = [int(x[2]) for x in evals if x[1] == topic and x[0] == "num_ret"][0]
# num_rel     = [int(x[2]) for x in evals if x[1] == topic and x[0] == "num_rel"][0]
# num_rel_ret = [int(x[2]) for x in evals if x[1] == topic and x[0] == "num_rel_ret"][0]
# mean_ap     = [float(x[2]) for x in evals if x[1] == topic and x[0] == "map"][0]
# rprec       = [float(x[2]) for x in evals if x[1] == topic and x[0] == "Rprec"][0]
# precisions  = [float(x[2]) for x in evals if x[1] == topic and x[0][:2] == "P_"]
# recalls     = [float(x[2]) for x in evals if x[1] == topic and x[0][:7] == "recall_"]
# iprecs      = [float(x[2]) for x in evals if x[1] == topic and x[0][:6] == "iprec_"]
# irecs       = np.linspace(0, 1.01, 11)

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

# PRECISION RECALL CURVE
for fname in files:
    evals = np.loadtxt("./terrier/var/evaluation/{}".format(fname), skiprows=2, dtype=str)
    # num_ret     = [int(x[2]) for x in evals if x[1] == topic and x[0] == "num_ret"][0]
    # num_rel     = [int(x[2]) for x in evals if x[1] == topic and x[0] == "num_rel"][0]
    # num_rel_ret = [int(x[2]) for x in evals if x[1] == topic and x[0] == "num_rel_ret"][0]
    # mean_ap     = [float(x[2]) for x in evals if x[1] == topic and x[0] == "map"][0]
    # rprec       = [float(x[2]) for x in evals if x[1] == topic and x[0] == "Rprec"][0]
    # precisions  = [float(x[2]) for x in evals if x[1] == topic and x[0][:2] == "P_"]
    # recalls     = [float(x[2]) for x in evals if x[1] == topic and x[0][:7] == "recall_"]
    iprecs      = [float(x[2]) for x in evals if x[1] == topic and x[0][:6] == "iprec_"]
    irecs = np.linspace(0, 1.01, 11)

    plt.plot(irecs, iprecs, marker=next(markers), label=next(legend_label))

plt.axvline(0.2, ls='--', c="black", lw=0.2)
plt.axvline(0.8, ls='--', c="black", lw=0.2)
plt.legend()
plt.savefig("./figures/iprc.png")


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
    evals = np.loadtxt("./terrier/var/evaluation/{}".format(fname), skiprows=2, dtype=str)
    # num_ret     = [int(x[2]) for x in evals if x[1] == topic and x[0] == "num_ret"][0]
    # num_rel     = [int(x[2]) for x in evals if x[1] == topic and x[0] == "num_rel"][0]
    # num_rel_ret = [int(x[2]) for x in evals if x[1] == topic and x[0] == "num_rel_ret"][0]
    # mean_ap     = [float(x[2]) for x in evals if x[1] == topic and x[0] == "map"][0]
    # rprec       = [float(x[2]) for x in evals if x[1] == topic and x[0] == "Rprec"][0]
    precisions  = [float(x[2]) for x in evals if x[1] == topic and x[0][:2] == "P_"]
    recalls     = [float(x[2]) for x in evals if x[1] == topic and x[0][:7] == "recall_"]
    # iprecs      = [float(x[2]) for x in evals if x[1] == topic and x[0][:6] == "iprec_"]
    # irecs = np.linspace(0, 1.01, 11)

    plt.plot(recalls, precisions, marker=next(markers), label=next(legend_label))

plt.legend()
plt.savefig("./figures/prc.png")



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

"""
plt.figure()
plt.subplot(1,2,1)
plt.grid()
plt.yticks(np.arange(1,13))
plt.xticks(np.arange(1,6), ["M1\n(max_depth=1)", "M2\n(max_depth=2)", "M3\n(max_depth=5)", "M4\n(max_depth=10)", "M5\n(max_depth=None)"], fontsize=8)
plt.plot(np.arange(1,6), n_features, 'r--', label="feature utilizzate")
plt.plot(np.arange(1,6), depths, label="depth effettiva")
plt.legend()

plt.subplot(1,2,2)
plt.grid()
plt.xticks(np.arange(1,6), ["M1\n(max_depth=1)", "M2\n(max_depth=2)", "M3\n(max_depth=5)", "M4\n(max_depth=10)", "M5\n(max_depth=None)"], fontsize=8)
plt.plot(np.arange(1,6), scores, label="R^2")
plt.ylabel("Score")
plt.legend()

plt.show()

"""
