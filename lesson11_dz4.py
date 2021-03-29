class OwnValueError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Wards:
    def __init__(self, ward):
        if type(ward) == str:
            self.ward = ward
        else:
            raise OwnValueError('Enter please for ward name str')
        self.divices = {
            'Xerox': [],
            'Scanner': [],
            'Printer': []
        }

    def receipt_device(self, device, device_kind):
        if f'{type(device)}' == "<class '__main__.Xerox'>" or f'{type(device)}' == "<class '__main__.Printer'>"\
                or f'{type(device)}' == "<class '__main__.Scanner'>":
            if type(device_kind) == str:
                self.divices[device_kind].append(device)
            else:
                raise OwnValueError('Enter please for device kind str')
        else:
            raise OwnValueError('Warehouse receipt just class')

    def restore_device(self, device_id, device_kind, warehouse):
        if f'{type(warehouse)}' == "<class '__main__.OfficeEquipmentWarehouse'>":
            if type(device_kind) == str:
                if type(device_id) == int:
                    devices_list = self.divices[device_kind]
                    i = 0
                    for device in devices_list:
                        if device.device_id == device_id:
                            warehouse.receipt(device, device_kind)
                            self.divices[device_kind].__delitem__(i)
                            break
                        i += 1
                else:
                    raise OwnValueError('Enter please for device id int')
            else:
                raise OwnValueError('Enter please for device kind str')
        else:
            raise OwnValueError('Warehouse must be a class')


class OfficeEquipmentWarehouse:
    def __init__(self):
        self.divices = {
            'Xerox': [],
            'Scanner': [],
            'Printer': []
        }

    def receipt(self, device, device_kind):
        if f'{type(device)}' == "<class '__main__.Xerox'>" or f'{type(device)}' == "<class '__main__.Printer'>"\
                or f'{type(device)}' == "<class '__main__.Scanner'>":
            if type(device_kind) == str:
                self.divices[device_kind].append(device)
            else:
                raise OwnValueError('Enter please for device kind str')
        else:
            raise OwnValueError('Warehouse receipt just class')

    def restore(self, device_kind, d_id, ward):
        if type(device_kind) == str:
            if type(d_id) == int:
                if f'{type(ward)}' == "<class '__main__.Wards'>":
                    divices_list = self.divices[device_kind]
                    i = 0
                    for divice in divices_list:
                        if divice.device_id == d_id:
                            ward.receipt_device(divice, device_kind)
                            self.divices[device_kind].__delitem__(i)
                            break
                        i += 1
                else:
                    raise OwnValueError('Enter please for ward str')
            else:
                raise OwnValueError('Enter please for device id int')
        else:
            raise OwnValueError('Enter please for device kind class')


class OfficeEquipment:
    def __init__(self, height, wight, length, price, brand, d_id):
        if type(height) == float or type(height) == int:
            self.height = height
        else:
            raise OwnValueError('Enter please for height int or float')
        if type(length) == float or type(length) == int:
            self.length = length
        else:
            raise OwnValueError('Enter please for length int or float')
        if type(wight) == float or type(wight) == int:
            self.wight = wight
        else:
            raise OwnValueError('Enter please for wight int or float')
        if type(price) == float or type(price) == int:
            self.price = price
        else:
            raise OwnValueError('Enter please for price int or float')
        if type(brand) == str:
            self.brand = brand
        else:
            raise OwnValueError('Enter please for brand str')
        if type(d_id) == int:
            self.device_id = d_id
        else:
            raise OwnValueError('Enter please for device id int')


class Xerox(OfficeEquipment):
    def __init__(self, height, wight, length, price, brand, d_id, a_print=True, m_copy=False):
        if type(a_print) == bool:
            self.air_print = a_print
        else:
            raise OwnValueError('Enter please for Air Print boolean')
        if type(a_print) == bool:
            self.multiple_copy = m_copy
        else:
            raise OwnValueError('Enter please for multiple copy boolean')
        super().__init__(height, wight, length, price, brand, d_id)


class Scanner(OfficeEquipment):
    def __init__(self, height, wight, length, price, brand, d_id, colors, d_scan=True, b_w=True):
        if type(d_scan) == bool:
            self.duplex_scan = d_scan
        else:
            raise OwnValueError('Enter please for duplex scan boolean')
        if type(colors) == str:
            self.colors = colors
        else:
            raise OwnValueError('Enter please for colors spectrum str')
        if type(b_w) == bool:
            self.black_white = b_w
        else:
            raise OwnValueError('Enter please for just black and white print boolean')
        super().__init__(height, wight, length, price, brand, d_id)


class Printer(OfficeEquipment):
    def __init__(self, height, wight, length, price, brand, d_id, d_print, c_storage):
        if type(d_print) == bool:
            self.duplex_print = d_print
        else:
            raise OwnValueError('Enter please for Duplex Print boolean')
        if type(c_storage) == str:
            self.color_storage = c_storage
        else:
            raise OwnValueError('Enter please for color storage boolean')
        super().__init__(height, wight, length, price, brand, d_id)


try:
    support = Wards('support')
    management = Wards('management')

    warehouse = OfficeEquipmentWarehouse()

    xerox1 = Xerox(46, 23, 45, 57, 'Xerox', 35, True, False, )
    xerox2 = Xerox(25, 47, 12, 35, 'Canon', 180, True, False)
    scanner1 = Scanner(12, 23, 45, 56, 'Epson', 430, 'RGB', True, True)
    scanner2 = Scanner(21, 123, 457, 215, 'Epson', 300, 'RGB', False, )
    printer1 = Printer(13, 25, 35, 14, 'Canon', 100, True, 'color cartridges')
    printer2 = Printer(14, 24, 25, 25, 'Printer', 26, True, 'bottle system')

    warehouse.receipt(xerox2, 'Xerox')
    warehouse.receipt(xerox1, 'Xerox')
    warehouse.receipt(scanner1, 'Scanner')
    warehouse.receipt(scanner2, 'Scanner')
    warehouse.receipt(printer2, 'Printer')
    warehouse.receipt(printer1, 'Printer')
    print(warehouse.divices)

    warehouse.restore('Scanner', 300, support)
    print(support.divices)
    print(warehouse.divices)

    support.restore_device(300, 'Scanner', warehouse)
    print(support.divices)
    print(warehouse.divices)

except OwnValueError as e:
    print(e)
