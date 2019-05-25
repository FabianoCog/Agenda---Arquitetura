def funcConsultar(conecta):
 
    name = str(raw_input("\nDigite o Nome a Pesquisar: "))
    name = (name.upper())
    cursor = conecta.cursor()
    sql="SELECT * FROM pessoas WHERE nome='"+name+"'"
    resultados = 0
 
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
            print"\n----------------------------\n"
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