pkg load database
conn = pq_connect (setdbopts ("dbname", "ejercicios", "host", "localhost", "port", "5432", "user", "postgres", "password", "C3leste2112"))

try
 nota1=input("primera nota: ");
 nota2=input("segunda nota: ");
 nota3=input("tercera nota: ");
 nota4=input("cuarta nota: ");
 nota5=input("quinta nota: ");
 arreglo=([nota1 nota2 nota3 nota4 nota5]); 
 media=mean(arreglo); 
 mediana=median(arreglo); 
 moda=mode(arreglo); 
 maximo=max(arreglo); 
 minimo=min(arreglo); 
 rango=maximo-minimo;
 desvest=std(arreglo,1)
 varianza=var(arreglo,1)
 fprintf('La media es: %d\n',media)
 fprintf('La mediana es: %d\n',mediana)
 fprintf('La moda es: %d\n',moda)
 fprintf('El rango es: %d\n',rango)
 fprintf('La desviación estándar es: %d\n',desvest)
 fprintf('La varianza es: %d\n',varianza)

catch
 disp("Algo salió mal")
end_try_catch

pq_exec_params(conn, 'insert into ej3 values ($1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12);',{nota1,nota2,nota3,nota4,nota5,media,mediana,moda,maximo,minimo,desvest,varianza});
N=pq_exec_params(conn, 'select * from ej3;')