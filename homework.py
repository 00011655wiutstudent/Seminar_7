
def calculate_average_price(input_dictionary):
    if check_float(input_dictionary):
        for a in input_dictionary:
            list_input = input_dictionary[a]
            i = 0
            value = 0
            while i < len(list_input):
                value = value + list_input[i]
                i = i + 1
            value = value/(i)
            value = round(value, 2)
            input_dictionary[a] = value
        return (input_dictionary)


def check_float(input_diction):
    for a in  input_diction:
        list_products = input_diction[a]
        i = 0
        while i < len(list_products):
            if type(list_products[i]) != float:
                print("Please make sure that you entered all the values as floats")
                return False
            i = i + 1
    return True

pasta_al_salmone = {
"Pomodorini/Tomatten/Tomatoes 250g pack": [1.99, 2.49, 1.19, 1.99],
"Capperi/Kappertjes/Capers": [0.69, 0.79, 0.89, 0.69],
"Olive oil extra virgin 750ml": [6.59, 7.29, 5.99, 6.39],
"Prezzemolo/Peterselie/Parsley": [0.99, 0.89, 0.99, 0.99],
"Coriandolo/Koriander/Coriander": [0.99, 0.89, 0.89, 0.89],
"Pasta Rummo 500g (Conchiglioni Rigati)": [2.29, 2.99, 2.99, 2.09],
"Salmone/Zalm/Salmon 250g": [4.99, 4.99, 4.99, 4.99],
"Aglio/Knoflook/Garlic": [0.99, 0.89, 0.99, 1.09],
"Olive/Olijven/Olives (Taggiasche)": [2.79, 3.49, 2.99, 3.09],
"Vino Bianco/Wit Wijn/White Wine (Greco di Tufo)": [14.95, 13.99, 14.18, 16.69],
"Caffe Lavazza (Black) 250g": [2.79, 3.09, 3.39, 2.79]
}

print(calculate_average_price(pasta_al_salmone))
