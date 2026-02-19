
nome = input('qual seu username? ' )  
print('Ola ' ,nome, ', seja bem vindo')
senha = input('qual sua senha? ' )   
print('sua senha é: ', senha) 
dominio = input('qual seu dominio? ')
print('seu dominio é: ', dominio)
email = nome + '@' + dominio
print('seu email é ', email) 

palavra = 'jaca'
#colocar a string como toda maiuscula
print('colocando o texto em maiuscula: ',palavra.upper())

PALAVRA = 'JACA'
#colocar a string como toda minuscula
print('colocando o texto em minuscula: ', PALAVRA.lower())

#contar caracter da string
palavra_contar = 'banana'
print('contar a letra b', palavra_contar.count('b') )
print('contar a letra a', palavra_contar.count('a') )
print('contar a letra n', palavra_contar.count('n') )

print(email)
a_c = email.count('a')
e_c = email.count('e')
i_c = email.count('i')
o_c = email.count('o')
u_c = email.count('u')
nova_senha = 'a' + str(a_c) + 'e'+ str(e_c) + 'i'+ str(i_c) + 'o'+ str(o_c) + 'u'+ str(u_c)
print(nova_senha)

