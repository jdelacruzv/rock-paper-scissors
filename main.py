import random
import os


option_lists = ['piedra','papel', 'tijera']
game_options = {0 : 'piedra', 1 : 'papel', 2 : 'tijera'}


def title_bar():
	line = "=" * 60 
	message = "¡Bienvenido(a) al Juego!"
	print(line)
	print("{:^60}".format(message))
	print(line)
	print("El objetivo es elegir una alternativa y compararla contra el")
	print("sistema. Para terminar el programa digite salir.")


def leave_sys():
	leave = input('\n¿Desea continuar? (S / N): ').lower()
	if leave == 's':
		game()
	else:
		os._exit(0)


# El usuario gana si: 'piedra gana tijera' o 'papel gana piedra' o 'tijera gana papel'
def game():
	while True:
		user_option = input('\nElija una opción (piedra, papel o tijera): ').lower()
		system_option = random.choice(option_lists)		
		if user_option == 'salir':
			leave_sys()
		elif user_option == 'piedra' or user_option == 'papel' or user_option == 'tijera':
			print(f'Usuario: {user_option}')
			print(f'Ordenador: {system_option}')
			if user_option == system_option:
				print('¡Empate!')
				leave_sys()
			elif user_option == game_options[0] and system_option == game_options[2]:
				print('¡Ganaste!')
				leave_sys()
			elif user_option == game_options[1] and system_option == game_options[0]:
				print('¡Ganaste!')
				leave_sys()
			elif user_option == game_options[2] and system_option == game_options[1]:
				print('¡Ganaste!')
				leave_sys()
			else:
				print('¡Perdiste!')
				leave_sys()
		else:			
			print(f'Usuario: {user_option}')
			print('...entrada inválida...')


def main():
	title_bar()
	resul = game()
	print(f'{resul}\n')


main()