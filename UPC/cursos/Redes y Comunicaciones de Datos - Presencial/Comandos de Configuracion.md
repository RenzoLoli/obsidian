SW1
-----

	EN
	CONF T
	INTERFACE VLAN 1
	IP ADDRESS 10.10.10.2 255.255.255.0
	NO SHUTDOWN
	EXIT
	IP DEFAULT-GATEWAY 10.10.10.1

--------------

SW2
-----
	EN
	CONF T
	INTERFACE VLAN 1
	IP ADDRESS 10.10.20.2 255.255.255.0
	NO SHUTDOWN
	EXIT
	IP DEFAULT-GATEWAY 10.10.20.1

SEGURIDAD BÁSICA ROUTER
--------------
	hostname RTA
	enable secret Ciscoenpa55
	line console 0
	password Ciscolinepa55
	login
	exit
	line vty 0 15
	password Ciscolinepa55
	login
	exit
	banner motd % *** SOLO PERSONAL AUTORIZADO ACCEDERÁ AL DISPOSITIVO *** %
	END
	copy run start

SEGURIDAD BÁSICA DE LOS SWITCHES
---------------
	hostname SW1
	enable secret Ciscoenpa55
	line console 0
	password Ciscolinepa55
	login
	exit
	line vty 0 15
	password Ciscolinepa55
	login
	exit
	banner motd % *** SOLO PERSONAL AUTORIZADO ACCEDERÁ AL DISPOSITIVO *** %
	END
	copy run start

---

	hostname SW2
	enable secret Ciscoenpa55
	line console 0
	password Ciscolinepa55
	login
	exit
	line vty 0 15
	password Ciscolinepa55
	login
	exit
	banner motd % *** SOLO PERSONAL AUTORIZADO ACCEDERÁ AL DISPOSITIVO *** %
	END
	copy run start




SEGURIDAD BASICA 
---

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
	transport input ssh
	login local
	exec-timeout 6
	loggin synchronous
	banner motd $ *** SOLO PERSONAL AUTORIZADO *** $
	end
	copy running-config startup-config




















