#### 1) Activar Vlan's  

	en
	conf t
	vlan <numero>
	name <nombre>
	exit

#### 2)  Activar puertos de interface

	en
	conf t
	int <interface>/<puerto>
	no shutdown
	exit

#### 3) Seleccionar puertos para la vlan

	en 
	conf t 
	int range <interface>/<desde>-<hasta>
	switchport mode access
	switchport access vlan <numero>
	exit

_-> la interface puede ser una o por rango_

#### 4) Configurar enlace troncal

	en 
	conf t
	int <interface>/<puerto>
	switchport mode trunk
	exit

_-> Se debe hacer en cada switch de cada punto del enlace troncal_

## Comandos Generales


* Mostrar Vlans

		show vlan
* Seleccionar la interface para configurar 

		interface <interface>/puerto
* Seleccionar rango de interfaces para configurar

		interface range <interface>/<desde>-<hasta>