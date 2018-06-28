while IFS='' read -r line || [[ -n "$line" ]]; do
    nm=`echo "$line" | cut -d ' ' -f1`
    tc=`echo "$line" | cut -d ' ' -f2`
    sed -i "3s/.s/.s $nm/" ../opensrcexpanded/$tc
    sed -i -r '3s/\S+//3' ../opensrcexpanded/$tc
    
done < "$1"
