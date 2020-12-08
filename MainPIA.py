import argparse
import logging

def Main():
    help1 = "Opcion para elegir script a utilizar.  [VTReport, Metadata, \
            Cipher, Nmap, Hunter]"
    info = 'PIA 2020'
    parser = argparse.ArgumentParser(info)
    parser.add_argument('-opt', '--option', required = True, help = help1,
                        dest = 'opt')
    parser.add_argument('-a', '--api', help = 'Agrega tu API key.')
    parser.add_argument('-c', '--company', help = 'Nombre de la compañía.')
    parser.add_argument('-n', '--numero', help = 'Numero de correos (Maximo 10\
                        si tienes plan gratuito).')
    parser.add_argument('-ip', '--ip',type=str, help = 'Ingresar ip para \
                        escaneo con nmap.')
    parser.add_argument('-in', '--inicio',type=int, help = 'Primer puerto \
                        a analizar.')
    parser.add_argument('-fi', '--fin',type=int, help = 'Ultimo puerto a \
                        analizar.')
    parser.add_argument('-en', '--encriptar', help = 'Ingresar ip para escaneo \
                        con nmap.')
    parser.add_argument('-de', '--desencriptaar', help = 'Primer puerto a \
                        analizar.')
    parser.add_argument('-p', '--path', help = 'Ingresar direccion del path \
                        con las imagenes.')
    parser.add_argument('-t', '--target', help = 'Ingresar direccion absoluta\
                         del directorio con los archivos')
    parser.add_argument('-r', '--result', help = 'Ingresar direccion absoluta\
                        del arhivo de salida')
    parser.add_argument('-pre', '--premium', help = 'Ingresa "y" si tienes una api\
                        premium de VirusTotal, de lo contrario ignorarlo')
    
    args = parser.parse_args()

    if args.opt.upper() == 'VTREPORT':
        api = args.api
        target = args.target
        result = args.result
        premium = args.premium
        if premium==None:
            premium = 'n'
        PSExce.getVTReport(api, target, result, premium)

    if args.opt.upper() == 'METADATA':
        path = args.path
        Metadata.PrintMeta(path)

    if args.opt.upper() == 'CIPHER':
        if args.encriptar:
            frase = args.encriptar
            caesarsCipher.Encriptar(frase)
        if args.desencriptaar:
            frase = args.desencriptaar
            caesarsCipher.Desencriptar(frase)

    if args.opt.upper() == 'NMAP':
        ip = args.ip
        inicio = args.inicio
        fin = args.fin
        nmaPia.Escaneo(ip,inicio,fin)

    if args.opt.upper() == 'HUNTER':
        api = args.api
        company = args.company
        numero = args.numero
        huntermail.hunterio(api,company,numero)


if __name__ == '__main__':
    try:
        import nmapp
        import Metadata
        import huntermail
        import caesarsCipher
        import PSExce
        Main()
    except ImportError:
        logging.error('No se tienen instalados todos los modulos.')
        import os
        os.system('pip install -r requirements.txt')
        print("Módulos Instalados...","Ejecuta de nuevo")
        exit()
