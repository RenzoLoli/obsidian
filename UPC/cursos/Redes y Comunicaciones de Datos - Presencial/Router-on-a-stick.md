_metodo para intercomunicar vlans_

---
### Switch

	1) Configurar puerto para enlace troncal con el router

---
### Router

* Encender la interfaz

		en
		conf t
		int <interface>/<puerto>
		no shutdown
		exit

* Configurar las subinterfaces para enrutar las vlan

		en
		conf t
		int <interface>/<puerto>.<numero_vlan>
		encapsulation dot1Q <numero_vlan>
		ip address <ip_vlan> <mask_vlan>

* Agregar los Gateway predeterminados a los dispositivos finales de cada vlan