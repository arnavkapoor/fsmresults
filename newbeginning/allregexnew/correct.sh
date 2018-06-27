while IFS='' read -r line || [[ -n "$line" ]]; do
    nm=`echo "$line" | cut -d ' ' -f1`
    tc=`echo "$line" | cut -d ' ' -f2`
    sed -i -e "3s/\.s/\.s $nm/g" $tc
    echo $nm	
done < "$1"
