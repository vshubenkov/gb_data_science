class ClsData:
    data_string = ''
    def __init__(self, data_string):
        ClsData.data_string = data_string

    @classmethod
    def convert_data_to_num(cls):
        if isinstance(cls.data_string, str):
            return cls.data_string.split('-')
        else:
            pass

    @staticmethod
    def check_data(data_num):
        print(data_num)

objData_1 = ClsData('16-05-2021')
objData_1.convert_data_to_num()
ClsData.check_data(objData_1.convert_data_to_num())

objData_2 = ClsData('16-06-2021')
objData_2.convert_data_to_num()

ClsData.check_data(objData_2.convert_data_to_num())
ClsData.check_data(objData_1.convert_data_to_num())