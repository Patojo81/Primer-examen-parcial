pkg load database
conn = pq_connect (setdbopts ("dbname", "ejercicios", "host", "localhost", "port", "5432", "user", "postgres", "password", "C3leste2112"))
 try  
 d1=randi(6)
 d2=randi(6)
 suma = d1+d2;
 disp("La suma es: ")
 disp(suma)
 if suma == 7
   disp("Perdiste")
   resultado = ('Perdiste'); 
   pq_exec_params(conn, 'insert into ej1 values ($1,$2,$3);',{dado1,dado2,suma});
 elseif  suma == 8
   disp("Ganador")
   resultado = ('Ganador');
   pq_exec_params(conn, 'insert into ej1 values ($1,$2,$3);',{dado1,dado2,suma});
 else
   disp("Juega de nuevo")
   resultado = ('Juega de nuevo');
   pq_exec_params(conn, 'insert into ej1 values ($1,$2,$3);',{dado1,dado2,suma});
 endif
catch
disp("Algo salió mal")
end_try_catch

#N=pq_exec_params(conn, 'select * from ej1;')
#coomit