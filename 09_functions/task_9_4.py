#!/usr/bin/env python3

ignore = ['duplex', 'alias', 'Current configuration']
def ignore_command(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
    '''
    return any(word in command for word in ignore)


def convert_config_to_dict(config_filename,):
	with open(config_filename, 'r') as source:
		result = {}
		for lines in source:
			if ignore_command(lines, ignore):
				continue
			elif lines.startswith('!') or lines.startswith('\n'):
				continue
			elif lines[0] != ' ':
				keys = lines.strip()
				result[keys] = []
			elif lines.startswith(' ') and lines[1] != ' ':
				result[keys].append(lines.strip())
	print(result)
	return(result)


convert_config_to_dict('config_sw1.txt')
