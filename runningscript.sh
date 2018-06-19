for file in ~/allregexnew/*
do

	basenm=$(basename "$file")
	noextension=`echo "$basenm"| cut -d '.' -f1`
 
	no_of_transitions=`cat "$file"|wc -l` 
	no_of_transitions=$((no_of_transitions-5))
	

	if [ $no_of_transitions -ne 0 ]
	then
		sed -i "/#define NUM_TRANSITIONS_KERNEL/s/.*/#define NUM_TRANSITIONS_KERNEL ${no_of_transitions}/" ~/partecl-runtime/kernel-gen/compile_const.h
		echo "// blank comment" >> ~/partecl-runtime/source/main-working.cl	
		no_of_tests=`cat ~/transition-pair-tests/"$basenm" | wc -l`
		echo $no_of_tests	
			
		mkdir -p ~/cputestresults/$basenm
		mkdir -p ~/gputestresults/$basenm	
		
		cp ~/transition-pair-tests/"$basenm" ~/partecl-runtime/kernel-gen/tests.txt	
		
		if [ 256 -le $no_of_tests ]
		then	
			filesave="256_1_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 256 Y N 100 1 ~/allregexnew/"$basenm" > ~/cputestresults/$basenm/$filesave  	
		
				
			filesave="256_4_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 256 Y N 100 4 ~/allregexnew/"$basenm" > ~/cputestresults/$basenm/$filesave  	
			  
			filesave="256_8_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 256 Y N 100 8 ~/allregexnew/"$basenm" > ~/cputestresults/$basenm/$filesave  	
			  
			filesave="256_32_"$noextension".test"
			~/partecl-runtime/build/cpu-test 256 -time Y -results N -runs 100 -filename ~/allregexnew/"$basenm" > ~/cputestresults/$basenm/$filesave  		
			
			filesave="256_"$noextension".test"  		
			~/partecl-runtime/build/gpu-test 256 -time Y -results N -runs 100 -filename ~/allregexnew/"$basenm" > ~/gputestresults/$basenm/$filesave
		
		fi		

                if [ 4096 -le $no_of_tests ]
                then
                
			filesave="4096_1_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 4096 Y N 100 1 ~/allregexnew/"$basenm" > ~/cputestresults/$basenm/$filesave  	
			
			filesave="4096_4_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 4096 Y N 100 4 ~/allregexnew/"$basenm" > ~/cputestresults/$basenm/$filesave  	
			  
			filesave="4096_8_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 4096 Y N 100 8 ~/allregexnew/"$basenm" > ~/cputestresults/$basenm/$filesave  	
			  
			filesave="4096_32_"$noextension".test"
			~/partecl-runtime/build/cpu-test 4096 -time Y -results N -runs 100 -filename  ~/allregexnew/"$basenm" > ~/cputestresults/$basenm/$filesave  		
		
			
			filesave="4096_"$noextension".test"  		
			~/partecl-runtime/build/gpu-test 4096 -time Y -results N -runs 100 -filename ~/allregexnew/"$basenm" > ~/gputestresults/$basenm/$filesave
		
		fi

                if [ 16384 -le $no_of_tests ]
                then
                
			filesave="16384_1_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 16384 Y N 100 1 ~/allregexnew/"$basenm" > ~/cputestresults/$basenm/$filesave  	
			
			filesave="16384_4_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 16384 Y N 100 4 ~/allregexnew/"$basenm" > ~/cputestresults/$basenm/$filesave  	
			  
			filesave="16384_8_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 16384 Y N 100 8 ~/allregexnew/"$basenm" > ~/cputestresults/$basenm/$filesave  	
			  
			filesave="16384_32_"$noextension".test"
			~/partecl-runtime/build/cpu-test 16384 -time Y -results N -runs 100 -filename ~/allregexnew/"$basenm" > ~/cputestresults/$basenm/$filesave  		
		
			
			filesave="16384_"$noextension".test"  		
			~/partecl-runtime/build/gpu-test 16384 -time Y -results N -runs 100 -filename ~/allregexnew/"$basenm" > ~/gputestresults/$basenm/$filesave
		
		fi		
		

                if [ 65536 -le $no_of_tests ]
                then
                
			filesave="65536_1_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 65536 Y N 100 1 ~/allregexnew/"$basenm" > ~/cputestresults/$basenm/$filesave  	
			
			filesave="65536_4_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 65536 Y N 100 4 ~/allregexnew/"$basenm" > ~/cputestresults/$basenm/$filesave  	
			  
			filesave="65536_8_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 65536 Y N 100 8 ~/allregexnew/"$basenm" > ~/cputestresults/$basenm/$filesave  	
			  
			filesave="65536_32_"$noextension".test"
			~/partecl-runtime/build/cpu-test 65536 -time Y -results N -runs 100 -filename ~/allregexnew/"$basenm" > ~/cputestresults/$basenm/$filesave  		
		
			
			filesave="65536_"$noextension".test"  		
			~/partecl-runtime/build/gpu-test 65536 -time Y -results N -runs 100 -filename ~/allregexnew/"$basenm" > ~/gputestresults/$basenm/$filesave
		
		fi		
		

                if [ 131072 -le $no_of_tests ]
                then
		
			filesave="131072_1_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 131072 Y N 100 1 ~/allregexnew/"$basenm" > ~/cputestresults/$basenm/$filesave  	
			
			filesave="131072_4_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 131072 Y N 100 4 ~/allregexnew/"$basenm" > ~/cputestresults/$basenm/$filesave  	
			  
			filesave="131072_8_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 131072 Y N 100 8 ~/allregexnew/"$basenm" > ~/cputestresults/$basenm/$filesave  	
			  
			filesave="131072_32_"$noextension".test"
			~/partecl-runtime/build/cpu-test 131072 -time Y -results N -runs 100 -filename ~/allregexnew/"$basenm" > ~/cputestresults/$basenm/$filesave  		
                
			
			filesave="131072_"$noextension".test"  		
			~/partecl-runtime/build/gpu-test 131072 -time Y -results N -runs 100 -filename ~/allregexnew/"$basenm" > ~/gputestresults/$basenm/$filesave
		
		fi

		
			filesave=""$no_of_tests"_1_"$noextension".test"
			timeout 120 bash ~/partecl-runtime/build/openmp-run.sh $no_of_tests Y N 100 1 ~/allregexnew/"$basenm" > ~/cputestresults/$basenm/$filesave  	
			
			filesave=""$no_of_tests"_4_"$noextension".test"
			timeout 120 bash ~/partecl-runtime/build/openmp-run.sh $no_of_tests Y N 100 4 ~/allregexnew/"$basenm" > ~/cputestresults/$basenm/$filesave  	
			  
			filesave=""$no_of_tests"_8_"$noextension".test"
			timeout 120 bash ~/partecl-runtime/build/openmp-run.sh $no_of_tests Y N 100 8 ~/allregexnew/"$basenm" > ~/cputestresults/$basenm/$filesave  	
			  
			filesave=""$no_of_tests"_32_"$noextension".test"
			timeout 120 ~/partecl-runtime/build/cpu-test $no_of_tests -time Y -results N -runs 100 -filename ~/allregexnew/"$basenm" > ~/cputestresults/$basenm/$filesave  		
         
			filesave=""$no_of_tests"_"$noextension".test"  		
			timeout 120 ~/partecl-runtime/build/gpu-test $no_of_tests -time Y -results N -runs 100 -filename ~/allregexnew/"$basenm" > ~/gputestresults/$basenm/$filesave
		
		if [ $no_of_tests -ge 1000000 ]
			then
			
			filesave="1024000_"$noextension".test"  		
			timeout 120 ~/partecl-runtime/build/gpu-test 1024000 -time Y -results N -runs 100 -filename ~/allregexnew/"$basenm" > ~/gputestresults/$basenm/$filesave
			
			filesave="1024000_1_"$noextension".test"
			timeout 120 bash ~/partecl-runtime/build/openmp-run.sh 1024000 Y N 100 1 ~/allregexnew/"$basenm" > ~/cputestresults/$basenm/$filesave  		
			
			filesave="1024000_4_"$noextension".test"
			timeout 120 bash ~/partecl-runtime/build/openmp-run.sh 1024000 Y N 100 4 ~/allregexnew/"$basenm" > ~/cputestresults/$basenm/$filesave  		
			
			filesave="1024000_8_"$noextension".test"
			timeout 120 bash ~/partecl-runtime/build/openmp-run.sh 1024000 Y N 100 8 ~/allregexnew/"$basenm" > ~/cputestresults/$basenm/$filesave  		
			
			filesave="1024000_32_"$noextension".test"
			timeout 120 ~/partecl-runtime/build/cpu-test 1024000 -time Y -results N -runs 100 -filename  ~/allregexnew/"$basenm" > ~/cputestresults/$basenm/$filesave  		
			
			
		fi
	fi
done
