## Figures

### `iprc.png` - Interpolated Precision Recall Curve (@ recall levels)
![iprc.png](../figures/iprc.png)

#### Interpretation
The shape of the curves is very much expected,
> enforcing the notion that as more **relevant** documents are retrieved (recall increases), the more **nonrelevant** documents are retrieved (precision decreases) [[1]](https://trec.nist.gov/pubs/trec16/appendices/measures.pdf)

At `recall=0.2` and `recall=0.8` I drew two vertical dashed grey lines to ease the comparison among the systems (as suggested in [[1]](https://trec.nist.gov/pubs/trec16/appendices/measures.pdf)).

Judging by the plot we can see that performance levels are more or less the same except for the one system that performs slightly worse than the others in range `[0.2, 0.8]`.

The file listed below shows the Precision Recall Curve at different document cutoffs (`[5,10,15,20,30,100,200,500,1000]`). There are no major changes in the shapes of the curves with respect to the graph above.
- `prc.png` - [Precision Recall Curve (@ document cutoffs)](../figures/prc.png)
___

### `distr_maps.png` - Distribution of MAP values across the 50 topics (Boxplots)
![prc.png](../figures/distr_maps.png)

#### Interpretation

Unfortunately the distribution of the measured MAP values on all the topics  is not that insightful. All systems' performances are very similar to each other which suggests that there is no empirical proof of a _significant_ difference among them. At later stages, it is actually verified that no system brings a (statistically) _significant_ improvement over the others.

Please note that the name "MAP" is just used for consistency with Terrier, the actual measure is "AP" or "Average Precision".

The files listed below show the distributions of RPrec and P@10 for the same context, since they are very similar (_intepretation_-wise) to the graph above, no further documentation is provided for them.
- `distr_rprecs.png` - [Distribution of RPrecs values across the 50 topics (Boxplots)](../figures/distr_rprecs.png)
- `distr_precs_10.png` - [Distribution of P@10s values across the 50 topics (Boxplots)](../figures/distr_precs_10.png)
___

### `tukey_maps.png` - Confidence intervals for each system on MAP
![prc.png](../figures/tukey_maps.png)

#### Interpretation

Tukey's HSD test tells us that none of the system is significantly better than the others (at significance level 0.05). That said we see however a trend in which the system that uses `TF_IDF` as a retrieval model with no stemming nor stopword removal (i.e. `tf_idf_none`) performs constantly worse then the others. The same behavior is reported in the figures listed below for RPrec and P@10. As for tukey's result we can not really say that there are different groups of systems. 

- the system marked in blue is the system I thought would perform slightly better than the others in all measures;
- grey systems are those who are not significantly different from the blue one; 
- red systems are those significantly different from the blue system, their confidence intervals would be disjoint. (none in this homework)

Figures listed below show the same graph but for different measures. The interpretation is fundamentally the same.
- `distr_rprecs.png` - [Confidence intervals for each system on RPrecs](../figures/tukey_rprecs.png)
- `distr_precs_10.png` - [Confidence intervals for each system on P@10](../figures/tukey_precs_10.png)
___
- Main documentation [HERE](../README.md)
- Scripts documentation [HERE](SCRIPTS.md)
- Figures documentation [you are here]
- Tables documentation [HERE](TABLES.md)
- `terrier.properties` [HERE](../terrier.properties)
