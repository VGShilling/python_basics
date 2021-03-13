class OfficeEquipWarehouse:

    def __init__(self):
        self.devices_list = []
        self.cnt_devices = {'Принтер': 0, 'Сканнер': 0, 'МФУ': 0}

    def receive(self, device):
        device_dict = {'Наименование': device.name,
                       'Модель': device.model,
                       'Интерфейс устройства': device.interface,
                       'Формат бумаги': device.paper_format,
                       'Цвет': device.color,
                       'Тип печатающего устройства': device.print_type,
                       'Кострукция сканера': device.construction}
        self.devices_list.append(device_dict)
        self.cnt_devices[device.name] += 1
        print('\nНа склад получена новая офисная техника:')
        for key in device_dict:
            print('  ', key, ':', device_dict[key])

    def storage(self):
        print('\nОфисная техника на складе:')
        for el in self.devices_list:
            print(' ', el)
        print(f"Всего на складе:\n Принтер - {self.cnt_devices['Принтер']} шт., "
              f"Сканнер - {self.cnt_devices['Сканнер']} шт., МФУ - {self.cnt_devices['МФУ']} шт.")

    def transfer(self, device_name):
        ln = len(self.devices_list)
        for el in self.devices_list:
            if device_name in el.values():
                print(f'\nПередано со склада в подразделение:\n {el}')
                self.devices_list.remove(el)
                self.cnt_devices[device_name] -= 1
                break
        if ln == len(self.devices_list):
            print(f'\n{device_name} - отсутствует на складе')


class OfficeEquipment:
    def __init__(self, model, interface, paper_format, color):
        self.model = model
        self.interface = interface
        self.paper_format = paper_format
        self.color = color


class Printer(OfficeEquipment):
    def __init__(self, model, interface, paper_format, color, print_type):
        super().__init__(model, interface, paper_format, color)
        self.name = 'Принтер'
        self.print_type = print_type
        self.construction = None


class Scanner(OfficeEquipment):
    def __init__(self, model, interface, paper_format, color, construction):
        super().__init__(model, interface, paper_format, color)
        self.name = 'Сканнер'
        self.construction = construction
        self.print_type = None


class MFP(OfficeEquipment):
    def __init__(self, model, interface, paper_format, color, construction, print_type):
        super().__init__(model, interface, paper_format, color)
        self.name = 'МФУ'
        self.construction = construction
        self.print_type = print_type


warehouse = OfficeEquipWarehouse()
mfp = MFP('hp', 'usb', 'a4', 'цветной', 'планшетный', 'лазерный')
scanner = Scanner('hp1', 'usb', 'a4', 'цветной', 'планшетный')
printer = Printer('epson', 'usb', 'A3', 'цветной', 'лазерный')

warehouse.receive(mfp)
warehouse.receive(scanner)
warehouse.receive(printer)
warehouse.storage()
warehouse.transfer('Принтер')
warehouse.storage()
