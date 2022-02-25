pkg load database
conn = pq_connect (setdbopts ("dbname", "ejercicios", "host", "localhost", "port", "5432", "user", "postgres", "password", "C3leste2112"))

try
num=input('número: ');
oper=1:n;
total = 0;
if nnz(rem(num,oper)==0)==2
    disp('Número primo');
    total = ('Numero primo');
else
    disp('Número compuesto');
    total = ('Numero Compuesto')
end

catch
 disp('algo salio mal');
 total = ('algo salio mal');
end_try_catch


N=pq_exec_params(conn, "insert into ej4 values ($1);",{num});
N=pq_exec_params(conn, 'select * from ej4;') %ver datos en la tabla