# author    : Eugen Saraci
# date      : 05/12/2018
# comments  : i dont know what the DRY principle is

import itertools
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
from tabulate import tabulate
from statsmodels.stats.multicomp import pairwise_tukeyhsd


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

markers         = itertools.cycle(("s", "^", "v", "o"))
legend_label    = itertools.cycle(("BM25 - PorterStemmer + Stopwords",
                                    "TF_IDF - PorterStemmer + Stopwords",
                                    "BM25 - PorterStemmer, NO Stopwords",
                                    "TF_IDF - NO PorterStemmer, NO Stopwords"))


##########################################
# INTERPOLATED PR CURVE
# TOPIC = ALL
# RECALL_CUTOFFS = [0.1 .. 1, step=0.1]
##########################################
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

# models should be compared in the 3 areas defined by these vertical lines
plt.axvline(0.2, ls="--", c="grey", lw=0.8)
plt.axvline(0.8, ls="--", c="grey", lw=0.8)
plt.legend()
# plt.show()
plt.savefig("./figures/iprc.png")
plt.clf()


#################################################
# PR CURVE
# TOPIC = ALL
# CUTOFFS = [5,10,15,20,30,50,100,200,500,1000]
#################################################

topic = "all"
# plt.xlim(0, 0.8)
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
#plt.show()
plt.savefig("./figures/prc.png")
plt.clf()


##################################################
# METRICS REQUIRED BY HW1
# TOPIC = ALL --> these are all means
# @aps      = Mean Average Precision
# @rprecs   = prec @ RecallBase
# @precs_10 = prec @ 10 (top-10 docs)
# they all contain 4 values, one for each system
##################################################

maps        = []
rprecs      = []
precs_10    = []

for fname in files:
    evals = np.loadtxt("./terrier/var/evaluation/{}".format(fname), skiprows=2, dtype=str)
    maps.append([float(x[2]) for x in evals if x[1] == topic and x[0] == "map"][0])
    rprecs.append([float(x[2]) for x in evals if x[1] == topic and x[0] == "Rprec"][0])
    precs_10.append([float(x[2]) for x in evals if x[1] == topic and x[0] == "P_10"][0])


# github markdown
print("### MAP, RPrec, P@10 across the different systems for `topic=all`")
print("\n" + tabulate(list(zip(legend_label, maps, rprecs, precs_10)), ["Model", "MAP", "RPrec", "P@10"], tablefmt="pipe") + "\n")


################################
# HYPOTHESIS TESTING
################################

maps        = []
rprecs      = []
precs_10    = []

for fname in files:
    evals = np.loadtxt("./terrier/var/evaluation/{}".format(fname), skiprows=2, dtype=str)
    maps.append([float(x[2]) for x in evals if x[1] != topic and x[0] == "map"])
    rprecs.append([float(x[2]) for x in evals if x[1] != topic and x[0] == "Rprec"])
    precs_10.append([float(x[2]) for x in evals if x[1] != topic and x[0] == "P_10"])

maps        = np.array(maps)
rprecs      = np.array(rprecs)
precs_10    = np.array(precs_10)


#####################################
# BOXPLOTS FOR MAP, RPREC AND PREC@10
#####################################

plt.boxplot([maps[0], maps[1], maps[2], maps[3]], vert=False, labels=["bm25_full", "tf_idf_full", "bm25_nostop", "tf_idf_none"])
plt.title("Distributions of MAPs")
plt.xlabel("MAP")
plt.tight_layout()
plt.savefig("./figures/distr_maps.png")
plt.clf()

plt.boxplot([rprecs[0], rprecs[1], rprecs[2], rprecs[3]], vert=False, labels=["bm25_full", "tf_idf_full", "bm25_nostop", "tf_idf_none"])
plt.title("Distributions of RPrecs")
plt.xlabel("RPrec")
plt.tight_layout()
plt.savefig("./figures/distr_rprecs.png")
plt.clf()

plt.boxplot([precs_10[0], precs_10[1], precs_10[2], precs_10[3]], vert=False, labels=["bm25_full", "tf_idf_full", "bm25_nostop", "tf_idf_none"])
plt.title("Distributions of P@10s")
plt.xlabel("P@10")
plt.tight_layout()
plt.savefig("./figures/distr_precs_10.png")
plt.clf()



######################################
# ANOVA 1-WAY
######################################

anova_maps      = stats.f_oneway(maps[0], maps[1], maps[2], maps[3])
anova_rprecs    = stats.f_oneway(rprecs[0], rprecs[1], rprecs[2], rprecs[3])
anova_precs_10  = stats.f_oneway(precs_10[0], precs_10[1], precs_10[2], precs_10[3])

# github markdown
print("### ANOVA-1-WAY results for MAP, RPREC, P@10\n")
print("| Measure |   F-stat   |   p-value  | ")
print("|:--------|-----------:|-----------:| ")
print("| MAP     | F: {0:.4f} | p: {1:.4f} |".format(anova_maps[0], anova_maps[1]))
print("| RPREC   | F: {0:.4f} | p: {1:.4f} |".format(anova_rprecs[0], anova_rprecs[1]))
print("| P@10    | F: {0:.4f} | p: {1:.4f} |".format(anova_precs_10[0], anova_precs_10[1]))
print()


######################################
# TUKEY HSD
######################################

# needed for `pairwise_tukeyhsd`
names = np.repeat("bm25_full", 50)
names = np.append(names, np.repeat("tf_idf_full", 50))
names = np.append(names, np.repeat("bm25_nostop", 50))
names = np.append(names, np.repeat("tf_idf_none", 50))

# reshaping for `pairwise_tukeyhsd`
maps.shape      = (200,)
rprecs.shape    = (200,)
precs_10.shape  = (200,)


alpha           = .05
tukey_maps      = pairwise_tukeyhsd(maps, names, alpha)
tukey_rprecs    = pairwise_tukeyhsd(rprecs, names, alpha)
tukey_precs_10  = pairwise_tukeyhsd(precs_10, names, alpha)

# github markdown
print("```")
print(tukey_maps)
print()
print(tukey_rprecs)
print()
print(tukey_precs_10)
print("```")

# saving plots
tukey_maps.plot_simultaneous("bm25_full").savefig("./figures/tukey_maps.png")
tukey_rprecs.plot_simultaneous("bm25_full").savefig("./figures/tukey_rprecs.png")
tukey_precs_10.plot_simultaneous("bm25_full").savefig("./figures/tukey_precs_10.png")
