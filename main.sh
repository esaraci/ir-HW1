# author: Eugen Saraci
# date  : 03/12/18


# it is recommeded not to execute tasks on their own unless the whole pipeline is clear
# call steps sequentially, if one step fails the following steps won't be executed
sh _preprocessing.sh && sh _indexing.sh && sh _retrieval.sh && sh _evaluation.sh && _plots.sh
