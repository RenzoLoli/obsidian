 TENER SUS PROCEDIMIENTOS PARA SUSTENTACIÓN PARCIAL
----------------------------
PRIMER PASO: Asignar vlans en switches & multicapas
-------------------------------------------------------------------
----------------------------

equipo1
upc7654321
upc1234567

---
quitar vlans

		no vlan 10
		no vlan 20
		no vlan 30
		no vlan 40
		no vlan 50
		no vlan 60
		no vlan 70
		no vlan 80
		no vlan 99

		no int vlan 10
		no int vlan 20
		no int vlan 30
		no int vlan 40
		no int vlan 50
		no int vlan 60
		no int vlan 70
		no int vlan 80
		no int vlan 99
		
1. Crear Vlans

		vlan 51
		name ADMINISTRACION
		vlan 52
		name LOGISTICA
		vlan 53
		name FINANZAS
		vlan 54
		name MARKETING
		vlan 55
		name VENTAS
		vlan 56
		name WIFI-Clientes
		vlan 57
		name WIFI-Ejecutivos
		vlan 58
		name Servidores
		vlan 99
		name NATIVE

-------------------------------------------------------------------
2. Asignar Vlans a los puertos

SW1

	INTERFACE RANGE F0/1-20
	SWITCHPORT MODE ACCESS
	SWITCHPORT ACCESS VLAN 51
	DO SHOW VLAN BRIEF
	exit

SW2

	INTERFACE RANGE F0/1-20
	SWITCHPORT MODE ACCESS
	SWITCHPORT ACCESS VLAN 52
	DO SHOW VLAN BRIEF
	exit

SW3

	INTERFACE RANGE F0/1-20
	SWITCHPORT MODE ACCESS
	SWITCHPORT ACCESS VLAN 53
	DO SHOW VLAN BRIEF
	exit

SW4

	INTERFACE RANGE F0/1-20
	SWITCHPORT MODE ACCESS
	SWITCHPORT ACCESS VLAN 54
	DO SHOW VLAN BRIEF
	exit

SW5

	INTERFACE RANGE F0/1-20
	SWITCHPORT MODE ACCESS
	SWITCHPORT ACCESS VLAN 55
	DO SHOW VLAN BRIEF
	exit

SW6  *1*

	INTERFACE F0/1
	SWITCHPORT MODE ACCESS
	SWITCHPORT ACCESS VLAN 56 
	DO SHOW VLAN BRIEF
	exit

SW6 *2*

	INTERFACE F0/2
	SWITCHPORT MODE ACCESS
	SWITCHPORT ACCESS VLAN 57
	DO SHOW VLAN BRIEF
	exit

MLS2

	INTERFACE RANGE G1/0/1-3
	SWITCHPORT MODE ACCESS
	SWITCHPORT ACCESS VLAN 58
	DO SHOW VLAN BRIEF
	exit

-------------------------------------------------------------------
3. Asignar TRUNK NATIVE

MLS1

	INTERFACE RANGE G1/0/1-8
	SWITCHPORT MODE TRUNK 
	SWITCHPORT TRUNK NATIVE VLAN 99
	DO SHOW INTERFACE TRUNK
	exit

SW1-6

	INTERFACE G0/1
	SWITCHPORT MODE TRUNK 
	SWITCHPORT TRUNK NATIVE VLAN 99
	DO SHOW INTERFACE TRUNK
	exit

MLS2

	INTERFACE G1/0/8
	SWITCHPORT MODE TRUNK 
	SWITCHPORT TRUNK NATIVE VLAN 99
	DO SHOW INTERFACE TRUNK
	exit

-------------------------------------------------------------------
4. Asignar IP a VLAN 99 en todos los SW y MLS

SW1

	INTERFACE VLAN 99
	IP ADDRESS 172.21.99.162 255.255.255.224
	NO SHUTDOWN
	EXIT
	IP DEFAULT-GATEWAY 172.21.99.161
	exit

SW2

	INTERFACE VLAN 99
	IP ADDRESS 172.21.99.163 255.255.255.224
	NO SHUTDOWN
	EXIT
	IP DEFAULT-GATEWAY 172.21.99.161
	exit

SW3

	INTERFACE VLAN 99
	IP ADDRESS 172.21.99.164 255.255.255.224
	NO SHUTDOWN
	EXIT
	IP DEFAULT-GATEWAY 172.21.99.161
	exit

SW4

	INTERFACE VLAN 99
	IP ADDRESS 172.21.99.165 255.255.255.224
	NO SHUTDOWN
	EXIT
	IP DEFAULT-GATEWAY 172.21.99.161
	exit

SW5

	INTERFACE VLAN 99
	IP ADDRESS 172.21.99.166 255.255.255.224
	NO SHUTDOWN
	EXIT
	IP DEFAULT-GATEWAY 172.21.99.161
	exit

SW6

	INTERFACE VLAN 99
	IP ADDRESS 172.21.99.167 255.255.255.224
	NO SHUTDOWN
	EXIT
	IP DEFAULT-GATEWAY 172.21.99.161
	exit

MLS1

	INTERFACE VLAN 99
	IP ADDRESS 172.21.99.170 255.255.255.224
	NO SHUTDOWN
	EXIT
	IP DEFAULT-GATEWAY 172.21.99.161
	exit

	ip routing

MLS2

	INTERFACE VLAN 99
	IP ADDRESS 172.21.99.169 255.255.255.224
	NO SHUTDOWN
	EXIT
	IP DEFAULT-GATEWAY 172.21.99.161
	exit

-------------------------------------------------------------------
5. Configurar subinterfaces en Router

		no interface g0/1.10
		no encapsulation dot1q 10
		shutdown
		exit
		no interface g0/1.20
		no encapsulation dot1q 20
		shutdown
		exit
		no interface g0/1.30
		no encapsulation dot1q 30
		shutdown
		exit
		no interface g0/1.40
		no encapsulation dot1q 40
		shutdown
		exit
		no interface g0/1.50
		no encapsulation dot1q 50
		shutdown
		exit
		no interface g0/1.60
		no encapsulation dot1q 60
		shutdown
		exit
		no interface g0/1.70
		no encapsulation dot1q 70
		shutdown
		exit
		no interface g0/1.80
		no encapsulation dot1q 80
		shutdown
		exit
		no interface g0/1.99
		no encapsulation dot1q 99
		shutdown
		exit

		int g0/0
		no ip address
		interface g0/1.51
		encapsulation dot1q 51
		ip address 172.21.48.1 255.255.255.128
		interface g0/1.52
		encapsulation dot1q 52
		ip address 172.21.48.129 255.255.255.224
		interface g0/1.53
		encapsulation dot1q 53
		ip address 172.21.48.161 255.255.255.224
		interface g0/1.54
		encapsulation dot1q 54
		ip address 172.21.48.193 255.255.255.224
		interface g0/1.55
		encapsulation dot1q 55
		ip address 172.21.48.225 255.255.255.224
		interface g0/1.56
		encapsulation dot1q 56
		ip address 172.21.49.1 255.255.255.240
		interface g0/1.57
		encapsulation dot1q 57
		ip address 172.21.49.17 255.255.255.240
		interface g0/1.58
		encapsulation dot1q 58
		ip address 172.21.49.49 255.255.255.248
		interface g0/1.99
		encapsulation dot1q 99 native
		ip address 172.21.99.161 255.255.255.224
		exit
		interface g0/0
		no shutdown

-------------------------------------------------------------------
6. Asignar gateways en multicapa

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

-----------------------------------------------------------------
7. Configurar DHCP en el DNS

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

//Aún no agrego esto
int vlan 51
ip helper-ADDRESS 172.21.64.210
int vlan 52
ip helper-ADDRESS 172.21.64.210
int vlan 53
ip helper-ADDRESS 172.21.64.210
int vlan 54
ip helper-ADDRESS 172.21.64.210
int vlan 55
ip helper-ADDRESS 172.21.64.210
int vlan 56
ip helper-ADDRESS 172.21.64.210
int vlan 57
ip helper-ADDRESS 172.21.64.210
int vlan 58
ip helper-ADDRESS 172.21.64.210
