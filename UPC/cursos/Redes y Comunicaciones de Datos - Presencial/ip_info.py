import sys

class Mask:
    def __init__(self):
        self.mask = [0,0,0,0]
        self.CIDR = 0
        self.wildcard = [255,255,255,255]

    def gen_mask(_mask):
        new_mask = Mask()
    
        if   type(_mask) == int:
            new_mask.CIDR = _mask
            new_mask.mask = Mask.calc_mask(new_mask.get_CIDR())
        elif type(_mask) == list:
            new_mask.mask = _mask
            new_mask.CIDR = Mask.calc_CIDR(new_mask.get_mask())

        new_mask.wildcard = Mask.calc_wildcard(new_mask.get_mask())

        return new_mask

    def get_CIDR(self):
        return self.CIDR

    def str_CIDR(self):
        return str(self.CIDR)

    def get_mask(self):
        return self.mask

    def str_mask(self):
        return ".".join(list(map(str, self.mask)))

    def get_wildcard(self):
        return self.wildcard

    def str_wikdcard(self):
        return ".".join(list(map(str, self.wildcard)))

    def calc_mask(_mask: int) -> []:
        if _mask < 0 or _mask > 32:
            raise Exception("mascara fuera de rango")

        new_mask = [0,0,0,0]
        col      = 0
        bits     = 7
        while col <= 3 and _mask > 0: 
            new_mask[col] |= 1 << bits
            bits -= 1
            _mask -= 1
            if bits == -1:
                col += 1
                bits = 7
            

        return new_mask

    def calc_CIDR(_mask: list) -> int:
        # todo: mejorar legibilidad y algoritmo

        count = 0
        mask  = _mask[0:]
        col   = 0
        element = mask[col]
        while True:
            count += element & 1
            element >>= 1
            if element == 0:
                col += 1
                if col > 3:
                    break
                element = mask[col]
 
        return count

    def calc_wildcard(_mask: list) -> list:
        wildcard = [255,255,255,255]
        for [key, value] in enumerate(_mask):
            wildcard[key] = wildcard[key] - value
        return wildcard

    def __str__(self):
        txt = ""
        txt += "CIDR: " + str(self.CIDR) + "\n"
        txt += "Mask: " + str(self.mask) + "\n"
        txt += "Wildcard " + str(self.Wildcard)
        return txt
    

class Address:
    def __init__(self):
        self.address = [0,0,0,0]

    def gen_address(_address):
        new_address = Address()
        
        new_address.address = _address

        return new_address

    def get_address(self):
        return self.address

    def str_address(self):
        return ".".join(list(map(str, self.address)))
    
    def get_full(self):
        return self.full

    def __str__(self):
        txt = ""
        txt += "Address: " + str(self.address)

class IP:
    def __init__(self, address, mask):
        self.address = address
        self.mask    = mask

    def get_address(self):
        return self.address

    def get_mask(self):
        return self.mask

def main():
    if len(sys.argv) < 3:
        raise Exception("[x] Cantidad de argumentos invalida")

    input_ip   = sys.argv[1]
    input_mask = sys.argv[2]
    
    convert_ip = None
    convert_mask = None
    if input_ip.isnumeric():
        convert_ip = int(input_ip)
    else:
        convert_ip = list(map(int, input_ip.split('.')))

    if   input_mask.isnumeric():
        convert_mask = int(input_mask)
    else:
        convert_mask = list(map(int, input_mask.split('.')))

    ip   = Address.gen_address(convert_ip) 
    mask = Mask.gen_mask(convert_mask)
    fullip = IP(ip, mask)

    full = f"{ip.str_address()}/{mask.str_CIDR()}"
    # print(f"[*] Full: {full}")
    # print("\tADDRESS \t/ \tMASK \t\t/ \tWILDCARD")
    # print("\t------- \t/ \t---- \t\t/ \t--------")
    # print("\t" + address.str_address() + " \t/ " + mask.str_mask() + "  (/" + mask.str_CIDR() + ")" + " \t/\t " + mask.str_wikdcard())

    print(ip.str_address() + "," + mask.str_mask() + "/" + mask.str_CIDR() + "," + mask.str_wikdcard())

if __name__ == "__main__":
    # try:
    # except Exception as e:
    #     print(str(e))
    main()

# tests = range(0, 33)
# for test in tests:
#     it = Mask.gen_mask(str(test))
#     print(it.str_CIDR() , it.str_wikdcard())
