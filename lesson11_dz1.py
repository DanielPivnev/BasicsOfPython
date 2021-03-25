class Data:
    def __init__(self, d):
        self.data = d

    @classmethod
    def data_numbers_str_to_int(cls):
        _data = cls(data).data.split('.')
        for i in range(len(_data)):
            _data[i] = int(_data[i])
        return cls.data_valid(_data)

    @staticmethod
    def data_valid(v_d):
        valid_data = v_d
        mouth_31_day_list = [1, 3, 5, 8, 12]
        mouth_30_day_list = [4, 6, 7, 9, 11]
        october = 10
        february = 2
        leap_year = 2020
        # year validation
        if valid_data[2] < 1900:
            valid_data[2] = 1900
        elif valid_data[2] > 2021:
            valid_data[2] = 2021
        # mouth validation
        if valid_data[1] < 1:
            valid_data[1] = 1
        elif valid_data[1] > 12:
            valid_data[1] = 12
        # day validation
        if valid_data[0] < 1:
            valid_data[0] = 1
        else:
            for m in mouth_31_day_list:
                if valid_data[0] > 31 and valid_data[1] == m:
                    valid_data[0] = 31
                    break
            for m in mouth_30_day_list:
                if valid_data[0] > 30 and valid_data[1] == m:
                    valid_data[0] = 30
                    break
            if valid_data[0] > 29 and valid_data[1] == october:
                valid_data[0] = 29
            elif valid_data[0] >= 29 and valid_data[1] == february and (valid_data[2] - leap_year) % 4 == 0:
                valid_data[0] = 29
            elif valid_data[0] > 28 and valid_data[1] == february:
                valid_data[0] = 28

        return valid_data


txt = 'Enter please a data in a form of "dd.mm.yyyy": '
data = input(txt)
print(Data.data_numbers_str_to_int())
