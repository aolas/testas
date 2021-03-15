# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



def uzdvn1(n,a,b):
    count = 0 #nustatoma pradinė teksto vertė
    try:
        for ind in range(0, len(n)):  # ciklas eina per visus teksto elementus
            for i in range(len(a)):   #einama per teigiamus simbolius
                if n[ind] == a[i]:    # tikrinama ar nagrin4jamas n simbolis atitinka nagrinejama a simbol5
                    count= count +1
            for i in range(len(b)):  # einama per neigiamus simbolius
                if n[ind] == b[i]:   # tikrinama ar nagrin4jamas simbolis n lygus nagrinėjamas simboliui b
                    count = count -1
    except TypeError:
        print("Invalid input provided")
    return count


def input_data(data_list):
    """
    Task2
    :param data_list: Takes list of numbers
    :return: None
    :outputs results from data_analyzis
    """
    try:
        for el in data_list:            #einama per sąrašą
            result = data_analyzis(el)  # sąrašas perduodamas analizei
            print (result)
    except TypeError:                   # Klaidų suvaldymas kai pateikiami netinkami duomenys
        print("Invalid input type provided")
#decorator
def change_by(val):                                      #funkcija naudojama paimti dekoratoriaus kintamajį
    def decorator(func):
        def wrapper(*args, **kwargs):                    #modifikuojamos funkcijos
            avrg, min, max, suma = func(*args, **kwargs) #Gaunami pirminiai funkcijos rezultatai
            try:                                            # suvaldomi netinkami duomenys pateikti dekoratoriui
                avrg -= val                                  #Modifikuojami rezultatai nurodytu dydžiu
                min -= val
                max -= val
                suma -= val
            except TypeError:
                print("Invalid value provided to decorator")
            return avrg, min, max, suma                  #Perduodami pakeisti funkcijos duomenys
        return wrapper
    return decorator
@change_by(10)
def data_analyzis( input_list):
    new_list = []                   #kintamasis skirtas saugoti kriterijus atitinkančius skaičius
    for i in range(len(input_list)):                              #Atliekamas skaičių reikšmių tinkamumo patikrinimas
        if (input_list[i]>= 10  and input_list[i] <= 100):
            new_list.append(input_list[i])
    suma = sum(new_list)                                                    #sumuojami elementai
    avrg = suma / len(new_list)
    index_min = min(range(len(new_list)), key=new_list.__getitem__)         #iekoma minimumo indekso
    index_max = max(range(len(new_list)), key=new_list.__getitem__)         #iekoma maksimumo indekso
    return avrg, new_list[index_min], new_list[index_max], suma             #gražinami rezultatai


def symbol_analyzis():
    """
    Task3
    :return:
    :outputs splits list and output unique letter
    """
    # Use a breakpoint in the code line below to debug your script.
    input_x = input("Input string x : ")
    input_y = input("Enter number y : ")
    try:
        y = int(input_y)                          #Verciamos x ir y reiksmes i skaicius
        length = len(input_x)
        if (y > 0 and length % y == 0):           #tikrinama ar dalinasi lygiai iš y ir ar didesnis už 0
            times = int(length/y)                 # gaunamas sekmento dydis
            for ind in range(times):
                str_output = " "                 # Saraso sujungimui reikalinga reiksme
                res = []                         # Masyvas naudojamas pasalinti dublikatus
                [res.append(x) for x in input_x[y*ind:y*(ind+1)] if x not in res]  #formuojamas sarasas ir pasalinami dublikatai
                print(str_output.join(res)) # Sujungiamas sarasas ir atspausdinamas rezultatas
        else:
            print("Requirements not met")
    except ValueError:                        #Naudojama klaidu valdymui
        print("Invalid data input")
    except TypeError:
        print("Invalid input provided")
def compres_text(text):
    try:                                     # skirta suvaldyti netinkamus duomenis
        if len(text) > 0:                    # Tirinama ar reikia spausti
            current_letter = text[0]         #Parenkamas pirmas simbolis
            number_of_repetition = 0         # Naudojamas pasikartojančių raidžių skaičiavimui
            new_text = ""                   # naudojamas formuojant suspaustą teksta
            for el in text:
                if el == current_letter:          # Jei raid4 kartojasi didinamas skaitliukas
                    number_of_repetition += 1
                else:                              # raide nebesikartoja
                    new_text = new_text + current_letter + str(number_of_repetition)  # Issaugoma pasikartojimo informacija
                    current_letter = el                                               # Priskiriama nauja raidė ir pasikartojimų kiekis
                    number_of_repetition = 1
            new_text = new_text + current_letter + str(number_of_repetition)          # Išsaugoma paskutinė serija pasikartojimų
            return new_text
        else:
            print("No need to compress empty string")
    except TypeError:
        print("Invlid input type provided")
class uzdv2:
    def input(self,data_list):

        for el in data_list:
            self.data_analyzis(el)

    def data_analyzis(self, input_list):

        input_item_count =len(input_list)
        greater_than_10 = []
        new_list = []
        return_list = []
        for i in range(len(input_list)):                                   #Atliekamas skaičių reikšmių patikrinimas
            if (input_list[i]>= 10  and input_list[i] <= 100):
                new_list.append(input_list[i])
        suma = 0
        for i in range(len(new_list)):
            suma = suma + new_list[i]
        avrg = suma / len(new_list)

        return_list.append(avrg)

        index_min = min(range(len(new_list)), key=new_list.__getitem__)         #iekoma minimumo indekso
        index_max = max(range(len(new_list)), key=new_list.__getitem__)
        return_list.append(new_list[index_min])
        return_list.append (new_list[index_max])


        return_list.append(suma)

        print ( return_list)


class uzdav3:
    def symbol_analyzis(self):
        # Use a breakpoint in the code line below to debug your script.
        input_x = input("Input string x : ")
        input_y = input("Enter number y : ")
        try:
            y = int(input_y)                          #Verciamos x ir y reiksmes i skaicius
            length = len(input_x)
            if (y > 0 and length % y == 0):           #tikrinama ar dalinasi lygiai iš y ir ar didesnis už 0
                times = int(length/y)                 # gaunamas sekmento dydis
                for ind in range(times):
                    str_output = " "                 # Saraso sujungimui reikalinga reiksme
                    res = []                         # Masyvas naudojamas pasalinti dublikatus
                    [res.append(x) for x in input_x[y*ind:y*(ind+1)] if x not in res]  #formuojamas sarasas ir pasalinami dublikatai
                    print(str_output.join(res)) # Sujungiamas listas

            else:
                print("Requirements not met")

        except ValueError:
            print("Invalid data input")
        except TypeError:
            print("Invalid input provided")




# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    n = "vienas du trys"
    a = "tnsb "
    b = "aydes"
    n = "The latest attack against Microsoft was also carried out as a proof-of-concept by a researcher. Attacks targeting Amazon, Slack, Lyft, and Zillow, by contrast, were malicious, but it’s not clear if they succeeded in executing the malware inside their networks. "
    n = "keturiolika"
    a =  "ktur"
    b =  "ila"
    result = uzdvn1(n, a, b)
    if result == -1:
        print("Atlikta")
    print(result)
    """   
    print("uzd2")
    data_list = [[1, 10, 34, 110, 400, 30, 20], [-5, -10, 55, 120, 30], [2, 67, 23, 78, 200], ]
    data_list2 = [[-1, 45, 23, 32, 999], [67, 99, 23], [23]]
    input_data(data_list)
    print("call2")
    input_data(data_list2)
    print("call3")
    input_data([["a",11]])

    
    print ("uzd3")
    x = "AABCAAADA"
    y = 3
    symbol_analyzis()
    
    print ("uzd 5")
    x = "aaavvvfdff"
    result = compres_text(x)
    print(result)
    x = "avtvvvff"
    result = compres_text(x)
    print(result)
    compres_text("")
    """

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
