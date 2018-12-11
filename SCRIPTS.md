## Documentation


### `_main.sh`
`main.sh` will sequentially execute:

1. `_preprocessing.sh`;
1. `_indexing.sh`;
1. `_retrieval.sh`;
1. `_evaluation.sh`.
___

### `_preprocessing.sh`
This script performs some basic sanity checks and creates the folders needed for its correct execution. It also renames `.{1,2,3}Z` files to `_{1,2,3}.Z` files and uncompresses them  using `uncompress`. If something goes wrong with these commands then `sanitize_z_format.py` is executed, this python script will rename and uncompress the files in the same manner, but it will not trigger parsing errors (which may occur on some OS + Shell configurations). Finally the script will tell Terrier to update the `collection.spec` file.

___

### `_indexing.sh`
This script spawns 3 subprocesses making each one of them execute Terrier with different parameteres as requesteb by the homework. Follows one of the commands:
```bash
sh terrier/bin/trec_terrier.sh -i \
-Dterrier.index.path=indexes/full \
-Dtermpipelines=Stopwords,PorterStemmer  
```
If everything executes correctly there will be 3 new folders inside `terrier/var/indexes` called `full`, `nostop`, and `none`. 

- `full` - index created using both PorterStemmer and Stopwords removal;
- `nostop` - index created using only the PorterStemmer;
- `none` - index that involves neither Stemming nor Stopwords removal.

From now on, when invoking a Terrier command, we need to specify on which index we want the command to be executed. That can be done with the inline parameter `-Dterrier.index.path=indexes/{full, nostop, none}`.
___

### `_retrieval.sh`
This script executes Terrier with different parameters (i.e. using different retrieval models), this time however, given the fast execution time, the tasks are executed sequentially and not in parallel. In this phase the topics contained in `data/topics.351-400_trec7.txt` will be queried to our systems which by using different combinations of index + retrieval model will return a list of documents deemed to be relevant for a given topic. Follows one of the commands:

```
sh terrier/bin/trec_terrier.sh -r \
-Dterrier.index.path=indexes/full \
-Dterrier.results=results \
-Dtrec.results.file=bm25_full.res \
-Dtrec.model=BM25 \
-Dtermpipelines=Stopwords,PorterStemmer
```
If everything goes as expected there will be 4 new files (8 actually) inside `terrier/var/results`.

- `bm25_full.res` - run file by the system using BM25 as retrieval model and `full` as index;
- `tf_idf_full.res` - run file by the system using TF_IDF as retrieval model and `full` as index;
- `bm25_nostop.res` - run file by the system using BM25 as retrieval model and `nostop` as index;
- `tf_idf_none.res` - run file by the system using TF_IDF as retrieval model and `none` as index.

___

### `_evaluation.sh` 
This script tells Terrier to compare the `.res` files in `terrier/var/results` against the ground truth represented by `data/qrels.trec7.txt`. Terrier calls `trec_eval.sh` under the hood which will compute compute some useful evaluation measures for each system and for each topic. 

If no errors arise there will be 4 new `.txt` files inside `terrier/var/evaluation`.
- `bm25_full.txt` - evaluation measure for the system using BM25 as retrieval model and `full` as index;
- `tf_idf_full.txt` - evaluation measure for the system using TF_IDF as retrieval model and `full` as index;
- `bm25_nostop.txt` - evaluation measure for the system using BM25 as retrieval model and `nostop` as index;
- `tf_idf_none.txt` - evaluation measure for the system using TF_IDF as retrieval model and `none` as index.

___

### `_plots.sh`

This script prints some tables on `stdout` and produces some plots to better visualize differences in performance among the different systems. Plots are saved in the `figures` folder. Refer to the [FIGURES.md](FIGURES.md) for more info about the figures.
