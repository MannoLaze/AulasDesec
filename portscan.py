#!/usr/bin/python
# This Python file uses the following encoding: utf-8
#PortScan basico em python 
#Exercício2 Modulo 4 -  Desec Security - Aluna Alley Pereira



import socket,sys

for porta in range(1,65535):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	if s.connect_ex((sys.argv[1], porta)) == 0:
		print "Porta",porta,"[ABERTA]"
		s.close()

