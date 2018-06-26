for file in ~/fsm/tests/allregex/*
do
	count=($(wc $file))
	new=($(basename $file))
	echo ".i 1" >> ~/fsm/tests/allregexnew/$new 
	echo ".o 1" >> ~/fsm/tests/allregexnew/$new
	echo ".s 2" >> ~/fsm/tests/allregexnew/$new
	echo ".p $count" >> ~/fsm/tests/allregexnew/$new
	echo ".b 10" >> ~/fsm/tests/allregexnew/$new
	cat $file >> ~/fsm/tests/allregexnew/$new
#	python prefix-gen.py ~/fsm/tests/allregexnewopensrc/$new
#	python transitionpairnetwork.py ~/fsm/tests/allregexnew/$new
#	python alternate-testgen.py ~/fsm/tests/transition-pairs/$new ~/fsm/tests/prefix-list/$new
done

# for file in ~/fsm/tests/allregexopensrc/*
# do
# 	new=($(basename $file))	
# 	python transitionpairnetwork.py ~/fsm/tests/opensrcexpanded/$new

# done

# for file in ~/fsm/tests/transition-pairs-opensrc/*
# do
# 	new=($(basename $file))	
# 	python alternate-testgen.py ~/fsm/tests/transition-pairs-opensrc/$new ~/fsm/tests/prefix-list-opensrc/$new
# done