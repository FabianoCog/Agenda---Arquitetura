def funcAlterar(conecta):
 
    print "\n\nDigite os dados:\n"
    ide = raw_input("ID do contato a alterar: ")
    novo_nome = raw_input("Novo Nome: ")
    novo_nome = (novo_nome.upper())
    cursor = conecta.cursor()
 
    sql = "UPDATE pessoas SET nome='"+novo_nome+"' WHERE id='"+ide+"'"
    try:
            cursor.execute(sql)
        conecta.commit()
 
        except MySQLdb.Error, e:
            print "Erro: " + sql
            print e
 
    print "Alteracao feita com sucesso."
    conecta.close()
    menu = raw_input()
    os.system("clear")
    opcaoUsuario()