a = '^'
b = ' '
n = 0

isaias_9_6 = '''

    Porque um menino nos nasceu, um filho se nos deu.
    O governo está sobre os seus ombros, e o seu nome será:
    "Maravilhoso Conselheiro", "Deus Forte", 
    "Pai da Eternidade", "Príncipe da Paz".

    Isaías 9:6

    '''

print(f'\n{isaias_9_6}')

while n < 10:
	if n == 0:
		print('\n', (21*' '), f'Feliz Natal!\n\n', (26*' '), '*')
	else:
		print(18*' ', ((b * (10-n)) + ((n + (n-1))) * a))

	n +=1

print((27*' '),f'|\n',(26*' '),'|\n\n')

