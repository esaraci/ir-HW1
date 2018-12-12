 
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
