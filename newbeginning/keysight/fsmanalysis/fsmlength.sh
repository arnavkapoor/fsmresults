for file in ../swiftsidecode/transition-pair-tests-network/*
do
	total=0
	my_array=( $(cat $file | cut -d " " -f2) )
	for var in "${my_array[@]}"
	do
  		total=$((total+var))
  	done
	echo $((total/${#myarray[@]}))
done
