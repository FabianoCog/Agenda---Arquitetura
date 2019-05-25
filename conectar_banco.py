def conectaBanco():
 
    HOST = "localhost"
    USER = "root"
    PASSWD = "SenhaDoseuBancodeDados"
    BANCO = "Agenda"
 
    try:
        conecta = MySQLdb.connect(HOST, USER, PASSWD)
        conecta.select_db(BANCO)
 
        except MySQLdb.Error, e:
            print "Erro: O banco especificado nao foi encontrado...",e
        menu = raw_input()
        os.system("clear")
        opcaoUsuario()
 
    return conecta