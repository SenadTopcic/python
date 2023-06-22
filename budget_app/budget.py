class Category:
    categories_blance = dict()
    def __init__(self, category):
        self.ledger = list()
        self.category = category
        self.categories_blance[category] = 0
    
    def deposit(self, amount, descritption=""):
        tmp_dict = dict()
        tmp_dict["amount"] = amount
        tmp_dict["description"] = descritption
        self.ledger.append(tmp_dict)
        self.categories_blance[self.category] = self.get_balance()

    def withdraw(self, amount, descritption=""):
        if not self.check_funds(amount):
            return False
        else :
            tmp_dict = dict()
            tmp_dict["amount"] = -1 * amount
            tmp_dict["description"] = descritption
            self.ledger.append(tmp_dict)
            self.categories_blance[self.category] = float(self.get_balance())
            return True

    def get_balance(self):
        i = 0
        suma = 0
        for i in range(len(self.ledger)):
            suma = suma + self.ledger[i]["amount"]
        return suma

    def transfer(self, amount, name_category):
        if not self.check_funds(amount):
            return False
        self.categories_blance[self.category] = float(self.get_balance())
        if self.categories_blance[self.category] > amount :
            name = name_category.category
            transfer_to = f"Transfer to {name_category.category}"
            transfer_from = f"Transfer from {self.category}"
            self.withdraw(amount, transfer_to)
            self.categories_blance[name] = self.categories_blance[name] + amount
            # update ledger list
            tmp_dict = dict()
            tmp_dict["amount"] = amount
            tmp_dict["description"] = transfer_from
            name_category.ledger.append(tmp_dict)
            return self.check_funds(amount)
    
    def check_funds(self, amount):
        result = True
        if amount > self.get_balance():
            result = False        
        return result
    
    def __str__ (self):
    #Header        
        title_len = len(self.category)
        numb_of_stars = int((30 - title_len)/2)
        head = f'{"*"*numb_of_stars}' + f"{self.category}" + f'{"*"*numb_of_stars}'
        #body
        body = ""
        i = 0
        for i in range(len(self.ledger)):
            item = self.ledger[i]
            tmp_desc = item['description'][0:23]
            tmp_amount = '{:.2f}'.format(item['amount'])
            if i < len(self.ledger) - 1:
                body = body + "{0:<23}{1:>7}".format(tmp_desc, tmp_amount) + "\n"
            else :
                body = body + "{0:<23}{1:>7}".format(tmp_desc, tmp_amount)
        #foot   
        foot = f"Total: {self.get_balance()}"
        #return for printing
        return  head + "\n" + body + "\n" + foot 

def create_spend_chart(cat):
    header = "Percentage spent by category"
    body = ""
    width = 0
    height = 0
    prc_list = list()
    output_lst = list()
    #calculate how many category we have
    length_cat = len(cat)
    
    #calculating the longest name in category
    longest_name = 0
    for name in cat:
        tmp_num = len(name.category)
        if longest_name < tmp_num:
            longest_name = tmp_num
    #define height and width of printing square 
    #height  = 12 is reserved for precentage, dividing line and length of longest name
    #width is defined number of category plus 1
    height = 12 + longest_name
    width = length_cat  + 1

    #extracting necessary data for calculating pecentage
    #percentage side is total expenses / total income * 100
    #after calculate we will rount to 10ns
    for i in range(length_cat):
        #defining length of current category
        tmp_len = len(cat[i].ledger)
        temp_perc = 0
        #define category expenses and income
        tmp_exp = 0
        for j in range(tmp_len):
            #defining short for amount value  in current category
            tmp_amount = cat[i].ledger[j]["amount"]
            if tmp_amount < 0:
                tmp_exp = tmp_exp + tmp_amount
        #adding percentage to prc_list
        temp_perc = (tmp_exp ) * (-1)
        prc_list.append(temp_perc)
        #print("TR", prc_list)
    sum_exp = 0
    sum_exp = sum(prc_list)
    below = fill_char_nam_cat(cat)
    above = fill_with_o(prc_list, sum_exp)
    left_side = (create_left_side(height))
    right_side = concate_arr(above, below)
    body = template(left_side, right_side)
    


    return header + "\n" + body

def create_left_side(height):
    result = list()
    tmp_side = ""
    for i in range(height):
        if i == 0:
            result.append(tmp_side + "100| ")
        elif i < 10 :
            result.append(" " + str((10 - i)*10) + "| ")
        elif i == 10 :
            result.append("  0| ")
        elif i == 11 :
            result.append("    -")
        else :
            result.append("     ")
    return result

def fill_with_o(prc_list, sum_exp):
    max_len = 12
    mod_name_lst = list()
    for i in range(len(prc_list)):
        num_of_o = int((prc_list[i]/sum_exp)*10)  + 2
        tmp_list_oos = list()
        for j in range(max_len):
            tmp_oos = ""
            if j < max_len - num_of_o :
                tmp_oos = "   "
            elif j == max_len - 1 :
                tmp_oos = "---"
            elif j >= max_len - num_of_o :
                tmp_oos = "o  "
            tmp_list_oos.append(tmp_oos)
        mod_name_lst.append(tmp_list_oos)       
    return mod_name_lst

def fill_char_nam_cat(kategorije):#modify names for printing to have equal length
    max_len = 0
    for name in kategorije:
        if max_len < len(name.category):
            max_len = len(name.category)
    mod_name_lst = list()
    for name in kategorije:
        tmp_name =""
        tmp_mod_lst = list()
        for i in range(max_len):
            try:
                tmp_name = name.category[i] + "  "
            except:
                tmp_name = "   "
            tmp_mod_lst.append(tmp_name)
        mod_name_lst.append(tmp_mod_lst)
    return mod_name_lst

def concate_arr(a, b):
    new_lst = list()
    for i in range(len(a)):
        lst_1 = a[i]
        lst_2 = b[i]
        lst_1.extend(lst_2)
        new_lst.append(lst_1)
    return new_lst

def template(left_side, right_side):
    tmp_str = ""
    for i in range(len(left_side)):
        tmp_str = tmp_str + left_side[i]
        for j in range(len(right_side)):
            if j < (len(right_side)) - 1:
                tmp_str = tmp_str + right_side[j][i]
            else :
                if i < len(left_side) - 1:
                    tmp_str = tmp_str + right_side[j][i] + "\n"
                else :
                    tmp_str = tmp_str + right_side[j][i]

    return tmp_str