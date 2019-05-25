def funcExcluir(conecta):
 
    print "\n\nDigite os dados:\n"
    ide_exclusao = raw_input("ID a Excluir: ")
    cursor = conecta.cursor()
 
    sql = "DELETE FROM pessoas WHERE id='"+ide_exclusao+"'"
    try:
            cursor.execute(sql)
        conecta.commit()
 
        except MySQLdb.Error, e:
            print "Erro: " + sql
            print e
 
    print "Exclusao feita com Sucesso."
    conecta.close()
    menu = raw_input()
    os.system("clear")
    opcaoUsuario()