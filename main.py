#! /usr/bin/env python


"""
this is a bad terrier wrapper
"""

import os
import argparse
import json



"""
parser.add_argument("-M", "--model", required=True, help='retrieval model', default="BM25", choices=["BM25", "TF_IDF"])
parser.add_argument("-sm","--setup-mode", help="executes trec_setup.sh")
parser.add_argument("-im", "--index-mode", help="executes trec_terrier.sh -i")
parser.add_argument("-em", "--eval-mode")

args = vars(parser.parse_args())
print(args)
"""


if __name__ == "__main__":
    print("ll")
    main_parser = argparse.ArgumentParser(description="A 'not so good' Python wrapper for Terrier.")

    subparsers = main_parser.add_subparsers(title="mode", description="select which step you want to perform",
                                            help="additional help")

    setup_parser = subparsers.add_parser("setup", aliases=["S"])
    index_parser = subparsers.add_parser("index", aliases=["I"])
    eval_parser = subparsers.add_parser("eval", aliases=["E"])

    # setup args
    setup_parser.add_argument("-i", "--input", help="collection's path")

    # indexing args
    index_parser.add_argument("--sw", "--stopwords", type=bool, default=False, help="activates stopwords")
    index_parser.add_argument("--ps", "--porterstemmer", type=bool, default=False, help="uses Porter Stemmer")
    index_parser.add_argument("--of", "--outputfolder", type=str, help="path of where the index will be stored")

    # bin / trec_terrier.sh - i -Dtermpipelines=Stopwords
    # -Dignore.low.idf.terms=true
    # -Dterrier.index.path=none, --printlexicon etc
    # evaluation args
    index_parser.add_argument("--em", "--stopwords", type=bool, default=False, help="activates stopwords removal")

    args = vars(main_parser.parse_args())
    print(args)
