meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            }
for i in range (5) :
    word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
    word = word.upper()
    if word in meme_dict.keys() :
        print("anlamı :",meme_dict[keys])
    else:
        ("kelime haznemde yok")
