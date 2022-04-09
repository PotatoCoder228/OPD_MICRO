Alphabet = {'0000': '0',
            '0001': '1',
            '0010': '2',
            '0011': '3',
            '0100': '4',
            '0101': '5', '0110': '6',
            '0111': '7', '1000': '8', '1001': '9',
            '1010': 'A', '1011': 'B', '1100': 'C',
            '1101': 'D', '1110': 'E', '1111': 'F'}
Alphabet_inv = {'0': '0000',
                '1': '0001',
                '2': '0010',
                '3': '0011',
                '4': '0100',
                '5': '0101', '6': '0110',
                '7': '0111', '8': '1000', '9': '1001',
                'A': '1010', 'B': '1011', 'C': '1100',
                'D': '1101', 'E': '1110', 'F': '1111'}


def info(command):
    global Alphabet_inv
    global Alphabet
    second_bit = Alphabet_inv[command[1:2]]
    info = ""
    if command[:1] == "0":
        info = non_adr_com(command)
    elif command[:1] == "F":
        info = if_else_com(command)
    elif second_bit[:1] == "0":
        info = just_adr_com(command)
    elif second_bit[:1] == "1":
        info = over_adr_com(command, second_bit)
    return info

def just_adr_com(command):
    String = ""
    type = "прямая абсолютная адресация"
    mnemonika = ""
    count_memory = 0
    memory = command[1:]
    info = "Команда" + " " + command + ":"
    text = open("absolute.txt", "r", encoding='utf-8')
    for i in range(13):
        text_str = text.readline().replace("\n", "").split(" ")
        mnemonika = text_str[1] + " " + memory
        count_memory = text_str[3]
        if text_str[0][:1] == command[:1]:
            print(mnemonika)
            String = text_str[2].replace(":", " ")
            info +="\n\tТип адресации:" + type
            info += "\n\tКоманда, мнемоника:" + command + ", " + mnemonika
            info += "\n\tОписание:" + String
            info += "\n\tКоличество обращений к памяти:" + count_memory
    text.close()
    return info


def non_adr_com(command):
    String = ""
    type = "безадресная команда"
    mnemonika = ""
    count_memory = 0
    info = "Команда" + " " + command + ":"
    text = open("non.txt", "r", encoding='utf-8')
    for i in range(22):
        text_str = text.readline().replace("\n", "").split(" ")
        mnemonika = text_str[1]
        count_memory = text_str[3]
        if text_str[0][1:2] == command[1:2]:
            print(mnemonika)
            String = text_str[2].replace(":", " ")
            info +="\n\tТип адресации:" + type
            info +="\n\tКоманда, мнемоника:" + command + ", " + mnemonika
            info += "\n\tОписание:" + String
            info += "\n\tКоличество обращений к памяти:" + count_memory
    text.close()
    return info


def if_else_com(command):
    String = ""
    type = "команда ветвления"
    mnemomika = ""
    count_memory = 0
    memory = command[1:]
    info = "Команда" + " " + command + ":"
    text = open("if_else.txt", "r", encoding='utf-8')
    for i in range(10):
        text_str = text.readline().replace("\n", "").split(" ")
        two_mnemo = text_str[1].split("&")
        if len(two_mnemo) == 2:
            mnemonika = two_mnemo[0] + " " + command[2:] + " и " + two_mnemo[1] + " " + command[2:]
        else:
            mnemonika = text_str[1]+" "+command[2:4]
        count_memory = text_str[3]
        if text_str[0][:2] == command[:2]:
            print(mnemonika)
            String = text_str[2].replace(":", " ")
            info += "\n\tТип адресации:" + type
            info += "\n\tКоманда, мнемоника:" + command + ", " + mnemonika
            info +="\n\tОписание:" + String
            info +="\n\tКоличество обращений к памяти:" + count_memory
    text.close()
    return info


def over_adr_com(command, second_bit):
    String = ""
    type = ""
    mnemonika = ""
    count_memory = 0
    memory = ""
    info = "Команда" + " " + command + ":"
    text = open("absolute.txt", "r", encoding='utf-8')
    if second_bit == "1110":
        type = "прямая относительная адресация"
        if Alphabet_inv[command[2:3]][:1] == "1":
            memory = "IP-" + hex(int(ip_step(Alphabet_inv[command[2:3]] + Alphabet_inv[command[3:4]])))[2:].upper()
        elif Alphabet_inv[command[2:3]][:1] == "0":
            memory = "IP+" + hex(int(ip_dec_step(Alphabet_inv[command[2:3]] + Alphabet_inv[command[3:4]])))[2:].upper()
        for i in range(13):
            text_str = text.readline().replace("\n", "").split(" ")
            mnemonika = text_str[1] + " " + memory
            count_memory = text_str[3]
            if text_str[0][:1] == command[:1]:
                print(mnemonika)
                String = text_str[2].replace(":", " ")
                info +="\n\tТип адресации:" + type
                info +="\n\tКоманда, мнемоника:" + command + ", " + mnemonika
                info +="\n\tОписание:" + "M=" + memory + ", " + String
                info +="\n\tКоличество обращений к памяти:" + count_memory
    elif second_bit == "1111":
        type = "прямая загрузка операнда"
        if Alphabet_inv[command[2:3]][:1] == "1":
            memory = "#-" + ip_step(Alphabet_inv[command[2:3]] + Alphabet_inv[command[3:4]])
        elif Alphabet_inv[command[2:3]][:1] == "0":
            memory = "#" + ip_dec_step(Alphabet_inv[command[2:3]] + Alphabet_inv[command[3:4]])
        for i in range(13):
            text_str = text.readline().replace("\n", "").split(" ")
            mnemonika = text_str[1] + " " + memory
            count_memory = text_str[3]
            if text_str[0][:1] == command[:1]:
                print(mnemonika)
                String = text_str[2].replace(":", " ")
                info +="\n\tТип адресации:" + type
                info +="\n\tКоманда, мнемоника:" + command + ", " + mnemonika
                info +="\n\tОписание:" + "M=" + memory[1:] + ", " + String
                info +="\n\tКоличество обращений к памяти:" + str(int(count_memory) - 1)
    elif second_bit == "1000":
        type = "косвенная относительная адресация"
        if Alphabet_inv[command[2:3]][:1] == "1":
            memory = "IP(-" + hex(int(ip_step(Alphabet_inv[command[2:3]] + Alphabet_inv[command[3:4]])))[2:].upper() + ")"
        elif Alphabet_inv[command[2:3]][:1] == "0":
            memory = "IP(+" + hex(int(ip_dec_step(Alphabet_inv[command[2:3]] + Alphabet_inv[command[3:4]])))[2:].upper() + ")"
        for i in range(13):
            text_str = text.readline().replace("\n", "").split(" ")
            mnemonika = text_str[1] + " " + memory
            count_memory = text_str[3]
            if text_str[0][:1] == command[:1]:
                print(mnemonika)
                String = text_str[2].replace(":", " ")
                info +="\n\tТип адресации:" + type
                info +="\n\tКоманда, мнемоника:" + command + ", " + mnemonika
                info +="\n\tОписание:" + "M=содержание ячейки с номером " + memory.replace("(", "").replace(")",
                                                                                                         "") + ", " + String
                info +="\n\tКоличество обращений к памяти:" + str(int(count_memory) + 2)
    elif second_bit == "1010":
        type = "косвенная (относительная) автоинкрементная адресация"
        if Alphabet_inv[command[2:3]][:1] == "1":
            memory = "(IP-" + hex(int(ip_step(Alphabet_inv[command[2:3]] + Alphabet_inv[command[3:4]])))[2:].upper() + ")+"
        elif Alphabet_inv[command[2:3]][:1] == "0":
            memory = "(IP+" + hex(int(ip_dec_step(Alphabet_inv[command[2:3]] + Alphabet_inv[command[3:4]])))[2:].upper() + ")+"
        for i in range(13):
            text_str = text.readline().replace("\n", "").split(" ")
            mnemonika = text_str[1] + " " + memory
            count_memory = text_str[3]
            if text_str[0][:1] == command[:1]:
                print(mnemonika)
                String = text_str[2].replace(":", " ")
                info +="\n\tТип адресации:" + type
                info +="\n\tКоманда, мнемоника:" + command + ", " + mnemonika
                info +="\n\tОписание:" + "M=содержание ячейки с номером " + memory.replace("(", "")[
                                                                         :-2] + "\n\tпосле операции содержание ячейки IP-3 инкрементируется," + String
                info +="\n\tКоличество обращений к памяти:" + str(int(count_memory) + 2)
    elif second_bit == "1011":
        type = "косвенная (относительная) авто декрементная адресация"
        if Alphabet_inv[command[2:3]][:1] == "1":
            memory = "-(IP-" + hex(int(ip_step(Alphabet_inv[command[2:3]] + Alphabet_inv[command[3:4]])))[2:].upper() + ")"
        elif Alphabet_inv[command[2:3]][:1] == "0":
            memory = "-(IP+" + hex(int(ip_dec_step(Alphabet_inv[command[2:3]] + Alphabet_inv[command[3:4]])))[2:].upper() +")"
        for i in range(13):
            text_str = text.readline().replace("\n", "").split(" ")
            mnemonika = text_str[1] + " " + memory
            count_memory = text_str[3]
            if text_str[0][:1] == command[:1]:
                print(mnemonika)
                String = text_str[2].replace(":", " ")
                info +="\n\tТип адресации:" + type
                info +="\n\tКоманда, мнемоника:" + command + ", " + mnemonika
                info +="\n\tОписание:" + "M=содержание ячейки с номером " + memory.replace("(", "")[:-1][
                                                                         1:] + "\n\tперед операцией содержание ячейки IP-3 декрементируется," + String
                info +="\n\tКоличество обращений к памяти:" + str(int(count_memory) + 2)
    elif second_bit == "1100":
        type = "адресация относительно SP"
        if Alphabet_inv[command[2:3]][:1] == "1":
            memory = "(SP-" + hex(int(ip_step(Alphabet_inv[command[2:3]] + Alphabet_inv[command[3:4]])))[2:].upper()+")"
        elif Alphabet_inv[command[2:3]][:1] == "0":
            memory = "(SP+" + hex(int(ip_dec_step(Alphabet_inv[command[2:3]] + Alphabet_inv[command[3:4]])))[2:].upper()+")"
        for i in range(13):
            text_str = text.readline().replace("\n", "").split(" ")
            mnemonika = text_str[1] + " " + memory
            count_memory = text_str[3]
            if text_str[0][:1] == command[:1]:
                print(mnemonika)
                String = text_str[2].replace(":", " ")
                info +="\tТип адресации:" + type
                info +="\tКоманда, мнемоника:" + command + ", " + mnemonika
                info +="\tОписание:" + "M=" + memory + ", " + String
                info +="\tКоличество обращений к памяти:" + count_memory
    text.close()
    return info


def ip_step(a):
    summ = 0
    n = len(a) - 1
    for i in a:
        summ += abs(int(i) - 1) * (2 ** n)
        n -= 1
    summ += 1
    summ = str(summ)
    return summ


def ip_dec_step(a):
    summ = 0
    n = len(a) - 1
    for i in a:
        summ += int(i) * (2 ** n)
        n -= 1
    summ = str(summ)
    return summ

def info_stack():
    commands = input("Введите все команды через пробел:")
    commands = commands.upper()
    list = commands.split(" ")
    for i in list:
        info(i)

info_stack()
