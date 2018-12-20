### MAP, RPrec, P@10 across the different systems for `topic=all`

| Model                                   |    MAP |   RPrec |   P@10 |
|:----------------------------------------|-------:|--------:|-------:|
| BM25 - PorterStemmer + Stopwords        | 0.2126 |  0.2705 |  0.484 |
| TF_IDF - PorterStemmer + Stopwords      | 0.212  |  0.2725 |  0.48  |
| BM25 - PorterStemmer, NO Stopwords      | 0.2108 |  0.274  |  0.474 |
| TF_IDF - NO PorterStemmer, NO Stopwords | 0.1875 |  0.246  |  0.43  |

### ANOVA-1-WAY results for MAP, RPREC, P@10

| Measure |   F-stat   |   p-value  | 
|:--------|-----------:|-----------:| 
| MAP     | F: 0.2699 | p: 0.8471 |
| RPREC   | F: 0.3508 | p: 0.7886 |
| P@10    | F: 0.3578 | p: 0.7836 |

```
  Multiple Comparison of Means - Tukey HSD,FWER=0.05  
======================================================
   group1      group2   meandiff  lower  upper  reject
------------------------------------------------------
 bm25_full  bm25_nostop -0.0018  -0.0877 0.0842 False 
 bm25_full  tf_idf_full -0.0005  -0.0865 0.0855 False 
 bm25_full  tf_idf_none -0.0251  -0.1111 0.0609 False 
bm25_nostop tf_idf_full  0.0012  -0.0848 0.0872 False 
bm25_nostop tf_idf_none -0.0233  -0.1093 0.0626 False 
tf_idf_full tf_idf_none -0.0246  -0.1106 0.0614 False 
------------------------------------------------------

  Multiple Comparison of Means - Tukey HSD,FWER=0.05  
======================================================
   group1      group2   meandiff  lower  upper  reject
------------------------------------------------------
 bm25_full  bm25_nostop  0.0034  -0.0786 0.0854 False 
 bm25_full  tf_idf_full  0.0019  -0.0801 0.0839 False 
 bm25_full  tf_idf_none -0.0246  -0.1066 0.0574 False 
bm25_nostop tf_idf_full -0.0015  -0.0835 0.0805 False 
bm25_nostop tf_idf_none  -0.028   -0.11  0.054  False 
tf_idf_full tf_idf_none -0.0265  -0.1085 0.0555 False 
------------------------------------------------------

  Multiple Comparison of Means - Tukey HSD,FWER=0.05  
======================================================
   group1      group2   meandiff  lower  upper  reject
------------------------------------------------------
 bm25_full  bm25_nostop  -0.01   -0.1632 0.1432 False 
 bm25_full  tf_idf_full  -0.004  -0.1572 0.1492 False 
 bm25_full  tf_idf_none  -0.054  -0.2072 0.0992 False 
bm25_nostop tf_idf_full  0.006   -0.1472 0.1592 False 
bm25_nostop tf_idf_none  -0.044  -0.1972 0.1092 False 
tf_idf_full tf_idf_none  -0.05   -0.2032 0.1032 False 
```
___

- Main documentation [HERE](../README.md)
- Scripts documentation [HERE](SCRIPTS.md)
- Figures documentation [HERE](FIGURES.md)
- Tables documentation [you are here]
- `terrier.properties` [HERE](../terrier.properties)
