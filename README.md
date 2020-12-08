## PIA PROGRA

1. Instalar requirements.txt
2. Correr "python PIA.py -h"

### Correr PIA.py

1. Saber que herramienta usar
2. Dependiendo de la herramienta, la opcion a utilizar: vtreport, metadata, cipher, nmap, hunter
3. python PIA.py -opt <herramienta>

### Modulo Hunter

1. Tener tu api de hunter.io
2. Correr python PIA.py -opt hunter -a <apikey> -c <compañia> -n <numero_de_correos>

### Modulo VTReport

1. Tener tu api de virustotal
2. Saber tu carpeta target y el archivo de los resultados
3. Correr python PIA.py -opt vtreport -a <apikey> -t <target> -r <resultados> -p (solo si tienes premium)

### Modulo Metadata

1. Tener tu folder con fotos a escanear
2. Correr python PIA.py -opt metadata -p <path_folder>

### Modulo Cipher

1. Saber si quieres encriptar o desencriptar
2. Encriptar usar -en, desencriptar usar -de
3. python PIA.py -opt cipher -de <frase> o python PIA.py -opt cipher -en <frase>

### Modulo Nmap

1. Saber tu ip
2. Dar un inicio y un fin para escanear loss puertos
3. Correr python PIA.py -opt nmap -ip <ip> -in <inicio> -fi <fin>