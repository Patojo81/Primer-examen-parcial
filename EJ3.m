pkg load database
conn = pq_connect(setdbopts('dbname','ejercicios','host','localhost',
'port','5432','user','postgres','password','C3leste2112'))
try
  
 p=input("Precio: ");
 siv = (p/1.12) ;
 iva = p - siv;
 disp("el precio si iva es: ")
 disp(siv)
 disp("el precio del iva es: ")
 disp(iva)
catch
 disp("Ha ocurrido un error")
end_try_catch

N= pq_exec_params(conn, "insert into Ej3oc values ($1,$2,$3);",{p,siv,iva});
N= pq_exec_params(conn, 'select * from Ej3oc;')