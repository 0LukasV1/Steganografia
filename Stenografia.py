from PIL import Image

obr = Image.open("krajina.jpg")
obr2 = Image.open("krajina.jpg")
pixels = obr.load()
pixels2 = obr2.load()
farba = []
farba2=[]
sirka = obr.size[0]
vyska = obr.size[1]

def oddrticka(obr,obr2):
    sprava = ""
    konecec= []
    konececec=""
    konec = ""
    dlzka = 0
    for i in range(0,sirka):
        dlzka += 1
        x = i % sirka
        y = i // sirka
        farba = pixels[x, y]
        farba2 = pixels2[x, y]
        if "00100011" in sprava:
            break
        else:
            if farba[2] != farba2[2] and farba[2]%2 != 0:
                sprava += "1"
            elif farba[2] != farba2[2] and farba[2] % 2 == 0:
                sprava += "0"
            elif farba[2] == farba2[2] and farba[2]%2 != 0:
                sprava  += "1"
            elif farba[2] == farba2[2] and farba[2] % 2 == 0:
                sprava += "0"
    konec = str(sprava.zfill(dlzka - 1))
    n = 8
    konecec = [konec[i:i + 8] for i in range(0, len(konec), 8)]
    print(*konecec)


oddrticka("obrsospr.png","obrsospr2.png")
