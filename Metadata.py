from PIL import Image, ImageFilter
from PIL.ExifTags import TAGS, GPSTAGS
import os

def decode_gps_info(exif):
    gpsinfo = {}
    if 'GPSInfo' in exif:
        #Parse geo references.
        Nsec = exif['GPSInfo'][2][2] 
        Nmin = exif['GPSInfo'][2][1]
        Ndeg = exif['GPSInfo'][2][0]
        Wsec = exif['GPSInfo'][4][2]
        Wmin = exif['GPSInfo'][4][1]
        Wdeg = exif['GPSInfo'][4][0]
        if exif['GPSInfo'][1] == 'N':
            Nmult = 1
        else:
            Nmult = -1
        if exif['GPSInfo'][3] == 'E':
            Wmult = 1
        else:
            Wmult = -1
        Lat = Nmult * (Ndeg + (Nmin + Nsec/60.0)/60.0)
        Lng = Wmult * (Wdeg + (Wmin + Wsec/60.0)/60.0)

def get_exif_metadata(image_path):
    ret = {}
    image = Image.open(image_path)
    if hasattr(image, '_getexif'):
        exifinfo = image._getexif()
        if exifinfo is not None:
            for tag, value in exifinfo.items():
                decoded = TAGS.get(tag, tag)
                ret[decoded] = value
    decode_gps_info(ret)
    return ret

def PrintMeta(dire):
    print("\n-------------Ruta de imágenes: "+dire+"-------------\n")
    os.chdir(dire)
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            print('\n',os.path.join(root, name))
            print ("[+] Metadata for file: %s \n" %(name))
            try:
                exifData = {}
                exif = get_exif_metadata(name)
                for metadata in exif:
                    print ("Metadata: %s - Value: %s " %(metadata, exif[metadata]))
                print ("\n")
            except:
                import sys, traceback, PIL
                traceback.print_exc(file=sys.stdout)

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-dp', help='Ingresar path de la carpeta donde hay multiples fotos')
    args = parser.parse_args()
    if args.dp:
        PrintMeta(args.dp)
    else:
        print(parser.usage)

if __name__ == '__main__':
    try:
        from PIL.ExifTags import TAGS, GPSTAGS
        from PIL import Image, ImageFilter
        import argparse
        Main()
    except ImportError:
        import os
        print("Error on Packages","Installing Packages")
        os.system('pip install -r requierements.txt')
        print("Packages Installed","ReRun")
        exit()