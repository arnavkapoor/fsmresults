for file in ~/fsm/tests/allregexnew/*
do
 	new=($(basename $file))
 	python prefix-gen.py ~/fsm/tests/allregexnew/$new
done

for file in ~/fsm/tests/prefix-list-network/*
do
 	new=($(basename $file))	
 	python transitionpairnetwork.py ~/fsm/tests/allregexnew/$new
done

for file in ~/fsm/tests/transition-pairs-network/*
do
 	new=($(basename $file))	
 	python alternate-testgen.py ~/fsm/tests/transition-pairs-network/$new ~/fsm/tests/prefix-list-network/$new
 done
