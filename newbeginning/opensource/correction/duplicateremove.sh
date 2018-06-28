for file in ~/fsmresults/newbeginning/opensource/opensrcexpanded/*
do
	awk '!x[$0]++' $file > temp.text
	cat temp.text > $file
	rm temp.text
done
