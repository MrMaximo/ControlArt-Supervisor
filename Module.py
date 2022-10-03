class module:
    
    def __init__(self, module_ID, hardware_address, serial_number):
        self.mod_ID     = module_ID
        self.hdw_addr   = hardware_address
        self.ser_num    = serial_number
        
    def getID(self):
        return self.mod_ID
    
    def getMAC(self):
        return self.hdw_addr
    
    def getSerialNumber(self):
        return self.ser_num