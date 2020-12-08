## PIA PROGRA

1. Instalar requirements.txt
2. Correr "python PIA.py -h"

### Correr PIA.py

1. Saber que herramienta usar
2. Dependiendo de la herramienta, la opcion a utilizar: vtreport, metadata, cipher, nmap, hunter
3. python PIA.py -opt ___herramienta___

### Modulo Hunter

1. Tener tu api de hunter.io
2. Correr python PIA.py -opt hunter -a ___apikey___ -c ___compañia___ -n ___numero de correos___

### Modulo VTReport

1. Tener tu api de virustotal
2. Saber tu carpeta target y el archivo de los resultados
3. Correr python PIA.py -opt vtreport -a ___apikey___ -t ___target___ -r ___resultados___ -p ___(solo si tienes premium)___

### Modulo Metadata

1. Tener tu folder con fotos a escanear
2. Correr python PIA.py -opt metadata -p ___path folder___

### Modulo Cipher

1. Saber si quieres encriptar o desencriptar
2. Encriptar usar -en, desencriptar usar -de
3. python PIA.py -opt cipher -de ___frase___ o python PIA.py -opt cipher -en ___frase___

### Modulo Nmap

1. Saber tu ip
2. Dar un inicio y un fin para escanear loss puertos
3. Correr python PIA.py -opt nmap -ip ___ip___ -in ___inicio___ -fi ___fin___