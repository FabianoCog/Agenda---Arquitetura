def opcaoUsuario():
 
    os.system("clear");
    print "==================================="
    print "======= Agenda de Contatos ========"
    print "==================================="
    opcao = raw_input("Escolha a opcao desejada\n\n[1] - Cadastrar\n[2] - Consultar\n[3] - Alterar\n[4] - Excluir\n[5] - Mostrar Todos\n[6] - Sair")
 
    try:
        opcao = int(opcao)
        if opcao<1 or opcao>6:
            os.system("clear");
            print "OPCAO INVALIDA: Verifique o valor digitado"
            time.sleep(2)
            opcaoUsuario()
    except:
        os.system("clear");
        print "OPCAO INVALIDA: Verifique o valor digitado"
        time.sleep(2)
        opcaoUsuario()
 
    if opcao == 1:
        conecta = conectaBanco()
        funcCadastrar(conecta)
 
    elif opcao == 2:
        conecta = conectaBanco()
        funcConsultar(conecta)
 
    elif opcao == 3:
        conecta = conectaBanco()
        funcAlterar(conecta)
 
    elif opcao == 4:
        conecta = conectaBanco()
        funcExcluir(conecta)
 
    elif opcao == 5:
        conecta = conectaBanco()
        funcMostrarTodos(conecta)
 
    elif opcao == 6:
        sys.exit()