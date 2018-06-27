new=($(basename $1))
python ~/fsm/tests/prefix-gen.py ${HOME}/fsm/tests/allregexnew/$new
python ~/fsm/tests/transitionpairnetwork.py ${HOME}/fsm/tests/allregexnew/$new
python ~/fsm/tests/alternate-testgen.py ${HOME}/fsm/tests/transition-pairs-network/$new ~/fsm/tests/prefix-list-network/$new
cp ${HOME}/fsm/tests/transition-pair-tests-network/$new temp.txt
cat temp.txt | shuf | cut -d " " -f 2 | nl -nln > ${HOME}/fsm/tests/transition-pair-tests-network/$new
rm temp.txt
