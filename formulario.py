'''
programa para entrada de dados de alunos de universidade para geracao de e-mail e senha automatico
'''
nome = input('entre com o seu nome: ' )
sobrenome = input('entre com seu sobrenome: ' )
dia_nascimento = input('dia de nascimento: ' )
mes_nascimento = input('mes de nascimento: ' )
ano_nascimento = input('ano de nascimento: ' )
universidade = input('qual sua universidade: ' )

e_mail = nome.lower() + '.' + sobrenome.lower() + '@' + universidade + '.br'
senha = str(e_mail.count('a')) + 'e' + str(e_mail.count('e')) + 'i' + str(e_mail.count('i')) + 'o' + str(e_mail.count('o')) + 'u' + str(e_mail.count('u'))

print('o seu e-mail é: {}' .format(e_mail))
print('a sua senha é: {}' .format(senha))

print('A sua senha e e-mail são: {}:{}' .format(senha,e_mail))

