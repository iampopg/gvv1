from colorama import init, Fore
import requests, random, re, sys ,os, time, platform
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from pyfiglet import figlet_format

init(autoreset=True)

red = Fore.RED
green = Fore.GREEN
yellow= Fore.YELLOW
mag = Fore.MAGENTA
white= Fore.WHITE
blue = Fore.BLUE




# for validating numbers 
def numberValidator(number, name):
    
    if number.startswith('+'):
        number = number[1:]
        
    
    url = 'https://login.microsoftonline.com/common/GetCredentialType?mkt=en-US'

    payload_template = {
        "isOtherIdpSupported": True,
        "checkPhones": False,
        "isRemoteNGCSupported": True,
        "isCookieBannerShown": False,
        "isFidoSupported": True,
        "country": "US",
        "forceotclogin": False,
        "isExternalFederationDisallowed": False,
        "isRemoteConnectSupported": False,
        "federationFlags": 0,
        "isSignup": False,
        "flowToken": "AQABAAEAAAAtyolDObpQQ5VtlI4uGjEPmVTvB5eZTaL_xvRdNX8zoF_M9oCPfpR1_3-Wz9ETrDbl5ca9Avq0LYJkoyoMgY5LIhrw_zFYKZPKDynsKoHPZfgeKmWiIAs1DXbLOrj1FwddvGzTm1ABWqIWhpNkryjIGv9-pljgbUnhPWj9pTn9ffvUpp8V2MtaAhrj46pyDne0WQmgpo5yxrOcie6NRDmX-vIRN1MIuXjLJ27VP51D0OM2hEp1OD47P6dtU6fk3-n2oCqUh1nP1tJCP1Pr47Uw2d3Hx3uCPYHHQJ8S3DkYwNqi4ieYGWQoRIaGrswGKuHiQRsyIuf8jtXEVXyOGqJhVIrV13orhsMe8QFdNAQE95yTcr7oSV6cXL7EWJdelszMsPUosCWSNdpwVI3lFGrKkYHetSaT2PrQem5AJIKBpKpvdLzk4q_P1P5_HA5hrOLCjH451cW4GJ2aVLL8wejgiEdppAzICHiHJOAthyGUP1R7w0z62wD6Ml9QOrRuqGS1KRxOCycJSUhLQcXDX5yIL1PCokaNJIAca5y1wkJb4zMbwhsGoVaUnWZK8XjTWYovsLqEn1dvUW_GrQxdQzwyIAA",
        "isAccessPassSupported": True,
        "username": number
    }


    headers = {
        "Host": "login.microsoftonline.com",
        # (other headers here)
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "close"
    }

    response = requests.post(url,headers=headers,json=payload_template)
    x = response.json()
    # print(x)
    if_exists_result = x["IfExistsResult"]

    if if_exists_result == 5 or if_exists_result == 0:
        print (f'{mag}==> Valid.....{green}{number}')
        save(number,name)
        
    else:
        print (f'{mag}==> Invalid...{red}{number}')
        
# numberValidator('sawdyk12d3@gmail.com')

#Generating 150,000 numbers
def numberGenerator(name, number):
    try:
        
        code = code_list
        print('Generating leads, please hold ....')
        
        if len(code) == 1:  # If the length of the country code is 1
            if number.startswith('0'):
                for i in range(100000):
                    if len(number) == 3:
                        starting = int(number + "000000")
                        ending = int(number + "999998")
                    elif len(number) == 4:
                        starting = int(number + "00001")
                        ending = int(number + "99998")
                    elif len(number) == 1:
                        starting = int(number + "00000000")
                        ending = int(number + "99999998")
                    elif len(number) == 2:
                        starting = int(number + "0000000")
                        ending = int(number + "9999998")
                    else:
                        print("Invalid length of 'number'")
                        return
                    
                    number1 = random.randint(starting, ending)
                    original = '+' + code + '0' +str(number1)
                    save(original, name)
            else:
                for i in range(100000):
                    if len(number) == 3:
                        starting = int(number + "0000000")
                        ending = int(number + "9999998")
                    elif len(number) == 4:
                        starting = int(number + "000001")
                        ending = int(number + "999998")
                    elif len(number) == 1:
                        starting = int(number + "000000000")
                        ending = int(number + "999999998")
                    elif len(number) == 2:
                        starting = int(number + "00000000")
                        ending = int(number + "99999998")
                    else:
                        print("Invalid length of 'number'")
                        return
                    
                    number1 = random.randint(starting, ending)
                    original = '+' + code + str(number1)
                    save(original, name)
        
        elif len(code) == 2:  # If the length of the country code is 2
            if number.startswith('0'):
                for i in range(100000):
                    if len(number) == 3:
                        starting = int(number + "00000")
                        ending = int(number + "99998")
                    elif len(number) == 4:
                        starting = int(number + "0001")
                        ending = int(number + "9998")
                    elif len(number) == 1:
                        starting = int(number + "0000000")
                        ending = int(number + "9999998")
                    elif len(number) == 2:
                        starting = int(number + "000000")
                        ending = int(number + "999998")
                    else:
                        print("Invalid length of 'number'")
                        return
                    
                    number1 = random.randint(starting, ending)
                    original = '+' +code + '0'+str(number1)
                    save(original, name)
            else:
                for i in range(100000):
                    if len(number) == 3:
                        starting = int(number + "000000")
                        ending = int(number + "999998")
                    elif len(number) == 4:
                        starting = int(number + "00001")
                        ending = int(number + "99998")
                    elif len(number) == 1:
                        starting = int(number + "00000000")
                        ending = int(number + "99999998")
                    elif len(number) == 2:
                        starting = int(number + "0000000")
                        ending = int(number + "9999998")
                    else:
                        print("Invalid length of 'number'")
                        return
                    
                    number1 = random.randint(starting, ending)
                    original = '+' +code + str(number1)
                    save(original, name)
        elif len(code) == 3:  # If the length of the country code is 3
            if number.startswith('0'):
                for i in range(100000):
                    if len(number) == 3:
                        starting = int(number + "0000")
                        ending = int(number + "9998")
                    elif len(number) == 4:
                        starting = int(number + "001")
                        ending = int(number + "998")
                    elif len(number) == 1:
                        starting = int(number + "000000")
                        ending = int(number + "9999998")
                    elif len(number) == 2:
                        starting = int(number + "00000")
                        ending = int(number + "99998")
                    else:
                        print("Invalid length of 'number'")
                        return
            else:
                for i in range(100000):
                    if len(number) == 3:
                        starting = int(number + "00000")
                        ending = int(number + "99998")
                    elif len(number) == 4:
                        starting = int(number + "0001")
                        ending = int(number + "9998")
                    elif len(number) == 1:
                        starting = int(number + "0000000")
                        ending = int(number + "9999998")
                    elif len(number) == 2:
                        starting = int(number + "000000")
                        ending = int(number + "999998")
                    else:
                        print("Invalid length of 'number'")
                        return
                    
                    number1 = random.randint(starting, ending)
                    original = '+' +code + str(number1)
                    save(original, name)
        
        print("Done generating leads.")
        
    except Exception as e:
        print(f"An error occurred: {e}")


# to save 
def save(number, name):
    with open(name, 'a') as save:
        save.write(f"{number}\n")
        

def get_file_path():
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    file_path = askopenfilename(filetypes=[("Text Files", "*")],title="Select File to Validate")
    root.destroy()
    return file_path

# countries selection 
def countries():
    print()
    print('''
        SELECT A COUNTRY
          [1]   United Stated (+1)
          [2]   Canada (+1)
          [3]   Austrailia (+61)
          [4]   United Kinddom (+44)
          [5]   Ireland (+353)
          [0]   Back to the main menu
          ''')
    country = input(": ").strip()
    while country not in ['1', '2', '3', '4', '5', '0']:
            print(red + 'Enter between 0-5, check the option above')
            option = input("Enter an option: ").strip()
    if country == '1' or country == '2':
        code = '1'
        
    elif country == '3':
        code = '61'
        
    elif country == '4':
        code = '44'    
    
    elif country == '5':
        code = '353'
        
    elif country == '0':
        run()
    codes = code
    return codes 


def run():
    try:
        x = 1
        if platform.system() == 'Windows':
            os.system('cls')
        elif platform.system() == 'Linux':
            os.system('clear')
            
        print()
        print(yellow+ figlet_format('G & V', font='standard', width = 100))
        print(f""" {green}Generator and Validator v1
                            
                            {white}Coded by Pop(G)
                            {red}telegram: https:t.me/iampopg
                            
        """)
        print()
        if not os.path.exists('result'):
            os.makedirs('result')
        print(f"""
            
            {yellow} [1] {mag}Generate number leads
            {yellow} [2] {mag}Validate leads
            {yellow} [3] {mag}Generate and validate
            {yellow} [4] {mag}Exit
            
            """)
    
        option = input(f"{yellow}Enter an option: ").strip()
       
        while option not in ['1', '2', '3', '4']:
            print(red + 'Enter between 1-4, check the option above')
            option = input("Enter an option: ").strip()
            
         # for generate 
         
        if option == '1' or option == '3':
            global code_list
            code_list = countries()
            
        if option == '1':
            
            print(f'{yellow}Enter the first 1-4 length of starting number of your target without country code {green}+{code_list}*****  {yellow}e.g 5 or 51 or 513 or 5134)')
            target = input(": ").strip()
            
            if target.startswith('+'):
                print('No Country code, just starting number')
                time.sleep(1)
                sys.exit()
                
            if len(target) in [1,2,3,4]:
                output = input(yellow + "Enter name to save the generated number: ").strip()
                if not output.endswith('.txt'):
                    output= output+".txt"
                # output = 'result/' + output
                numberGenerator(output,target)
                print()
                input(f"{mag}Done and saved to {green}{output}")
                run()
            else: 
                print()
                print(f"I repeate, Enter {red}Enter the first 3/4 starting number of your target without +1(e.g 513 or 5134) ")
                time.sleep(3)
                sys.exit()
        
        # for validate
        elif option == '2':
            print()
            print("MAKE SURE YOU ARE CONNECTED TO INTERNET")
            print()
            name = input("Enter name to save the validate numbers: ")
            name = "result/" + name
            print(yellow + "Now Select file to validate")
            time.sleep(1)
            number_list = get_file_path()  # Use the drag-and-drop function
            with open(number_list, 'r') as read:
                numbers = read.readlines()
                with ThreadPoolExecutor(max_workers=64) as executor:
                    executor.map(lambda number: numberValidator(number.strip(), name), numbers)
            input(f"{mag}Valid numbers saved to {green} {name}")
            run()
        
        
        # for generate and validate
        elif option == '3':
            print()
            print("MAKE SURE YOU ARE CONNECTED TO INTERNET")
            print()
            print(f'{yellow}Enter the first 1-4 length of starting number of your target without country code {green}+{code_list}*****  {yellow}e.g 5 or 51 or 513 or 5134)')
            target = input(": ").strip()
            if target.startswith('+'):
                print('No Country code, just starting number')
                time.sleep(1)
                sys.exit()

            if len(target) in [1,2,3,4]:
                output = input(yellow + "Enter name to save the generated number: ").strip()
                if not output.endswith('.txt'):
                    output= output+".txt"
                valid = input(f'{yellow}Enter name to save the Validated number: ').strip()
                valid = 'result/' + valid
                numberGenerator(output,target)
                print()
                print(f"{mag}Done generating and generated number saved to {green}{output}")
                time.sleep(1)
                print(f"{mag}Starting to Validate .....")
                time.sleep(2)
                
                with open(output, 'r') as read:
                    numbers = read.readlines()
                    with ThreadPoolExecutor(max_workers=100) as executor:
                        executor.map(lambda number: numberValidator(number.strip(), valid), numbers)
                input(f"{mag}Valid numbers saved to {green} {valid}")
                run()
                
                
            else: 
                print()
                print(f"I repeate, Enter {red}Enter the first 3/4 starting number of your target without +1(e.g 513 or 5134) ")
                time.sleep(3)
                sys.exit()
                
        elif option == '4':
            print("Thanks for you time")
            time.sleep(2)
            sys.exit()
        
        
        else:
            sys.exit()
            
    except ValueError as e:
        print(f"{red}You are only allow to Enter number:")
        time.sleep(3)
        sys.exit()
    
    except FileNotFoundError:
        print()
        print(f"{red} File not found... Dont forget to put .txt if it's a text file")
    except KeyboardInterrupt:
        print()
        print()
        print("Thanks for you time")
        time.sleep(2)
    except ImportError:
        print(red + 'Colorama or request not found installed on your system')
        print()
        print('Installing now ...')
        time.sleep(1)
        os.system(f"pip install requests")
        os.system(f"pip install colorama")
        print('Done installing, please run the program again, Thanks')
        time.sleep(1)
        sys.exit()
        
run()