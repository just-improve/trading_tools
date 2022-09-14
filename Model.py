from Ftx_methods import FtxClientWJ


class Model:
    def __init__(self):
        self.value = ''

    def printer (self, tekst):
        print(tekst)

    def perp_market_from_dict_generator(self,dict):
        new_dict = {}
        substring = "PERP"
        for x in dict:
            if substring in x:
                new_dict[x]=dict[x]
        return new_dict

    def spread_generator (sefl):
        obj_ftx = FtxClientWJ()
        all_future_info = obj_ftx.get_all_futures()
        #print(all_future_info[0]['ask'])
        #print(all_future_info[0]['bid'])
        list_0f_biggests_spread = []
        dict_of_spread = {}
        for x in all_future_info:
            ask = x['ask']
            bid = x['bid']
            #print(ask is None)
            #print(type(bid))
            spread = -1
            if ask is not None and bid is not None:
                spread =(ask/bid)-1
            dict_of_spread[x['name']]=spread

            #dict_of_spread[x['name']]=spread
            #list_0f_biggests_spread.append(spread)
        return dict_of_spread

    def get_x_amount_of_dict_elements(self, dict, ilosc):
        counter = 0
        new_list = []
        for x in dict.items():
            if counter<ilosc:
                new_list.append(x)
                counter+=1
        my_str = ""
        for x in new_list:
            my_str = my_str+ str(x) + "\n"
        return my_str

    def sort_dict_highest_value(self, dict):
        dict1= {}
        for w in sorted(dict, key=dict.get, reverse=True):
            #print(w, dict[w])
            dict1[w]=dict[w]
        return dict1

    def sort_dict_lowest_value(self, dict):
        dict1= {}
        for w in sorted(dict, key=dict.get, reverse=False):
            #print(w, dict[w])
            dict1[w]=dict[w]
        return dict1



    def sort_dict (self, dict1):

        sorted_values = sorted(dict1.values())  # Sort the values
        sorted_dict = {}

        for i in sorted_values:
            for k in dict1.keys():
                if dict1[k] == i:
                    sorted_dict[k] = dict1[k]
                    break

        sorted_dict = reversed(list(sorted_dict.items()))
        return sorted_dict


    def calculate(self, caption):
        print(f'button {caption}  clicked in model')
        if caption == 'C':
            self.value = ''

        elif caption == '+/-':
            self.value = self.value + caption

        elif isinstance(caption, int):
            self.value += str(caption)

        return self.value

    def return_label (self, label):
        return label
