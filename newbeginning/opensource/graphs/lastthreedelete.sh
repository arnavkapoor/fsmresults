for files in ./individualcsv/*
do
	head -n -3 $files > temp.txt
	cp temp.txt $files
	rm temp.txt
done
