import subprocess
import os
import argparse

def getVTReport(APIkey, target, result, premium):
    path = os.path.dirname(os.path.abspath(__file__))
    command = f'{path}\\VTReport.ps1 -apikey "{APIkey}" -target "{target}" -result "{result}" -premium "{premium}"'
    PSline = "powershell -ExecutionPolicy ByPass -File "

    subprocess.check_output(PSline + command)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=' ',formatter_class=argparse.
                                RawDescriptionHelpFormatter)
    parser.add_argument("-api", metavar='apikey', dest="APIkey", required=True)
    parser.add_argument("-target", metavar='Target', dest="target", required=True)
    parser.add_argument("-result", metavar='Result', dest="result")

    APIkey = parser.parse_args().APIkey
    target = parser.parse_args().target
    result = parser.parse_args().result

    getVTReport(APIkey, target, result)

