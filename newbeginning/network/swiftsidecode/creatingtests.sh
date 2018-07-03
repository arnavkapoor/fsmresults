new=($(basename $1))
python ./prefix-gen.py ./allregexnew/$new
python ./transitionpairnetwork.py ./allregexnew/$new
python ./alternate-testgen.py ./transition-pairs-network/$new ./prefix-list-network/$new
sed -i -e "s/[[:space:]]\+/ /g" ./transition-pair-tests-network/$new

