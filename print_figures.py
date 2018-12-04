import numpy as np
import matplotlib.pyplot as plt

files = ["bm25_full.txt", "tf_idf_full.txt", "bm25_nostop.txt", "tf_idf_none.txt"]

evals = np.loadtxt("./terrier/var/evaluation/{}".format(files[0]), skiprows=2, dtype=str)

# topic 'all' contains 94 metrics
# every other topic t in [351, 400] cotains 91 metrics

topic       = "all"

num_ret     = [int(x[2]) for x in evals if x[1] == topic and x[0] == "num_ret"][0]
num_rel     = [int(x[2]) for x in evals if x[1] == topic and x[0] == "num_rel"][0]
num_rel_ret = [int(x[2]) for x in evals if x[1] == topic and x[0] == "num_rel_ret"][0]
mean_ap     = [float(x[2]) for x in evals if x[1] == topic and x[0] == "map"][0]
rprec       = [float(x[2]) for x in evals if x[1] == topic and x[0] == "Rprec"][0]
precisions  = [float(x[2]) for x in evals if x[1] == topic and x[0][:2] == "P_"]
recalls     = [float(x[2]) for x in evals if x[1] == topic and x[0][:7] == "recall_"]
iprecs      = [float(x[2]) for x in evals if x[1] == topic and x[0][:6] == "iprec_"]


p_r_curve = plt.figure()
