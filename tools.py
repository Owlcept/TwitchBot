from config import BOT_PREFIX as prefix

def list_commands(listcmd):

	msgs = list()
	msg = str()

	for cmd in listcmd:
		if (len(msg) + len(cmd) + 2) < 500:
			msg = msg + f'{prefix}{cmd}, '
		else:
			msgs.append(msg)
			msg = ''

	if msg:
		msg = msg[:]
		msgs.append(msg)

	return msgs