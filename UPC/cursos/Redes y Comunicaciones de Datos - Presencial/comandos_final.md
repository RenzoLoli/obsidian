 TENER SUS PROCEDIMIENTOS PARA SUSTENTACIÓN PARCIAL
----------------------------
PRIMER PASO: Asignar vlans en switches & multicapas
-------------------------------------------------------------------
1. Crear Vlans

		vlan 10
		name ADMINISTRACION
		vlan 20
		name LOGISTICA
		vlan 30
		name MARKETING
		vlan 40
		name VENTAS
		vlan 50
		name FINANZAS
		vlan 60
		name WIFI-Clientes
		vlan 70
		name WIFI-Ejecutivos
		vlan 80
		name Servidores
		vlan 99
		name NATIVE

-------------------------------------------------------------------
2. Asignar Vlans a los puertos

SW1

	INTERFACE RANGE F0/1-20
	SWITCHPORT MODE ACCESS
	SWITCHPORT ACCESS VLAN 10
	DO SHOW VLAN BRIEF
	exit

SW2

	INTERFACE RANGE F0/1-20
	SWITCHPORT MODE ACCESS
	SWITCHPORT ACCESS VLAN 20
	DO SHOW VLAN BRIEF
	exit

SW3

	INTERFACE RANGE F0/1-20
	SWITCHPORT MODE ACCESS
	SWITCHPORT ACCESS VLAN 30
	DO SHOW VLAN BRIEF
	exit

SW4

	INTERFACE RANGE F0/1-20
	SWITCHPORT MODE ACCESS
	SWITCHPORT ACCESS VLAN 40
	DO SHOW VLAN BRIEF
	exit

SW5

	INTERFACE RANGE F0/1-20
	SWITCHPORT MODE ACCESS
	SWITCHPORT ACCESS VLAN 50
	DO SHOW VLAN BRIEF
	exit

SW6  *1*

	INTERFACE F0/1
	SWITCHPORT MODE ACCESS
	SWITCHPORT ACCESS VLAN 60 
	DO SHOW VLAN BRIEF
	exit

SW6 *2*

	INTERFACE F0/2
	SWITCHPORT MODE ACCESS
	SWITCHPORT ACCESS VLAN 70
	DO SHOW VLAN BRIEF
	exit

MLS2

	INTERFACE RANGE G1/0/1-3
	SWITCHPORT MODE ACCESS
	SWITCHPORT ACCESS VLAN 80
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
	IP ADDRESS 172.21.49.34 255.255.255.240
	NO SHUTDOWN
	EXIT
	IP DEFAULT-GATEWAY 172.21.49.33
	exit

SW2

	INTERFACE VLAN 99
	IP ADDRESS 172.21.49.35 255.255.255.240
	NO SHUTDOWN
	EXIT
	IP DEFAULT-GATEWAY 172.21.49.33
	exit

SW3

	INTERFACE VLAN 99
	IP ADDRESS 172.21.49.36 255.255.255.240
	NO SHUTDOWN
	EXIT
	IP DEFAULT-GATEWAY 172.21.49.33
	exit

SW4

	INTERFACE VLAN 99
	IP ADDRESS 172.21.49.37 255.255.255.240
	NO SHUTDOWN
	EXIT
	IP DEFAULT-GATEWAY 172.21.49.33
	exit

SW5

	INTERFACE VLAN 99
	IP ADDRESS 172.21.49.38 255.255.255.240
	NO SHUTDOWN
	EXIT
	IP DEFAULT-GATEWAY 172.21.49.33
	exit

SW6

	INTERFACE VLAN 99
	IP ADDRESS 172.21.49.39 255.255.255.240
	NO SHUTDOWN
	EXIT
	IP DEFAULT-GATEWAY 172.21.49.33
	exit

MLS1

	INTERFACE VLAN 99
	IP ADDRESS 172.21.49.40 255.255.255.240
	NO SHUTDOWN
	EXIT
	IP DEFAULT-GATEWAY 172.21.49.33
	exit

MLS2

	INTERFACE VLAN 99
	IP ADDRESS 172.21.49.41 255.255.255.240
	NO SHUTDOWN
	EXIT
	IP DEFAULT-GATEWAY 172.21.49.33
	exit

-------------------------------------------------------------------
5. Configurar subinterfaces en Router

		int g0/0
		no ip address
		interface g0/1.10
		encapsulation dot1q 10
		ip address 172.21.48.1 255.255.255.128
		interface g0/1.20
		encapsulation dot1q 20
		ip address 172.21.48.129 255.255.255.224
		interface g0/1.30
		encapsulation dot1q 30
		ip address 172.21.48.161 255.255.255.224
		interface g0/1.40
		encapsulation dot1q 40
		ip address 172.21.48.193 255.255.255.224
		interface g0/1.50
		encapsulation dot1q 50
		ip address 172.21.48.225 255.255.255.224
		interface g0/1.60
		encapsulation dot1q 60
		ip address 172.21.49.1 255.255.255.240
		interface g0/1.70
		encapsulation dot1q 70
		ip address 172.21.49.17 255.255.255.240
		interface g0/1.80
		encapsulation dot1q 80
		ip address 172.21.49.49 255.255.255.248
		interface g0/1.99
		encapsulation dot1q 99 native
		ip address 172.21.49.33 255.255.255.240
		exit
		interface g0/0
		no shutdown

-------------------------------------------------------------------
6. Asignar gateways en multicapa

		INT VLAN 10
		IP ADDRESS 172.21.48.1 255.255.255.128
		INT VLAN 20
		IP ADDRESS 172.21.48.129 255.255.255.224
		INT VLAN 30
		IP ADDRESS 172.21.48.161 255.255.255.224
		INT VLAN 40
		IP ADDRESS 172.21.48.193 255.255.255.224
		INT VLAN 50
		IP ADDRESS 172.21.48.225 255.255.255.224
		INT VLAN 60
		IP ADDRESS 172.21.49.1 255.255.255.240
		INT VLAN 70
		IP ADDRESS 172.21.49.17 255.255.255.240
		INT VLAN 80
		IP ADDRESS 172.21.49.49 255.255.255.248
		INT VLAN 99
		IP ADDRESS 172.21.49.33 255.255.255.240
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

		ip dhcp pool POOLVln10
		network 172.21.48.0 255.255.255.128
		default-router 172.21.48.1
		dns-server 172.21.49.50
		exit

		ip dhcp pool POOLVln20
		network 172.21.48.128 255.255.255.224
		default-router 172.21.48.129
		dns-server 172.21.49.50
		exit

		ip dhcp pool POOLVln30
		network 172.21.48.160 255.255.255.224
		default-router 172.21.48.161
		dns-server 172.21.49.50
		exit

		ip dhcp pool POOLVln40
		network 172.21.48.192 255.255.255.224
		default-router 172.21.48.193
		dns-server 172.21.49.50
		exit

		ip dhcp pool POOLVln50
		network 172.21.48.224 255.255.255.224
		default-router 172.21.48.225
		dns-server 172.21.49.50
		exit

		ip dhcp pool POOLVln60
		network 172.21.49.0 255.255.255.240
		default-router 172.21.49.1
		dns-server 172.21.49.50
		exit

		ip dhcp pool POOLVln70
		network 172.21.49.16 255.255.255.240
		default-router 172.21.49.17
		dns-server 172.21.49.50
		exit

		ip dhcp pool POOLVln80
		network 172.21.49.48 255.255.255.248
		default-router 172.21.49.49
		dns-server 172.21.49.50
		exit

//Aún no agrego esto
int vlan 10
ip helper-ADDRESS 172.21.64.210
int vlan 20
ip helper-ADDRESS 172.21.64.210
int vlan 30
ip helper-ADDRESS 172.21.64.210
int vlan 40
ip helper-ADDRESS 172.21.64.210
int vlan 50
ip helper-ADDRESS 172.21.64.210
int vlan 60
ip helper-ADDRESS 172.21.64.210
int vlan 70
ip helper-ADDRESS 172.21.64.210
int vlan 80
ip helper-ADDRESS 172.21.64.210
