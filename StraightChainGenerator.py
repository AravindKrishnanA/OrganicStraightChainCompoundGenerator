import sys
import os
import mysql.connector as ms
#global front_screen
#global c
#global main_prg
def front_screen():
    os.system("cls")
    print("\t\t ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄      ")
    print("\t\t▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌     ")
    print("\t\t▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌       ▐░▌ ▀▀▀▀█░█▀▀▀▀      ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░▌░▌     ▐░▌     ")
    print("\t\t▐░▌               ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░▌          ▐░▌       ▐░▌     ▐░▌          ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░▌▐░▌    ▐░▌     ")
    print("\t\t▐░█▄▄▄▄▄▄▄▄▄      ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░▌ ▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌     ▐░▌          ▐░▌          ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░▌ ▐░▌   ▐░▌     ")
    print("\t\t▐░░░░░░░░░░░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░▌▐░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌          ▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░▌  ▐░▌  ▐░▌     ")
    print("\t\t ▀▀▀▀▀▀▀▀▀█░▌     ▐░▌     ▐░█▀▀▀▀█░█▀▀ ▐░█▀▀▀▀▀▀▀█░▌     ▐░▌     ▐░▌ ▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌     ▐░▌          ▐░▌          ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌     ▐░▌     ▐░▌   ▐░▌ ▐░▌     ")
    print("\t\t          ▐░▌     ▐░▌     ▐░▌     ▐░▌  ▐░▌       ▐░▌     ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌          ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░▌    ▐░▌▐░▌     ")
    print("\t\t ▄▄▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░▌      ▐░▌ ▐░▌       ▐░▌ ▄▄▄▄█░█▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌     ▐░▌          ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌▐░▌       ▐░▌ ▄▄▄▄█░█▄▄▄▄ ▐░▌     ▐░▐░▌     ")
    print("\t\t▐░░░░░░░░░░░▌     ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌     ▐░▌          ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌     ")
    print("\t\t ▀▀▀▀▀▀▀▀▀▀▀       ▀       ▀         ▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀       ▀            ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀      \n")
    print("\t\t                          ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄                                      ")
    print("\t\t                         ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌                                     ")
    print("\t\t                         ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌░▌     ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌                                     ")
    print("\t\t                         ▐░▌          ▐░▌          ▐░▌▐░▌    ▐░▌▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌                                     ")
    print("\t\t                         ▐░▌ ▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌ ▐░▌   ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌                                     ")
    print("\t\t                         ▐░▌▐░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░▌       ▐░▌▐░░░░░░░░░░░▌                                     ")
    print("\t\t                         ▐░▌ ▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌   ▐░▌ ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀ ▐░█▀▀▀▀▀▀▀█░▌     ▐░▌     ▐░▌       ▐░▌▐░█▀▀▀▀█░█▀▀                                      ")
    print("\t\t                         ▐░▌       ▐░▌▐░▌          ▐░▌    ▐░▌▐░▌▐░▌          ▐░▌     ▐░▌  ▐░▌       ▐░▌     ▐░▌     ▐░▌       ▐░▌▐░▌     ▐░▌                                       ")
    print("\t\t                         ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌     ▐░▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌ ▐░▌       ▐░▌     ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░▌      ▐░▌                                      ")
    print("\t\t                         ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░▌       ▐░▌                                     ")
    print("\t\t                          ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀         ▀       ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀                                      \n")
    print("\n\n", "\t"*11 , "START(s)\n", "\t"*11 , "ABOUT(a)\n", "\t"*11, "INSTRUCTIONS(i)\n", "\t"*11, "QUIT(q)","\n"*14, "\t"*11, "Project done by:\n", "\t"*11, "Advik Giridhar & \n", "\t"*11, "Aravind Krishnan A")
    choice = input()
    if choice == 's':
        os.system("cls") 
        #try:
        main_prog()
        #except:
            #print("invalid input")
        #print("hello")
        
        cont()
    elif choice == 'a':
        os.system("cls") 
        print("ABOUT\n\nThis program is written by Advik Giridhar and Aravind Krishnan A as a part of our 12th grade computer project\nwe would like to extend our gratitude to Mrs. Rashmi, our computer teacher for this wonderful learning experience\nA special thanks to Sindhi High School and the CBSE Board for encouraging projects like this\nCreating this project was a really fun journey and was hardly an easy one to complete.So we hope you enjoy using this generator")
        print("\n\nBIBLIOGRAPHY:\n\n>stackverflow.com\n>quora.com\n>patorjk.com\n")
        b = input("WOULD YOU LIKE TO GO BACK?(y/n): ")
        if b == 'y':
            front_screen()
        else:
            sys.exit()
    elif choice == 'i':
        os.system("cls") 
        print("HOW TO OPERATE:\n\n1.Once you have entered 's' to start the generator you will see the following:\n\n\tenter a prefix:\n\nThis is where you must enter a chemical chain prefix of your choice but always with the position like so:\n\n\tenter a prefix: 1,2-dichloro\n\n2.This prompt will continue to appear so that you can enter multiple prefxes. Once you are done entering prefixes simply enter 'n'\n\n3.the next prompt will appear asking for the carbon chain and suffix like so:\n\n\tenter carbon chain and suffix:\n\n4.enter a carbon chain and suffix with upto 9 carbons with all positions mentiond.(No need to mention position if it is an alkane):\n\n\tenter carbon chain and suffix: butan-1,4-dioic acid\n\tenter carbon chain and suffix: oct-3,4-diene-7-ol")
        print("\n\nThis program does NOT support:\n>Cyclic compounds\n>Inorganic compounds\n>Esters and Ethers\n>Carbon chains with more than 9 carbons")
        print("\n\nHOPE YOU ENJOY USING THIS GENERATOR")
        b = input("\nWOULD YOU LIKE TO GO BACK?(y/n): ")
        if b == 'y':
            front_screen()
        else:
            sys.exit()
    elif choice == 'q':
        sys.exit()
    else:
        os.system("cls")
        front_screen()
          

def cont():
    c = input("WOULD YOU LIKE TO CONTINUE? (y/n): ")
    if c == 'y':
        front_screen()
    elif c=='n':
        sys.exit()
    else:
        cont()

#PART 0.1 standalone functions

def vertical_single_bond():
    l = ["    |     ", "    |     "]
    return l
def vertical_double_bond():
    l = ["    ||    ", "    ||    "]
    return l  

#PART 0.2 function for identification and shape of groups
def identify(attach):
    if attach == 2:
        l = ["  ", "--", "--"]
    elif attach == 3:
        l = ["__", "__", "__"]
    else:
        import mysql.connector as ms
        con = ms.connect( host = 'localhost', user = 'root', passwd = 'V1dyan1ketan', database = 'project12')
        cur = con.cursor()
        cur.execute('select * from identify_sql where attach = {}'.format("'"+attach+"'"))
        data = cur.fetchall()
        l = data[0][1:]
    return l


def main_prog():
    #PART 1.1: prefixes and their positions
    terminal_groups = ['oic acid', 'al', 'amide', 'oyl fluoride', 'oyl chloride', 'oyl bromide', 'oyl iodide']
    terminal_check = [False, False]
    prefix = input("Please Enter Prefix1: ")
    list_prefix = ['methyl', 'fluoro', 'bromo', 'chloro', 'iodo', 'ethyl', 'propyl', 'butyl', 'pentyl', 'hexyl', 'heptyl', 'octyl', 'nonyl', 'cyano', 'oxo', 'sulpho']

    valid_prefix = False
    for a in list_prefix:
        if a in prefix or prefix == 'n':
            valid_prefix = True
    if valid_prefix == False:
        print("**INVALID INPUT**")
        cont()
    
    #parallel lists
    pre_pos = []
    pre_grp = []

    while prefix != 'n':
        pre_count = 0
        group = ''
    
        for a in prefix:
            if a.isdigit():
                pre_pos.append(int(a))
                pre_count += 1
            if a.isalpha():
                group += a
        for g in list_prefix:
            if g in group:
                #specific exception (the word 'ethyl' lies in the word 'methyl') 
                if g == 'ethyl' and 'm' in group:
                    group = 'methyl'
                elif g == 'ethyl' and 'm' not in group:
                    group = 'ethyl'
                else:
                    group = g
        for i in range(pre_count):
            pre_grp.append(group)
        
        prefix = input("Please Enter Prefix: ")

        valid_prefix = False
        for a in list_prefix:
            if a in prefix or prefix == 'n':
                valid_prefix = True
        if valid_prefix == False:
            print("**INVALID INPUT**")
            cont()
    #PART 1.2 : carbon chain, bond type and their positions
    bond_type_lst = ['an', 'en', 'yn']
    main = input("Please Enter Carbon Chain and Suffix: " )
    valid_main = False
    for a in bond_type_lst:
        if a in main:
            valid_main = True
    if valid_main == False:
        print("**INVALID INPUT** : NO BOND TYPE specifications")
        cont()
    #PART 1.2.1 Handling special single carbon compounds
    ter_meth = False
    if main == 'methan-1-al':
        if len(pre_grp) == 0:
            l = ["        __        __  ", "|__|__ /  ` |__| /  \ ", "|  |   \__, |  | \__/ "]
            ter_meth = True
        else:
            print("**INVALID NAME**")
            cont()
    elif main == 'methan-1-oic acid':
        if len(pre_grp) == 0:
            l = ["        __   __   __       ", "|__|__ /  ` /  \ /  \ |__| ", "|  |   \__, \__/ \__/ |  | "]
            ter_meth = True
        else :
            print("**INVALID NAME**")
            cont()
    elif main == 'methan-1-amide':
        if len(pre_grp) == 0:
            l = ["        __   __            ", "|__|__ /  ` /  \ |\ | |__| ", "|  |   \__, \__/ | \| |  |2"]
            ter_meth = True
        else :
            print("**INVALID NAME**")
            cont()
    elif main == 'methan-1-oyl fluoride':
        if len(pre_grp) == 0:
            l = ["        __   __   ___ ", "|__|__ /  ` /  \ |__  ", "|  |   \__, \__/ |    "]
            ter_meth = True
        else :
            print("**INVALID NAME**")
            cont()
    elif main =='methan-1-oyl chloride':
        if len(pre_grp) == 0:
            l = ["        __   __   __    ", "|__|__ /  ` /  \ /  ` | ", "|  |   \__, \__/ \__, | "]
            ter_meth = True
        else :
            print("**INVALID NAME**")
            cont()
    elif main == 'methan-1-oyl bromide':
        if len(pre_grp) == 0:
            l = ["      __   __   __    ", "|__| /  ` /  \ |__) __", "|  | \__, \__/ |__)| "]
            ter_meth = True
        else :
            print("**INVALID NAME**")
            cont()
    elif main == 'methan-1-oyl iodide':
        if len(pre_grp) == 0:
            l = ["        __   __    ", "|__|__ /  ` /  \ | ", "|  |   \__, \__/ | "]
            ter_meth = True
        else :
            print("**INVALID NAME**")
            c = input("WOULD YOU LIKE TO CONTINUE? (y/n): ")
            cont()

    if ter_meth :
        for i in range(3):
            print('\t\t', l[i])
        cont()

    c_chain_lst = ['meth', 'eth', 'prop', 'but', 'pent', 'hex', 'hept', 'oct', 'non']
    c_chain = ''
    for a in c_chain_lst:
        if a in main:
            if 'meth' in main:
                c_chain = 'meth'
            else:
                c_chain = a

    no_c_chn = ''
    for i in range(len(c_chain),len(main)):
        no_c_chn += main[i]

    Mbond_type = 0
    bond_pos1 = {}
    for a in bond_type_lst:
        if a in no_c_chn:
            Mbond_type = (bond_type_lst.index(a))+1

    if Mbond_type == 2 or Mbond_type == 3:
        dash_c = 0
        c1 = 0
        while dash_c != 2:
            if no_c_chn[c1] == '-':
                dash_c += 1
            elif no_c_chn[c1].isdigit():
                bond_pos1[int(no_c_chn[c1])] = Mbond_type
            c1 += 1

    #PART 1.3: functional group and its position

    fn_group_lst = ['ol', 'al', 'oic acid', 'one', 'amide', 'nitrile', 'amine', 'onic acid' 'oyl fluoride', 'oyl chloride', 'oyl bromide', 'oyl iodide']
    fnc_grp = ''
    if no_c_chn[-3:] not in 'aneneyne': #compound has a functional group
        flag = False
        for a in no_c_chn:
            if a == 'n':
                flag = True
            if flag == True:
                fnc_grp += a

    fnc_grp1 = ''
    for a in fn_group_lst:
        if a in fnc_grp:
            fnc_grp1 = a
            if fnc_grp1 in terminal_groups:
                if not terminal_check[0]:
                    terminal_check[0] = True
                if '-di' in fnc_grp:
                    terminal_check[1] = True

    n_carbon = c_chain_lst.index(c_chain) + 1
    if fnc_grp != '':
        c = 0
        for a in fnc_grp:
            if a.isdigit():
                if fnc_grp1 in terminal_groups:
                    if c == 0:
                        for i in range (len(pre_pos)):
                            pre_pos[i] -= 1
                    print(a)
                    if a == '1' or a == str(n_carbon):
                        pass
                    else:
                        print("TERMINAL GROUPS can only be present in TERMINAL POSITIONS: ")
                        cont()
                    c+=1
                if c == 2:
                    pre_pos.append(int(a)-2)
                    c+=1
                else:
                    pre_pos.append(int(a))
                pre_grp.append(fnc_grp1)

    #PART 1.4 accounting for terminal groups
    for i in range(2):
        if terminal_check[i]:
            c_chain = c_chain_lst[c_chain_lst.index(c_chain) - 1]
    bond_pos = {}
    if terminal_check[0]:
        for a in bond_pos1.keys():
            bond_pos[a-1] = bond_pos1[a]
    else:
        bond_pos = bond_pos1
    n_carbon = c_chain_lst.index(c_chain) + 1
    #PART 1.5 adding hydrogens in available spaces

    #n_carbon = c_chain_lst.index(c_chain) + 1
    ketone_pos = []
    for i in range(1,n_carbon+1):
        
        if i == 1 :
            if i in bond_pos.keys():
                bond_type = bond_pos[i]
            else:
                bond_type = 1
            c = 0
            for a in pre_pos:
            
                if a == i:
                    for j in range(len(pre_grp)):
                        if pre_pos[j] == a and (pre_grp[j] == 'one' or pre_grp[j] == 'oxo'):
                            print("**INVALID INPUT** : Ketone cannot occupy TERMINAL POSITION")
                            cont()
                    c += 1
            no_of_hydrogens = 4-bond_type-c
            if c_chain == 'meth':
                no_of_hydrogens+=1
            if no_of_hydrogens < 0:
                print("**INVALID NAME**")
                cont()
            else:
                for j in range(no_of_hydrogens):
                    pre_pos.append(i)
                    pre_grp.append('h')

        elif i == n_carbon:
            if i-1 in bond_pos.keys():
                bond_type = bond_pos[i-1]
            else:
                bond_type = 1
            c = 0
            for a in pre_pos:
            
                if a == i:
                    for j in range(len(pre_grp)):
                        if pre_pos[j] == a and (pre_grp[j] == 'one' or pre_grp[j] == 'oxo'):
                            print("**INVALID INPUT** : Ketone cannot occupy TERMINAL POSITION")
                            cont()
                    c += 1
            no_of_hydrogens = 4-bond_type-c

            if no_of_hydrogens < 0:
                print("**INVALID NAME**")
                cont()
            else:
                for j in range(no_of_hydrogens):
                    pre_pos.append(i)
                    pre_grp.append('h')
    
  
        else:
            if i in bond_pos.keys():
                bond_type = bond_pos[i]
            else:
                bond_type = 1
            if i-1 in bond_pos.keys():
                bond_type += bond_pos[i-1]
            else:
                bond_type +=1
            c = 0
            for a in range(len(pre_pos)):
                b = pre_pos[a]
                if b == i:
                    if pre_grp[a] == 'one' or pre_grp[a] == 'oxo':
                        c += 2
                        ketone_pos.append(b)
                    else:
                        c += 1
            no_of_hydrogens = 4-bond_type-c
            if no_of_hydrogens < 0:
                print("**INVALID NAME**")
                cont()
            else:
                for j in range(no_of_hydrogens):
                    pre_pos.append(i)
                    pre_grp.append('h')

    pre_pos2, pre_grp2 = pre_pos, pre_grp #backup lists

    #PART 2.1 First row of the structure

    #PART 2.1.1 building row dictionary

    print("\n\n\n")
    row1 = {}
    for i in range(1,n_carbon+1):
        if i in pre_pos2:
            index = pre_pos2.index(i)
            if pre_grp2[index] in terminal_groups:
                if i not in pre_pos2[index+1:]:
                    row1[i] = '*'
                    continue
                else:
                    index = pre_pos2.index(i,index+1,len(pre_grp2)+1)

            row1[i] = pre_grp2[index]
            pre_pos2.pop(index)
            pre_grp2.pop(index)
        else:
            row1[i] = '*'

    #PART 2.1.2 printing attachments
    for i in range(3):
        c = 1
        print(" "*23, end ='')
        for j in range(n_carbon):
            l1 = identify(row1[c])
            print(l1[i], end = '')
            c+=1
        print()

    #PART 2.1.3 printing bonds below the above groups
    for i in range(2):
        print(" "*23, end ='')
        for j in range(1, n_carbon+1):
            if row1[j] != '*':
                if j in ketone_pos:
                    if i == 1:
                        ketone_pos.pop(ketone_pos.index(j))
                    l = vertical_double_bond()
                else:
                    l = vertical_single_bond()
                print(l[i], end = '')
            else:
                print("          ", end = '')
        print()

    #PART 2.2 Second row of the structure

    #PART 2.2.1 building row dictionary
    row2 = {}

    c1 = 1
    for i in range(1,2*(n_carbon+2)):
        if i == 1 :
            if i in pre_pos2:
                row2[1] = pre_grp2[pre_pos.index(1)]
                if row2[1] not in terminal_groups:
                    row2[0] = 'terminal_space'
                else:
                    row2[0] = 'nothing'
                index = pre_pos2.index(1)
                pre_pos2.pop(index)
                pre_grp2.pop(index)
            else:
                row2[1] = '*'
                row2[0] = 'terminal_space'
            continue
    
        if i == 2*n_carbon +3 :
            j = n_carbon
            if j in pre_pos2:
                row2[i] = pre_grp2[pre_pos.index(j)]
                index = pre_pos.index(j)
                pre_pos2.pop(index)
                pre_grp2.pop(index)
            else:
                row2[i] = '*'
            continue
    
        if i == 2 or i == 2*n_carbon+2:
            if i-1 not in pre_pos and i == 2:
                row2[i] = ''
            elif (i/2)-1 not in pre_pos and i == 2*n_carbon+2:
                row2[i] = ''
            else:
                row2[i] = 'horizontal_single_bond'
            continue
    
        elif i % 2 == 1:
            row2[i] = 'carbon'
        elif i % 2 == 0:
            pos = i - 2 - c1
            if pos not in bond_pos.keys():
                row2[i] = 'horizontal_single_bond'
            else :
                row2[i] = bond_pos[pos]
            c1 += 1
    #print(row2)
    #PART 2.2.2 printing row2
    for i in range(3):
        c = 0
        for j in range(2*(n_carbon+2)):
            l = identify(row2[c])
            print(l[i], end = '')
            c+=1
        print()
        
    #PART 2.3 Third row of the structure

    #PART 2.3.1 Building row dictionary


    row3 = {}
    for i in range(1,n_carbon+1):
        if i in pre_pos2:
            index = pre_pos2.index(i)
            if pre_grp2[index] in terminal_groups:
                if i not in pre_pos2[index+1:]:
                    row3[i] = '*'
                    continue
                else:
                    index = pre_pos2.index(i,index+1,len(pre_grp2)+1)

            row3[i] = pre_grp2[index]
            pre_pos2.pop(index)
            pre_grp2.pop(index)
        else:
            row3[i] = '*'

    #PART 2.3.2 Printing bonds above third row groups
    for i in range(2):
        print(" "*23, end ='')
        for j in range(1, n_carbon+1):
            if row3[j] != '*':
                if j in ketone_pos:
                    ketone_pos.pop(index(j))
                    l = vertical_double_bond()
                else:
                    l = vertical_single_bond()
                print(l[i], end = '')
            else:
                print("          ", end = '')
        print()

    #PART 2.3.3 Printing Third row groups

    for i in range(3):
        c = 1
        print(" "*23, end ='')
        for j in range(n_carbon):
            l = identify(row3[c])
            print(l[i], end = '')
            c+=1
        print()

#actual execution
front_screen()


            

