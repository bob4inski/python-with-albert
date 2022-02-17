class Phone:

    @staticmethod
    def get_coutry_cod(num):
        return num[1:-14]

    @staticmethod
    def check_number(num):
        numbers = ''.join(num[1:].split('-'))
        digits = numbers.isdigit()
        plus = num[0] == '+'
        minus = (num[-3] + num[-6] + num[-10] + num[-14]) == '----'
        return digits and plus



print(Phone.check_number('+72222-922-664-82-58'))
print(Phone.get_coutry_cod('+72ВВС2-922-664-82-58'))





