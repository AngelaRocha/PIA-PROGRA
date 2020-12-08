import nmap
import os
import logging
import socket

def Escaneo(ip,inicio,fin):
    lPath = os.path.dirname(os.path.abspath(__file__))
    scanner = nmap.PortScanner()
    if ip.upper() == 'LOCAL':
        target = socket.gethostbyname(socket.gethostname()) + '/24'
        scanner.scan(target)
        f = open(f'{lPath}\\resultados.csv', 'w+')
        f.write(scanner.csv())
        f.close()
    else:
        final = fin + 1
        for i in range(inicio,final):
            res = scanner.scan(ip, str(i))
            res = res['scan'][ip]['tcp'][i]['state']
            print(f'the port {i} is {res}.')


if __name__ == '__main__':
    import nmap
    import os
    import logging
    try:
        import nmap
        ip =(input("Introduce Tu Ip: "))
        inicio = int(input("Introduce El Puerto Incial: "))
        fin = int(input("Introduce El  Puerto Final: "))
        print(Escaneo(ip,inicio,fin))
    except ImportError:
        logging.info('Modulo de Nmap')
        os.system('pip install python-nmap')
        logging.error("No se tiene instalado el modulo nmap")
        print('Installing nmap...')
        print('Ejecuta de nuevo tu script...')
        exit()
