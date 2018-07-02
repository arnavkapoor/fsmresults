new=($(basename $1))
python ./prefix-gen.py ../opensrcexpanded/$new
python ./transitionpairnetwork.py ../opensrcexpanded/$new
python ./alternate-testgen.py ./transition-pairs-network/$new ./prefix-list-network/$new
cp ./transition-pair-tests-network/$new temp.txt
cat temp.txt | shuf | cut -d " " -f 2 | nl -nln > ./transition-pair-tests-network/$new
sed -i -e "s/[[:space:]]\+/ /g" ./transition-pair-tests-network/$new
rm temp.txt
