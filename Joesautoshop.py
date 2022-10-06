

class Customer:
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    def set_name(self, name):
        self.__name = name
    
    def set_address(self, address):
        self.__address = address

    def set_phone(self, phone):
        self.__phone = phone
    
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address
    
    def get_phone(self):
        return self.__phone

    
    class Car:
        def __init__(self, make, model, year):
            self.__make = make
            self.__model = model
            self.__year = year

        def set_make(self, make):
            self.__make = make

        def set_model(self, model):
            self.__model = model
        
        def set_year(self, year):
            self.__year = year

        def get_make(self):
            return self.__make

        def get_model(self):
            return self.__model
        
        def get_year(self):
            return self.__year


    class ServiceQuote:
        def __init__(self, parts_chg, labor_chg):
            self.__parts_chg = parts_chg
            self.__labor_chg = labor_chg

        def set_parts_chg(self, parts_chg):
            self.__parts_chg = parts_chg

        def set_labor_chg(self, labor_chg):
            self.__labor_chg = labor_chg

        def get_parts_chg(self):
            return self.__parts_chg

        def get_labor_chg(self):
            return self.__labor_chg

        def get_sales_tax(self):
            return 8

        def get_total_charges(self):
            tot_chg = self.get_labor_chg + self.get_parts_chg + self.get_sales_tax
            return tot_chg + tot_chg*(self.get_sales_tax/100)
