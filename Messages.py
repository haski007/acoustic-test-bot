#!/usr/bin/env python
# -*- coding: utf-8 -*-


HI = "Вітаю..."

STOP = "Stopped	"



def help(message):
	start_str = "Hey, %s!\n" % message.from_user.first_name
	
	result = start_str + "I can accept these commands:\n"
	
	# Here is list of all commands of my bot
	commands = [
		"\t/start - to start communication with bot\n",
		"\t/help - to get all instructions.\n"
	]

	for command in commands:
		result += command
	return result

