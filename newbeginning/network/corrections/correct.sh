while IFS='' read -r line || [[ -n "$line" ]]; do
    nm=`echo "$line" | cut -d ' ' -f1`
    tc=`echo "$line" | cut -d ' ' -f2`
    sed -i -r '3s/\S+//3' $tc
done < "$1"
