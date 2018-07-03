get_seeded_random()
{
  seed="$1"
  openssl enc -aes-256-ctr -pass pass:"$seed" -nosalt \
    </dev/zero 2>/dev/null
}

new=($(basename $1))
python ./prefix-gen.py ./allregexnew/$new
python ./transitionpairnetwork.py ./allregexnew/$new
python ./better-testgen.py ./transition-pairs-network/$new ./prefix-list-network/$new
cp ./transition-pair-tests-network/$new temp.txt
cat temp.txt| shuf --random-source=<(get_seeded_random 42) | cut -d " " -f 2 | nl -nln > ./transition-pair-tests-network/$new
rm temp.txt
sed -i -e "s/[[:space:]]\+/ /g" ./transition-pair-tests-network/$new
