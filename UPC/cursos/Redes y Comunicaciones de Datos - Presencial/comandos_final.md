 TENER SUS PROCEDIMIENTOS PARA SUSTENTACIÓN PARCIAL
----------------------------
-------------------------------------------------------------------
----------------------------

	user: equipo1
	pass1: upc7654321
	pass2: upc1234567

---
#SW1

	en
	conf t
	vlan 51
	name ADMINISTRACION
	exit
	int vlan 51
	exit
	vlan 99
	name NATIVE
	exit
	int vlan 99
	exit
	
	INTERFACE RANGE F0/1-20
	SWITCHPORT MODE ACCESS
	SWITCHPORT ACCESS VLAN 51
	DO SHOW VLAN BRIEF
	exit
	
	INTERFACE G0/1
	SWITCHPORT MODE TRUNK 
	SWITCHPORT TRUNK NATIVE VLAN 99
	DO SHOW INTERFACE TRUNK
	exit
	
	INTERFACE VLAN 99
	IP ADDRESS 172.21.99.162 255.255.255.224
	NO SHUTDOWN
	EXIT
	IP DEFAULT-GATEWAY 172.21.99.161
	exit

#SW2

	en
	conf t
	
	vlan 52
	name LOGISTICA
	exit
	int vlan 52
	exit
	vlan 99
	name NATIVE
	exit
	int vlan 99
	exit
	
	INTERFACE RANGE F0/1-20
	SWITCHPORT MODE ACCESS
	SWITCHPORT ACCESS VLAN 52
	DO SHOW VLAN BRIEF
	exit
	
	INTERFACE G0/1
	SWITCHPORT MODE TRUNK 
	SWITCHPORT TRUNK NATIVE VLAN 99
	DO SHOW INTERFACE TRUNK
	exit
	
	INTERFACE VLAN 99
	IP ADDRESS 172.21.99.163 255.255.255.224
	NO SHUTDOWN
	EXIT
	IP DEFAULT-GATEWAY 172.21.99.161
	exit

#SW3

	en
	conf t
	
	vlan 53
	name MARKETING
	exit
	int vlan 53
	exit
	vlan 99
	name NATIVE
	exit
	int vlan 99
	exit
	
	INTERFACE RANGE F0/1-20
	SWITCHPORT MODE ACCESS
	SWITCHPORT ACCESS VLAN 53
	DO SHOW VLAN BRIEF
	exit
	
	INTERFACE G0/1
	SWITCHPORT MODE TRUNK 
	SWITCHPORT TRUNK NATIVE VLAN 99
	DO SHOW INTERFACE TRUNK
	exit
	
	INTERFACE VLAN 99
	IP ADDRESS 172.21.99.164 255.255.255.224
	NO SHUTDOWN
	EXIT
	IP DEFAULT-GATEWAY 172.21.99.161
	exit

#SW4

	en
	conf t
	
	vlan 54
	name VENTAS
	exit
	int vlan 54
	exit
	vlan 99
	name NATIVE
	exit
	int vlan 99
	exit
	
	INTERFACE RANGE F0/1-20
	SWITCHPORT MODE ACCESS
	SWITCHPORT ACCESS VLAN 54
	DO SHOW VLAN BRIEF
	exit
	
	INTERFACE G0/1
	SWITCHPORT MODE TRUNK 
	SWITCHPORT TRUNK NATIVE VLAN 99
	DO SHOW INTERFACE TRUNK
	exit
	
	INTERFACE VLAN 99
	IP ADDRESS 172.21.99.165 255.255.255.224
	NO SHUTDOWN
	EXIT
	IP DEFAULT-GATEWAY 172.21.99.161
	exit

#SW5

	en
	conf t
	
	vlan 55
	name FINANZAS
	exit
	int vlan 55
	exit
	vlan 99
	name NATIVE
	exit
	int vlan 99
	exit
	
	INTERFACE RANGE F0/1-20
	SWITCHPORT MODE ACCESS
	SWITCHPORT ACCESS VLAN 55
	DO SHOW VLAN BRIEF
	exit
	
	INTERFACE G0/1
	SWITCHPORT MODE TRUNK 
	SWITCHPORT TRUNK NATIVE VLAN 99
	DO SHOW INTERFACE TRUNK
	exit
	
	INTERFACE VLAN 99
	IP ADDRESS 172.21.99.166 255.255.255.224
	NO SHUTDOWN
	EXIT
	IP DEFAULT-GATEWAY 172.21.99.161
	exit

#SW6

	en
	conf t
	
	vlan 56
	name WIFI-Clientes
	exit
	int vlan 56
	exit
	vlan 57
	name WIFI-Ejecutivos
	exit
	int vlan 57
	exit
	vlan 99
	name NATIVE
	exit
	int vlan 99
	exit
	
	INTERFACE F0/1
	SWITCHPORT MODE ACCESS
	SWITCHPORT ACCESS VLAN 56 
	DO SHOW VLAN BRIEF
	exit
	
	INTERFACE F0/2
	SWITCHPORT MODE ACCESS
	SWITCHPORT ACCESS VLAN 57
	DO SHOW VLAN BRIEF
	exit
	
	INTERFACE G0/1
	SWITCHPORT MODE TRUNK 
	SWITCHPORT TRUNK NATIVE VLAN 99
	DO SHOW INTERFACE TRUNK
	exit
	
	INTERFACE VLAN 99
	IP ADDRESS 172.21.99.167 255.255.255.224
	NO SHUTDOWN
	EXIT
	IP DEFAULT-GATEWAY 172.21.99.161
	exit

#MLS2

	en 
	conf t 
	
	vlan 58
	name SERVIDORES
	exit
	int vlan 58
	exit
	vlan 99
	name NATIVE
	exit
	int vlan 99
	exit
	
	INTERFACE RANGE G1/0/1-3
	SWITCHPORT MODE ACCESS
	SWITCHPORT ACCESS VLAN 58
	DO SHOW VLAN BRIEF
	exit
	
	INTERFACE G1/0/24
	SWITCHPORT MODE TRUNK 
	SWITCHPORT TRUNK NATIVE VLAN 99
	DO SHOW INTERFACE TRUNK
	exit
	
	INTERFACE VLAN 99
	IP ADDRESS 172.21.99.169 255.255.255.224
	NO SHUTDOWN
	EXIT
	IP DEFAULT-GATEWAY 172.21.99.161
	exit

#MLS1

	en
	conf t
	
	vlan 51
	name ADMINISTRACION
	vlan 52
	name LOGISTICA
	vlan 53
	name MARKETING
	vlan 54
	name VENTAS
	vlan 55
	name FINANZAS
	vlan 56
	name WIFI-Clientes
	vlan 57
	name WIFI-Ejecutivos
	vlan 58
	name SERVIDORES
	vlan 99
	name NATIVE
	exit
	
	INT VLAN 51
	IP ADDRESS 172.21.48.1 255.255.255.128
	INT VLAN 52
	IP ADDRESS 172.21.48.129 255.255.255.224
	INT VLAN 53
	IP ADDRESS 172.21.48.161 255.255.255.224
	INT VLAN 54
	IP ADDRESS 172.21.48.193 255.255.255.224
	INT VLAN 55
	IP ADDRESS 172.21.48.225 255.255.255.224
	INT VLAN 56
	IP ADDRESS 172.21.49.1 255.255.255.240
	INT VLAN 57
	IP ADDRESS 172.21.49.17 255.255.255.240
	INT VLAN 58
	IP ADDRESS 172.21.49.49 255.255.255.248
	INT VLAN 99
	IP ADDRESS 172.21.99.161 255.255.255.224
	exit
	
	INTERFACE RANGE G1/0/1-8
	SWITCHPORT MODE TRUNK 
	SWITCHPORT TRUNK NATIVE VLAN 99
	exit
	#### DO SHOW INTERFACE TRUNK
	
	INTERFACE VLAN 99
	IP ADDRESS 172.21.99.170 255.255.255.224
	NO SHUTDOWN
	exit
	IP DEFAULT-GATEWAY 172.21.99.161
	
	INTERFACE RANGE G1/0/24
	SWITCHPORT MODE TRUNK 
	SWITCHPORT TRUNK NATIVE VLAN 99
	exit
	#### DO SHOW INTERFACE TRUNK
	
	ip routing

#R1

	en
	conf t
	
	int g0/0
	no ip address
	interface g0/0.51
	encapsulation dot1q 51
	ip address 172.21.48.1 255.255.255.128
	no shutdown
	interface g0/0.52
	encapsulation dot1q 52
	ip address 172.21.48.129 255.255.255.224
	interface g0/0.53
	encapsulation dot1q 53
	ip address 172.21.48.161 255.255.255.224
	interface g0/0.54
	encapsulation dot1q 54
	ip address 172.21.48.193 255.255.255.224
	interface g0/0.55
	encapsulation dot1q 55
	ip address 172.21.48.225 255.255.255.224
	interface g0/0.56
	encapsulation dot1q 56
	ip address 172.21.49.1 255.255.255.240
	interface g0/0.57
	encapsulation dot1q 57
	ip address 172.21.49.17 255.255.255.240
	interface g0/0.58
	encapsulation dot1q 58
	ip address 172.21.49.49 255.255.255.248
	interface g0/0.99
	encapsulation dot1q 99 native
	ip address 172.21.99.161 255.255.255.224
	exit
	interface g0/0
	no shutdown

#APCLI

	SSID: APWIFICLIAR
	WEP:  0123456789

#APEJE

	SSID: APWIFIEJEAR
	WEP:  0123456789

#SVDHCPAR

	pool: POOLVln51
	default-gateway: 172.21.48.1
	dns-server: 172.21.49.50
	mask: 255.255.255.128
	network: 172.21.48.0
	ip-start: 172.21.48.2
	max-hosts: 30
	
	pool: POOLVln52
	default-gateway: 172.21.48.129
	dns-server: 172.21.49.50
	mask: 255.255.255.224
	network: 172.21.48.128
	ip-start: 172.21.48.130
	max-hosts: 30
	
	pool: POOLVln53
	default-gateway: 172.21.48.161
	dns-server: 172.21.49.50
	mask: 255.255.255.224
	network: 172.21.48.160
	ip-start: 172.21.48.162
	max-hosts: 30
	
	pool: POOLVln54
	default-gateway: 172.21.48.193
	dns-server: 172.21.49.50
	mask: 255.255.255.224
	network: 172.21.48.192
	ip-start: 172.21.48.194
	max-hosts: 30
	
	pool: POOLVln55
	default-gateway: 172.21.48.225
	dns-server: 172.21.49.50
	mask: 255.255.255.224
	network: 172.21.48.224
	ip-start: 172.21.48.226
	max-hosts: 30
	
	pool: POOLVln56
	default-gateway: 172.21.49.1
	dns-server: 172.21.49.50
	mask: 255.255.255.224
	network: 172.21.49.0
	ip-start: 172.21.49.2
	max-hosts: 30
	
	pool: POOLVln57
	default-gateway: 172.21.49.17
	dns-server: 172.21.49.50
	mask: 255.255.255.240
	network: 172.21.49.16
	ip-start: 172.21.49.18
	max-hosts: 30

#router #mls1 

	int vlan 51
	ip helper-address 172.21.49.53
	int vlan 52
	ip helper-address 172.21.49.53
	int vlan 53
	ip helper-address 172.21.49.53
	int vlan 54
	ip helper-address 172.21.49.53
	int vlan 55
	ip helper-address 172.21.49.53
	int vlan 56
	ip helper-address 172.21.49.53
	int vlan 57
	ip helper-address 172.21.49.53
	int vlan 58
	ip helper-address 172.21.49.53

#router #switches

	en
	conf t
	service password-encryption
	security password min-length 10
	enable secret upc1234567
	no ip domain-lookup
	username equipo1 secret upc7654321
	login block-for 180 attempts 4 within 120
	line console 0
	login local
	exec-timeout 6
	loggin synchronous
	exit
	line vty 0 15
	password upc1234567
	transport input telnet
	login local
	exec-timeout 6
	loggin synchronous
	banner motd $ *** SOLO PERSONAL AUTORIZADO *** $
	exit
	copy run start

#router 

	router ospf 10
	router-id 6.6.6.6
	network 172.21.99.32 0.0.0.31 area 0
	network 172.21.99.160 0.0.0.31 area 0
	exit

#roter #router-lima

	interface serial 0/1/0
	ip ospf 10 area 0

#MLS1 

	router ospf 10
	network 172.21.48.0 0.0.0.127 area 0
	network 172.21.48.128 0.0.0.31 area 0
	network 172.21.48.160 0.0.0.31 area 0
	network 172.21.48.192 0.0.0.31 area 0
	network 172.21.48.224 0.0.0.31 area 0
	network 172.21.49.0 0.0.0.15 area 0
	network 172.21.49.16 0.0.0.15 area 0
	network 172.21.49.48 0.0.0.7 area 0
	network 172.21.99.160 0.0.0.31 area 0
	passive-interface GigabitEthernet1/0/1
	passive-interface GigabitEthernet1/0/2
	passive-interface GigabitEthernet1/0/3
	passive-interface GigabitEthernet1/0/4
	passive-interface GigabitEthernet1/0/5
	passive-interface GigabitEthernet1/0/6
	passive-interface GigabitEthernet1/0/8
	end


-----------------------------------------------------------------
#router 
### -> Esto o un server dhcp

	ip dhcp excluded-address 172.21.48.1 172.21.48.127
	ip dhcp excluded-address 172.21.48.129 172.21.48.159
	ip dhcp excluded-address 172.21.48.161 172.21.48.191
	ip dhcp excluded-address 172.21.48.193 172.21.48.223
	ip dhcp excluded-address 172.21.48.225 172.21.48.255
	ip dhcp excluded-address 172.21.49.1 172.21.49.15
	ip dhcp excluded-address 172.21.49.17 172.21.49.31
	ip dhcp excluded-address 172.21.49.49 172.21.49.55

	ip dhcp pool POOLVln51
	network 172.21.48.0 255.255.255.128
	default-router 172.21.48.1
	dns-server 172.21.49.50
	exit

	ip dhcp pool POOLVln52
	network 172.21.48.128 255.255.255.224
	default-router 172.21.48.129
	dns-server 172.21.49.50
	exit
	
	ip dhcp pool POOLVln53
	network 172.21.48.160 255.255.255.224
	default-router 172.21.48.161
	dns-server 172.21.49.50
	exit

	ip dhcp pool POOLVln54
	network 172.21.48.192 255.255.255.224
	default-router 172.21.48.193
	dns-server 172.21.49.50
	exit

	ip dhcp pool POOLVln55
	network 172.21.48.224 255.255.255.224
	default-router 172.21.48.225
	dns-server 172.21.49.50
	exit

	ip dhcp pool POOLVln56
	network 172.21.49.0 255.255.255.240
	default-router 172.21.49.1
	dns-server 172.21.49.50
	exit

	ip dhcp pool POOLVln57
	network 172.21.49.16 255.255.255.240
	default-router 172.21.49.17
	dns-server 172.21.49.50
	exit

	ip dhcp pool POOLVln58
	network 172.21.49.48 255.255.255.248
	default-router 172.21.49.49
	dns-server 172.21.49.50
	exit


	en
	conf t
	do copy run start
	end