def testaPudim():
    import requests
    from time import sleep
    while True:
        #sleep(1)
        try:
            teste = requests.get('http://pudim.com.br')
        
        except Exception as erro:
            print(f'\n\n\033[31mO Site Pudim está Offline  =(\033[m \n\n')
        
        else:
            print(f'\n\033[32mO site Pudim está Online =D\033[m\n\n')


############
testaPudim()