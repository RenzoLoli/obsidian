#### 1) Activar Vlan's  

		en
		conf t
		vlan <numero>
		name <nombre>
		exit


#### 2) Seleccionar puertos para la vlan

		en 
		conf t 
		int range <interface>/<desde>-<hasta>
		switchport mode access
		switchport access vlan <numero>
		exit

_-> la interface puede ser una o por rango_

#### 3) Configurar enlace troncal

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