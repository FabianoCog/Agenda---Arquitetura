def funcMostrarTodos(conecta):
 
    resultados = 0
    cursor = conecta.cursor()
    sql="SELECT * FROM pessoas;"
 
    try:
            cursor.execute(sql)
        resultado = cursor.fetchall()
 
        for dados in resultado:
            ide = dados[0]
                    nome = dados[1]
            endereco = dados[2]
            email = dados[3]
            telefone = dados[4]
            resultados= int(resultados)
            resultados = resultados + 1
            print"----------------------------------"
            print " ID: %s\n Nome: %s\n Endereco: %s\n Email: %s\n Telefone: %s"%(ide, nome, endereco, email, telefone)
        conecta.commit()
 
        except MySQLdb.Error, e:
            print "Erro: " + sql
            print e
 
    print "\n\nForam encontrados %d resultados"%resultados
    conecta.close()
    menu = raw_input()
    os.system("clear")
    opcaoUsuario()