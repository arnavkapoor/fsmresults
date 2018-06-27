for file in ~/fsmresults/newbeginning/opensource/opensrcexpanded/*
do
	sort -u -o "$file" "$file"
done
