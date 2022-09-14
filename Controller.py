from Model import Model
from View import View


class Controller:

    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def main(self):
        self.view.main()

    def on_button_click(self, caption):
        self.model.printer(caption)
        self.view.lab.config(text="dsdf")

    def get_spread(self):
        entry_pool = self.view.ent.get()
        try:
            entry_pool = int(entry_pool)
        except:
            print("błąd")
            entry_pool = 1

        print (self.view.btn_rb.get())
        print (self.view.var_check_box.get())
        dict = {}
        dict = self.model.spread_generator()

        if self.view.btn_rb.get()== 1  and self.view.var_check_box.get()==0:    #wszystkie od najmniejszego spreadu
            dict = self.model.sort_dict_lowest_value(dict)
            print(dict)
            list_of_x_elements_from_dict = self.model.get_x_amount_of_dict_elements(dict, entry_pool)
            self.view.lab.config(text=list_of_x_elements_from_dict)
        elif self.view.btn_rb.get()==1  and self.view.var_check_box.get()==1:   #wszystkie coiny od najwiekszego  spreadu  NIE DZIAŁA SORTOWANIE
            dict = self.model.sort_dict_highest_value(dict)
            print(dict)
            list_of_x_elements_from_dict = self.model.get_x_amount_of_dict_elements(dict, entry_pool)
            self.view.lab.config(text=list_of_x_elements_from_dict)

        elif self.view.btn_rb.get()==2 and self.view.var_check_box.get()==0:         #tylko perpy od najmniejszego  spreadu
            dict = self.model.perp_market_from_dict_generator(dict)
            dict = self.model.sort_dict_lowest_value(dict)
            print(dict)
            list_of_x_elements_from_dict = self.model.get_x_amount_of_dict_elements(dict, entry_pool)
            self.view.lab.config(text=list_of_x_elements_from_dict)


        elif self.view.btn_rb.get()==2 and self.view.var_check_box.get()==1:      #tylko perpy od największego spreadu
            dict = self.model.perp_market_from_dict_generator(dict)
            dict = self.model.sort_dict_highest_value(dict)
            print(dict)
            list_of_x_elements_from_dict = self.model.get_x_amount_of_dict_elements(dict, entry_pool)
            self.view.lab.config(text=list_of_x_elements_from_dict)


    def on_button(self):
        print("button clicked")


if __name__ == '__main__':
    print("if main")
    calculator = Controller()
    calculator.main()
    print("Mariusz z commitem")


