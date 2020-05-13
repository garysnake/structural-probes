#  Use this file to convert trainable data!
# Required tsv file, change name in the for loop

for file in `find /home/garysnake/packages/stanford-corenlp-full-2018-10-05/ -name "*.jar"`; do
        export CLASSPATH="$CLASSPATH:`realpath $file`";
done

# Convert Raw to Tree format
# java -mx200m edu.stanford.nlp.parser.lexparser.LexicalizedParser -retainTMPSubcategories -outputFormat "penn" /home/garysnake/packages/stanford-corenlp-full-2018-10-05/edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz temp.txt > temp.tree

# Convert Raw to parsed conllx format only need to change from -treeFile to -sentFile
for name in 'in_domain_dev' 'in_domain_train' 'out_of_domain_dev'; do
        python3 support_script/convert_tsv_to_raw.py  tsv/${name}.tsv  ${name}.raw
        java -mx1g edu.stanford.nlp.trees.EnglishGrammaticalStructure -sentFile ${name}.raw -checkConnected -basic -keepPunct -conllx > ${name}.conllx
        # Important convert back to raw, to have consistent raw file with parsed conllx
        python3 support_script/convert_conll_to_raw.py ${name}.conllx ${name}.raw
done