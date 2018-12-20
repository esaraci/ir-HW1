 
### MAP, RPrec, P@10 across the different systems for `topic=all`
| Model                                   |    MAP |   RPrec |   P@10 |
|:----------------------------------------|-------:|--------:|-------:|
| BM25 - PorterStemmer + Stopwords        | 0.1828 |  0.2391 |  0.418 |
| TF_IDF - PorterStemmer + Stopwords      | 0.1821 |  0.2391 |  0.42  |
| BM25 - PorterStemmer, NO Stopwords      | 0.1857 |  0.2409 |  0.43  |
| TF_IDF - NO PorterStemmer, NO Stopwords | 0.1693 |  0.229  |  0.406 |

### ANOVA-1-WAY results for MAP, RPREC, P@10
| Measure |    F-stat |  p-value  | 
|:--------|----------:|----------:| 
| MAP     | F: 0.0997 | p: 0.9601 |
| RPREC   | F: 0.0567 | p: 0.9822 |
| P@10    | F: 0.0446 | p: 0.9875 |



### Multiple Comparison of Means (MAP) - Tukey HSD, family-wise error rate (FWER)=0.05  

|    group1   |    group2   | meandiff |  lower  | upper  |  reject |
|:-----------:|:-----------:|---------:|--------:|-------:|--------:|
|  bm25_full  | bm25_nostop |  0.0029  | -0.0816 | 0.0874 |  False  |
|  bm25_full  | tf_idf_full | -0.0006  | -0.0851 | 0.0838 |  False  |
|  bm25_full  | tf_idf_none | -0.0135  |  -0.098 | 0.071  |  False  |
| bm25_nostop | tf_idf_full | -0.0035  |  -0.088 | 0.081  |  False  |
| bm25_nostop | tf_idf_none | -0.0164  | -0.1008 | 0.0681 |  False  |
| tf_idf_full | tf_idf_none | -0.0128  | -0.0973 | 0.0716 |  False  |


### Multiple Comparison of Means (RPRECS) - Tukey HSD, family-wise error rate (FWER)=0.05  

|    group1   |    group2   | meandiff |  lower  | upper  | reject |
|:------------|:-----------:|---------:|--------:|-------:|-------:|
|  bm25_full  | bm25_nostop |  0.0018  | -0.0818 | 0.0854 | False  |
|  bm25_full  | tf_idf_full |   -0.0   | -0.0837 | 0.0836 | False  |
|  bm25_full  | tf_idf_none | -0.0101  | -0.0938 | 0.0735 | False  |
| bm25_nostop | tf_idf_full | -0.0018  | -0.0855 | 0.0818 | False  |
| bm25_nostop | tf_idf_none | -0.0119  | -0.0956 | 0.0717 | False  |
| tf_idf_full | tf_idf_none | -0.0101  | -0.0937 | 0.0736 | False  |

### Multiple Comparison of Means (P@10) - Tukey HSD, family-wise error rate (FWER)=0.05 

|    group1   |    group2   | meandiff | lower  | upper | reject |
|:-----------:|:-----------:|---------:|-------:|------:|-------:|
|  bm25_full  | bm25_nostop |  0.012   | -0.159 | 0.183 | False  |
|  bm25_full  | tf_idf_full |  0.002   | -0.169 | 0.173 | False  |
|  bm25_full  | tf_idf_none |  -0.012  | -0.183 | 0.159 | False  |
| bm25_nostop | tf_idf_full |  -0.01   | -0.181 | 0.161 | False  |
| bm25_nostop | tf_idf_none |  -0.024  | -0.195 | 0.147 | False  |
| tf_idf_full | tf_idf_none |  -0.014  | -0.185 | 0.157 | False  |
___

- Scripts documentation [HERE](docs/SCRIPTS.md)
- Figures documentation [HERE](docs/FIGURES.md)
- Tables documentation [you are here]
- `terrier.properties` [HERE](terrier.properties)
