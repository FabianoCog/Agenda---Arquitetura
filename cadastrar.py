def funcCadastrar(conecta):
 
    print "\n\nDigite os dados:\n"
    name = str(raw_input("Nome: "))
    name = (name.upper())
    address = str(raw_input("Endereco: "))
    address = (address.upper())
    mail = str(raw_input("Email: "))
    mail = (mail.upper())
    fone = str(raw_input("Telefone: "))
    fone = (fone.upper())
    cursor = conecta.cursor()
 
    sql="INSERT INTO pessoas (nome,endereco,email,telefone) VALUES ('"+name+"','"+address+"','"+mail+"','"+fone+"')"
 
    try:
            cursor.execute(sql)
        conecta.commit()
 
        except MySQLdb.Error, e:
            print "Erro: " + sql
            print e
 
    print "Dados gravados com sucesso."
    conecta.close()
    menu = raw_input()
    os.system("clear")
    opcaoUsuario()