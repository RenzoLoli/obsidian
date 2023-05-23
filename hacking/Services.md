
## #FTP
	
	name: file transfer protocol
	use-for: protocolo para compartir archivos, impresoras, etc entre nodos
					de una red
	port: 21
	service-name-reference: ftp
	useful-applications:
		- ftp
	
## #SMB

	name: server message block
	use-for: protocolo para compartir archivos, impresoras, etc entre nodos
					de una red
	port: 445
	service-name-reference: windows-ds 	
	useful-applications:
		- smbclient
	
## #telnet

	name: teletype network
	use-for: protocolo para acceder a otras maquinas remotamente
	port: 22
	service-name-reference: telnet
	useful-applications:
		- telnet
	
## #redis

	name: remote dictionary server
	use-for: motor de base de datos en memoria basado en almacenamiento de tablas de hashes
	port: 6379
	service-name-reference: redis
	useful-applications:
		- redis-cli
	
## #http

	name: Hypertext Transfer Protocol
	use-for: protocolo de capa de aplicacion para la transmision de documentos de hipermedia
		port: 80,8080,8000
	service-name-reference: http,apache
	useful-applications:
		- firefox,chrome,safari,edge

## #https

	name: Hypertext Transfer Protocol Secure
	use-for: protocolo de capa de aplicacion para la transmision de documentos de hipermedia 
					segura
	port: 443
	service-name-reference: https,apache
	useful-applications:
		- firefox,chrome,safari,edge

## #mysql

	name: Structured Query Language
	use-for: es un sistema de gestion de bases de datos relacionales
	port: 3306
	service-name-reference: mysql
	useful-applications:
		- mysql