class OfficeEquipmentWarehouse:
    def __init__(self, value, devices_amount):
        self.value = value
        self.devices_amount = devices_amount



class OfficeEquipment:
    def __init__(self, height, wight, length, price, brand):
        self.height = height
        self.length = length
        self.wight = wight
        self.price = price
        self.brand = brand


class Xerox(OfficeEquipment):
    def __init__(self):
        super().__init__()


class Scanner(OfficeEquipment):
    def __init__(self):
        super().__init__()


class Printer(OfficeEquipment):
    def __init__(self):
        super().__init__()