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
























