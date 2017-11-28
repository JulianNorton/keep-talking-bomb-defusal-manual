print('test')

affirmative_response = ['true', '1', 't', 'y', 'yes', 'yeah', 'yup']

def case_settings():
    parallel_port = input("Parallel port? y/n\n")
    # Define Parallel port
    if parallel_port in affirmative_response:
        parallel_port = True
    else:
        print('No parallel port.')
        parallel_port = False
    # Define batteries
    batteries = input("Is there more than 1 battery? y/n\n")
    if batteries in affirmative_response:
        batteries = True
    else:
        print('1 or less batteries')
        batteries = False

    # Define serial digit
    serial_digit_odd = input("Is the last serial digit odd? y/n\n")
    if serial_digit_odd in affirmative_response:
        serial_digit_odd = True
    else:
        print('Serial digit is not odd.')
        serial_digit_odd = False
    
def simple_wires(parallel_port, batteries, serial_digit_odd):
    # TODO, remove this into global function
    # show the case settings
    print('parallel_port', parallel_port)
    print('batteries', batteries)
    print('serial_digit_odd', serial_digit_odd)

    wire_count = int(input("How many wires?\n"))
    print(wire_count)
    # Check to make sure wire count is valid
    wire_list = list()
    print("Red, white, blue, black, or yellow?")
    for i in range(wire_count):
        current_wire=str.lower((input("Enter the color:")))
        print(current_wire)
        wire_list.append(current_wire)
    print(wire_list)
    # 3 wire solutions
    if wire_count == 3:
        print(' 3 wire solution')
        if 'red' not in wire_list:
            print('!!!!!!!!!!!!!!!!!!!')
            print('cut the SECOND wire!\n')
        elif wire_list[2] == 'white':
            print('!!!!!!!!!!!!!!!!!!!')
            print('cut the LAST wire!\n')
        elif wire_list.count('blue') > 1:
            print('!!!!!!!!!!!!!!!!!!!')
            print('cut the LAST *BLUE* wire!\n')
    # 4 wire solutions
    elif wire_count == 4:
        if wire_list.count('red') > 1 and (serial_digit_odd == True):
            print('!!!!!!!!!!!!!!!!!!!')
            print('cut the LAST *RED* wire!\n')
        elif wire_list[3] == 'yellow' and ('red' not in wire_list):
            print('!!!!!!!!!!!!!!!!!!!')
            print('cut the FIRST wire!\n')
        elif wire_list.count('blue') == 1:
            print('!!!!!!!!!!!!!!!!!!!')
            print('cut the FIRST wire!\n')
        elif wire_list.count('yellow') > 1:
            print('!!!!!!!!!!!!!!!!!!!')
            print('cut the LAST wire!\n')
        else:
            print('!!!!!!!!!!!!!!!!!!!')
            print('cut the SECOND wire!\n')
    # 5 wire solutions
    elif wire_count == 5:
        if wire_list[4] == 'black' and (serial_digit_odd == True):
            print('!!!!!!!!!!!!!!!!!!!')
            print('cut the FOURTH wire!\n')
        elif wire_list.count('red') == 1 and (wire_list.count('yellow') > 1):
            print('!!!!!!!!!!!!!!!!!!!')
            print('cut the FIRST wire!\n')
        elif 'black' not in wire_list:
            print('!!!!!!!!!!!!!!!!!!!')
            print('cut the SECOND wire!\n')
        else:
            print('!!!!!!!!!!!!!!!!!!!')
            print('cut the FIRST wire!\n')
    # 6 wire solutions
    elif wire_count == 6:
        if 'yellow' not in wire_list and (serial_digit_odd == True):
            print('!!!!!!!!!!!!!!!!!!!')
            print('cut the THIRD wire!\n')
        elif wire_list.count('yellow') == 1 and (wire_list.count('white') > 1):
            print('!!!!!!!!!!!!!!!!!!!')
            print('cut the FOURTH wire!\n')
        elif 'red' not in wire_list:
            print('!!!!!!!!!!!!!!!!!!!')
            print('cut the SECOND wire!\n')
        else:
            print('!!!!!!!!!!!!!!!!!!!')
            print('cut the FOURTH wire!\n')

# TODO, include case_settings()

simple_wires(True, False, True)

