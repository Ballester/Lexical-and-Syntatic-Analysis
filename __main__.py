from lexico import Lexico

lex = Lexico("inputs.in")

#Insere estados
lex.insereEstado("q0")
lex.insereEstado("chaves", final=True)
lex.insereEstado("id", final=True)
lex.insereEstado("op", final=True)

#Insere transicoes
lex.insereTrans("q0", "id", "a-z")
lex.insereTrans("id", "id", "a-z")
lex.insereTrans("id", "id", "0-9")

#Operacoes
lex.insereTrans("q0", "op", "+")
lex.insereTrans("q0", "op", "-")
lex.insereTrans("q0", "op", "*")

lex.insereTrans("q0", "chaves", "{")
lex.insereTrans("q0", "chaves", "}")

lex.insereTrans("q0", "q0", "i")
lex.insereTrans("q2", "q3", "-")
lex.insereTrans("q3", "q1", "-")

lex.insereReservada("for")
lex.insereReservada("while")
lex.insereReservada("if")


#Seta estado inicial
lex.setInicial("q0")

#Insere delimitadores
lex.insereDelimitador(" ")
lex.insereDelimitador("\n")

#Le do arquivo
var = lex.scanner()
print var
erro = False
while (var != 'EOF' and not erro):
	if len(var) > 1:
		if var[0] == 'ERRO':
			print var
			erro = True
		else:
			var = lex.scanner()
			print var

	
		
'''
lex.printEstados()
lex.printFinais()
lex.printTrans()
'''