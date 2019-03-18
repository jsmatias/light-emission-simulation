#rm p0.txt p1.txt
if [ ! -f p1.txt ]; then
tail -n +39 $1 > p0.txt

awk '{gsub("Energy:", "");print}' p0.txt  > p1.txt
sed 's/Norma:(//'       p1.txt  > p0.txt
sed 's/L^2:L(L+1):(//'  p0.txt  > p1.txt
sed 's/S^2:S(S+1):(//'  p1.txt  > p0.txt
sed 's/Q(Racah):(//'    p0.txt  > p1.txt
sed 's/R(Racah):(//'    p1.txt  > p0.txt
sed 's/M:(//'           p0.txt  > p1.txt
sed 's/)//'             p1.txt  > p0.txt
sed 's/)//'             p0.txt  > p1.txt
sed 's/)//'             p1.txt  > p0.txt
sed 's/)//'             p0.txt  > p1.txt
sed 's/)//'             p1.txt  > p0.txt
sed 's/)//'             p0.txt  > p1.txt
sed 's/,/   /'          p1.txt  > p0.txt
sed 's/,/   /'          p0.txt  > p1.txt
sed 's/,/   /'          p1.txt  > p0.txt
sed 's/,/   /'          p0.txt  > p1.txt
sed 's/,/   /'          p1.txt  > p0.txt
sed 's/,/   /'          p0.txt  > p1.txt

fi

exit
################################################################################

for dir in Er_W_*; do echo $dir; cd $dir; bash ../DejoSoloEspectro.sh ErenNaYF4.o* ; cd ../.  ; done

for dir in Er_W_*; do echo $dir; cd $dir; fin=${dir#Er_}; echo $fin; cp p1.txt soloEspectro_${fin}.txt ; cd ../.  ; done

for dir in Er_W_*; do echo $dir; cd $dir; cp soloEspectro_*.txt ../. ; cd ../.  ; done


tar -cf todosEspectros.tar soloEspectro_W_-*

gzip todosEspectros.tar 


################################################################################

for dir in Er_A4_*; do echo $dir; cd $dir; bash ../DejoSoloEspectro.sh ErenNaYF4.o* ; cd ../.  ; done

for dir in Er_A4_*; do echo $dir; cd $dir; fin=${dir#Er_}; echo $fin; cp p1.txt soloEspectro_${fin}.txt ; cd ../.  ; done

for dir in Er_A4_*; do echo $dir; cd $dir; cp soloEspectro_*.txt ../. ; cd ../.  ; done


tar -cf todosEspectros.tar soloEspectro_A4_*

gzip todosEspectros.tar 


