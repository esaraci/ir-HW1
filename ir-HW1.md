## Information Retrieval HW1



#### Primo passo: `collection.spec`

Come primo passo è necessario generare il file `etc/collection.spec` il quale dovrà contenere tutti i file da indicizzare. Lo si può creare manualmente, semplicemente aggiungendo un path per riga oppure utilizzando il comando `sh bin/trec_setup.sh /path/to/collection`



#### Secondo passo: `terrier.properties`

Il secondo passo prevede la modifica del file `etc/terrier.properties` nel quale verranno inserite tutte le configurazioni utili per le differenti run.

Segue un template:

```
#### [QUERY EXPANSION SETTINGS] ####
#default controls for query expansion
querying.postprocesses.order=QueryExpansion
querying.postprocesses.controls=qe:QueryExpansion
#default controls for the web-based interface. SimpleDecorate
#is the simplest metadata decorator. For more control, see Decorate.
querying.postfilters.order=SimpleDecorate,SiteFilter,Scope
querying.postfilters.controls=decorate:SimpleDecorate,site:SiteFilter,scope:Scope

#default and allowed controls
querying.default.controls=
querying.allowed.controls=scope,qe,qemodel,start,end,site,scope

#### [TREC DOCUMENT SETTINGS] ####
TrecDocTags.doctag=DOC
TrecDocTags.idtag=DOCNO
TrecDocTags.skip=DOCHDR
TrecDocTags.casesensitive=false

#### [TREC QUERY SETTINGS] ####
TrecQueryTags.doctag=top
TrecQueryTags.idtag=num
TrecQueryTags.process=title, desc
TrecQueryTags.skip=narr
TrecQueryTags.casesensitive=false

#### [COLLECTION/ENCODING SETTINGS] ####
tokeniser=EnglishTokeniser
trec.encoding=UTF-8
trec.collection.class=TRECCollection
trec.document.class=FileDocument

#### [INDEX SETTINGS] ####
indexer.meta.forward.keys=filename
indexer.meta.forward.keylens=512
indexing.simpleFilecollection.recurse=true

#### [INDEX PATH] ####
terrier.index.path=var/index

#### [PIPELINE SETTINGS] ####
stopwords.filename=stopword-list.txt
termpipelines=Stopwords,PorterStemmer
```



#### Terzo passo: `indexing`

Il terzo passo consiste nella indicizzazione. Il comando per fare ciò è: `sh bin/trec_terrier.sh -i`. Gli indici generati si trovano nella cartella `var/index`, la destinazione può essere cambiata nel tramite il file `etc/terrier.properties`.

Per esplorare l'indice possiamo utilizzare i seguenti comandi:

```
--printlexicon		contenuto del lexicon
--printinverted		contentuo dell'indice inverso
--printdirect		contenuto dell'indice diretto	
--printstats		statistiche
--printmeta			the meta structure
```



#### Quarto passo: `evaluation`

Il comando per effettuare una valutazione *set-based* è `sh bin/trec_eval -q -m set pool.txt run.txt`, mentre quello per effettuare una valutazione *rank-based* è `sh bin/trec_eval -q -m all_trec pool.txt run.txt`



#### Proprietà avanzate

Inserendo la riga `ignore.low.idf.terms=true` nel file `etc/terrier.properties` 

```
ignore.low.idf.terms=true		# ignora valori bassi di ID
max.term.length=20				# lunghezza max termini da indicizzare
terrier.index.path=path/		# dove salvare l'indice

# considerare le maiuscole
org.terrier.indexing.TRECFullTokenizer=true
```





##### Recap

![](/home/esaraci/Projects/ir-HW1/assets/Screenshot_20181126_095913.png)

