# number = int(input("Digite um número de 0 a 1000000: "))
# number_in_string = str(number)

def n2x(number):
    number_in_string = str(number)

    one_dig_list_x = ["zero","um","dois","três","quatro","cinco","seis","sete","oito","nove"]
    ten_to_nineteen = ["dez", "onze", "doze", "treze", "quatorze", "quinze", "desesseis", "desessete", "dezoito", "dezenove"]
    tens_place_list_x = ["vinte", "trita", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
    hundreds_house_x = ["cento", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"]

    if len(number_in_string) == 1:
        print(one_dig_list_x[number])
    elif len(number_in_string) == 2:        
        d = int(number / 10)
        u = number % 10

        if d == 1:
            print(ten_to_nineteen[u])
        else:
            if u == 0:
                print(tens_place_list_x[d - 2])
            else:
                print(str(tens_place_list_x[d - 2]), "e", one_dig_list_x[u])
    elif len(number_in_string) == 3:
        c = int(number / 100)
        d = int((number / 10) % 10)
        u = number % 10
        
        if number == 100:
            print("cem")
        else:
            print(f"{hundreds_house_x[c - 1]}", end=" ")
            if number % 100 != 0:
                if number % 10 == 0:
                    print(f"e {tens_place_list_x[d - 2]}")
                else:
                    if d != 0 or u !=0:
                        if d == 0:
                            print(f"e {one_dig_list_x[u]}")
                        elif d == 1:
                            print(f"e {ten_to_nineteen[u]}")
                        else:
                            print(f"e {tens_place_list_x[d - 2]}", end=" ")
                            if u != 0:
                                print(f"e {one_dig_list_x[u]}")
            else:
                print("")
    elif len(number_in_string) == 4:
        m = int(number / 1000)
        c = int((number % 1000) / 100)
        d = int((number % 100) / 10)
        u = number % 10

        print(one_dig_list_x[m], "mil", end=" ")

        if c != 0 or d != 0 or u != 0:
            if c != 0:
                if c == 1 and d == 0 and u == 0:
                    print("e cem", end="")
                else:
                    print("e", hundreds_house_x[c - 1], end=" ")
                if d != 0:
                    if d == 1:
                        print("e", ten_to_nineteen[u])
                    else:
                        print("e", tens_place_list_x[d - 2], end=" ")
                        if u != 0:
                            print("e", one_dig_list_x[u])
                        else:
                            print("")
                elif u != 0:
                    print("e", one_dig_list_x[u])
                else:
                    print("")
            elif d != 0:
                if d == 1:
                    print("e", ten_to_nineteen[u])
                else:
                    print("e", tens_place_list_x[d - 2], end=" ")
                    if u != 0:
                        print("e", one_dig_list_x[u])
                    else:
                        print("")
            else:
                print("e", one_dig_list_x[u])
        else:
            print("")
    elif len(number_in_string) == 5:
        cm = int(number / 10000)
        m = int((number % 10000) / 1000)
        c = int((number % 1000) / 100)
        d = int((number % 100) / 10)
        u = number % 10

        if cm == 1:
            print(ten_to_nineteen[m], "mil", end=" ")
            if c == 0 and d == 0 and u == 0:
                print("")
            else:
                if c != 0:
                    if c == 1 and d == 0 and u == 0:
                        print("e cem", end=" ")
                    else:
                        print("e", hundreds_house_x[c - 1], end=" ")
                    if d != 0:
                        if d == 1:
                            print("e", ten_to_nineteen[u])
                        else:
                            print("e", tens_place_list_x[d - 2], end=" ")
                            if u != 0:
                                print("e", one_dig_list_x[u])
                            else:
                                print("")
                    elif u != 0:
                        print("e", one_dig_list_x[u])
                    else:
                        print("")
                elif d !=0:
                    if d == 1:
                        print("e", ten_to_nineteen[u])
                    else:
                        print("e", tens_place_list_x[d - 2], end=" ")
                        if u != 0:
                            print("e", one_dig_list_x[u])
                        else:
                            print("")
                elif u != 0:
                    print("e", one_dig_list_x[u])

for i in range(0, 1000000, 1):
    if i > 10000 and i <= 20000:
        n2x(i)
        