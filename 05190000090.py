import math

KUVVET_PUANI_YOK = 0  # oyuncunun kuvvet puani yoksa 0 alınır
MIN_KUVVET_PUANI = 1000  # oyuncunun kuvvet puani en az 1000 olabilir
MIN_MAC_SONUCU = 0  # maç sonucu en az 0 olabilir
MAX_MAC_SONUCU = 5  # maç sonucu en çok 5 olabilir
BEYAZ = 'b'
SIYAH = 's'


# her oyuncunun farklı olmak üzere lisans numaraları alınır. Hata kontrolü yapılır.
def lisans_numarasi_al(oyuncular):
    try:
        sonuc = False
        lisans_no = int(input("Oyuncunun lisans numarasini giriniz (bitirmek için 0 ya da negatif giriniz):"))
        for oyuncu in oyuncular:
            if lisans_no in oyuncu:
                sonuc = True
        if sonuc:
            lisans_no = lisans_numarasi_al(oyuncular)
    except ValueError:
        print("Hatalı veri türü girdiniz")
        lisans_no = lisans_numarasi_al(oyuncular)

    return lisans_no


# her oyuncunun adının alınması ve isimlerin türkçeyle uyumlu olarak büyük harfe çevrilmesi
def oyuncu_adini_al():
    oyuncu_adi = input("Oyuncunun adini-soyadini giriniz:")
    while oyuncu_adi == '':
        oyuncu_adi = input("Oyuncunun adini-soyadini giriniz:")
    oyuncu_adi = oyuncu_adi.replace('i', 'İ')
    buyuk_isim = oyuncu_adi.upper()

    return buyuk_isim


# her oyuncunun elo puanı alınır ve uygun veri girilmezse girilene kadar tekrar istenir. Hata kontrolü yapılır.
def oyuncu_elo_al():
    try:
        oyuncu_elo = int(input("Oyuncunun ELO’sunu giriniz (en az {min}, yoksa {yok}):".format(min=MIN_KUVVET_PUANI, yok=KUVVET_PUANI_YOK)))
        if oyuncu_elo != KUVVET_PUANI_YOK and oyuncu_elo < MIN_KUVVET_PUANI:
            oyuncu_elo = oyuncu_elo_al()
    except ValueError:
        print("Hatalı veri türü girdiniz")
        oyuncu_elo = oyuncu_elo_al()

    return oyuncu_elo


# her oyuncunun ukd puanı alınır ve uygun veri girilmezse girilene kadar tekrar istenir. Hata kontrolü yapılır.
def oyuncu_ukd_al():
    try:
        oyuncu_ukd = int(input("Oyuncunun UKD’sini giriniz (en az {min}, yoksa {yok}):".format(min=MIN_KUVVET_PUANI, yok=KUVVET_PUANI_YOK)))
        if oyuncu_ukd != KUVVET_PUANI_YOK and oyuncu_ukd < MIN_KUVVET_PUANI:
            oyuncu_ukd = oyuncu_ukd_al()
    except ValueError:
        print("Hatalı veri türü girdiniz")
        oyuncu_ukd = oyuncu_ukd_al()

    return oyuncu_ukd


# sıralanmış oyuncu bilgilerinin formatlanması ve yazdırılması
def oyuncu_bilgilerini_yazdir(oyuncular):
    sira_no = 1  # oyunculara başlangıç sıra numaraları verilie
    print("Başlangıç Sıralama Listesi:")
    print("BSNo     LNo   Ad-Soyad         ELO    UKD")
    print("----", "  -----", "  -------------", "  ----", "  ----")
    for oyuncu in oyuncular:
        oyuncu[1][0] = sira_no
        print(format(oyuncu[1][0], '4d'), end='   ')
        print(format(oyuncu[0], '5d'), end='   ')
        print(format(oyuncu[1][2], '13'), end='   ')
        print(format(oyuncu[1][3], '4d'), end='   ')
        print(format(oyuncu[1][4], '4d'))
        sira_no += 1


# Oyuncular, başlangıçta ve her tur öncesinde eşleştirme amacıyla sırasıyla büyükten küçüğe doğru puan, elo, ukd,
# ad-soyad(alfabetik sıra) ve lisans numaralarına göre sıralanırlar.
def sirala(oyuncular):
    alphabet = " ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
    oyuncular_isme_ve_lnoya_gore_sirali = sorted(oyuncular, key=lambda oyuncu: (tuple(alphabet.find(c) for c in oyuncu[1][2]), oyuncu[0]), reverse=False)
    oyuncular_sirali = sorted(oyuncular_isme_ve_lnoya_gore_sirali, key=lambda oyuncu: (sum(oyuncu[1][1]), oyuncu[1][3], oyuncu[1][4]), reverse=True)

    return oyuncular_sirali


# turnuvanın tur sayısının alınması. İstenilen aralıkta veri girilmezse tekrar istenir. Hata kontrolü yapılır.
def turnuva_biligilerini_al(oyuncular):
    min_tur_sayisi = math.ceil(math.log2(len(oyuncular)))  # min tur sayısının hesaplanması
    max_tur_sayisi = len(oyuncular) - 1  # max tur sayısının hesaplanması
    try:
        tur_sayisi = int(
            input("Turnuvadaki tur sayisini giriniz ({min}-{max}):".format(min=min_tur_sayisi, max=max_tur_sayisi)))
        if tur_sayisi < min_tur_sayisi or tur_sayisi > max_tur_sayisi:
            tur_sayisi = turnuva_biligilerini_al(oyuncular)
    except ValueError:
        print("Hatalı veri türü girdiniz")
        tur_sayisi = turnuva_biligilerini_al(oyuncular)

    return tur_sayisi


# ilk oyuncunun renginin alınması. Uygun veri girilmezse kullanıcıdan tekrar istenir.
def ilk_oyuncunun_rengini_al():
    renk = input("Baslangic siralamasina gore ilk oyuncunun ilk turdaki rengini giriniz ({renk1}/{renk2}): ".format(renk1=BEYAZ, renk2=SIYAH))
    if renk != BEYAZ and renk != SIYAH:
        renk = ilk_oyuncunun_rengini_al()

    return renk


# turnuvadaki her turdaki her masa için maçın sonucunun alınması. İstenilen aralıkta veri girilmezse tekrar istenir. Hata kontrolü yapılır.
def mac_sonuclarini_al(tur_sayisi, masa_sayisi):
    try:
        sonuc = int(input(
            "{tur}. turda {masa}. masada oynanan macin sonucunu giriniz({min}-{max}):".format(tur=tur_sayisi, masa=masa_sayisi, min=MIN_MAC_SONUCU, max=MAX_MAC_SONUCU)))
        if sonuc < MIN_MAC_SONUCU or sonuc > MAX_MAC_SONUCU:
            sonuc = mac_sonuclarini_al(tur_sayisi, masa_sayisi)
    except ValueError:
        print("Hatalı veri türü girdiniz")
        sonuc = mac_sonuclarini_al(tur_sayisi, masa_sayisi)

    return sonuc


# her turdaki eşleştirilmelerin yazdırılması ve formatlanması
def esletirme_tablolarini_yazdir(turlar, tur_sayisi, oyuncular):
    print("{tur}.Tur Eşleştirme Listesi:".format(tur=tur_sayisi))
    print("Beyazlar".rjust(19), "Siyahlar".rjust(22))
    print("MNo   BSNo     LNo   Puan  -  Puan   LNo   BSNo")
    print("---   ----   -----   ----     ----  -----  ----")
    for masa_no in turlar[tur_sayisi]:
        beyaz_oyuncu = oyuncu_bilgisini_getir(oyuncular, turlar[tur_sayisi][masa_no][0])
        siyah_oyuncu = oyuncu_bilgisini_getir(oyuncular, turlar[tur_sayisi][masa_no][1])
        print(format(masa_no, '3d'), end='   ')
        if beyaz_oyuncu is not None:
            print(format(beyaz_oyuncu[1][0], '4d'), end='   ')
            print(format(beyaz_oyuncu[0], '5d'), end='   ')
            print(format(sum(beyaz_oyuncu[1][1]), '4.2f'), end='  -  ')
        if siyah_oyuncu is not None:
            print(format(sum(siyah_oyuncu[1][1]), '4.2f'), end='   ')
            print(format(siyah_oyuncu[0], '4d'), end='  ')
            print(format(siyah_oyuncu[1][0], '4d'))
        else:
            print(format("BYE"))
    print()


# 2 oyuncu biribiriyle sadece 1 defa oynayabildiği için daha önce birlikte oynadılar mı diye kontrol edilir
def daha_once_eslesmis_mi(turlar, rakip_arayan, rakip_atanan):
    sonuc = False
    for tur_no in turlar:
        for masa_no in turlar[tur_no]:
            if rakip_arayan[0] == turlar[tur_no][masa_no][0] and rakip_atanan[0] == turlar[tur_no][masa_no][1]:
                sonuc = True
            elif rakip_arayan[0] == turlar[tur_no][masa_no][1] and rakip_atanan[0] == turlar[tur_no][masa_no][0]:
                sonuc = True
    return sonuc


# rakip aranan oyuncuya en yakın puana sahip oyuncu grubunun bulunması
def en_yakin_puanli_rakipleri_getir(oyuncular, turlar, tur_no, rakip_arayan, kontrol_edilmis_rakipler):
    en_yakin_puanli_rakipler = []  # en yakın puana sahip oyuncuların saklanması için bir liste oluşturulur.
    for oyuncu in oyuncular:
        sonuc = True
        for masa_no in turlar[tur_no]:
            # rakip olabilecek oyuncu o turda başka bir masaya yerleşmiş mi diye kontrol edilir.
            if oyuncu[0] == turlar[tur_no][masa_no][0] or oyuncu[0] == turlar[tur_no][masa_no][1]:
                sonuc = False
            # hata almamak için rakip arayan var mı diye kontrol edilir.
            elif rakip_arayan is not None and rakip_arayan == oyuncu:
                sonuc = False
            # rakip olabilecek oyuncu ile daha önce oynamış mı diye kontrol edilir.
            elif daha_once_eslesmis_mi(turlar, rakip_arayan, oyuncu):
                sonuc = False
            # daha önce kontrol edilmiş oyuncular görmezden gelinir
            elif len(kontrol_edilmis_rakipler) > 0:
                for kontrol_edilmis_rakip in kontrol_edilmis_rakipler:
                    if kontrol_edilmis_rakip == oyuncu:
                        sonuc = False
        if sonuc:
            # uygun koşulları sağlıyorsa oyuncunun bilgileri getirilir
            en_yakin_puanli_rakip = oyuncu_bilgisini_getir(oyuncular, oyuncu[0])
            # kontrol edilen rakip adayları arasından puanı büyük olan rakip veya rakipler seçilir
            if len(en_yakin_puanli_rakipler) == 0 or sum(en_yakin_puanli_rakip[1][1]) >= sum(en_yakin_puanli_rakipler[0][1][1]):
                # en yakın puanlı rakip en yakın puanlı rakipler listesine eklenir
                en_yakin_puanli_rakipler.append(en_yakin_puanli_rakip)

    return en_yakin_puanli_rakipler


# bye geçecek oyuncunun bulunması
def bye_gececek_kullaniciyi_getir(oyuncular, turlar):
    oyuncular_tersten_siralanmis = oyuncular.copy()  # oyuncular listesinin kopyası oluşturulur
    oyuncular_tersten_siralanmis.reverse()  # kopyalan liste tersten sıralanır
    bye_gececek_kullanici = None
    for oyuncu in oyuncular_tersten_siralanmis:
        sonuc = True
        if bye_gececek_kullanici is None:
            for tur_no in turlar:
                if bye_gececek_kullanici is None:
                    for masa_no in turlar[tur_no]:
                        # beyaz oyuncu oynamadan puan alırsa birdaha tur atlayamaz
                        if turlar[tur_no][masa_no][2] == 3 and turlar[tur_no][masa_no][0] == oyuncu[0]:
                            sonuc = False
                        # siyah oyuncu oynamadan puan alırsa birdaha tur atlayamaz
                        elif turlar[tur_no][masa_no][2] == 4 and turlar[tur_no][masa_no][1] == oyuncu[0]:
                            sonuc = False
                        # daha önceden tur atladıysa(bye geçmek) birdaha atlayamaz
                        elif turlar[tur_no][masa_no][1] is None and turlar[tur_no][masa_no][0] is not None and turlar[tur_no][masa_no][0] == oyuncu[0]:
                            sonuc = False
        # önceden tur atlamadıysa ve oynamadan puan almadıysa oyuncular tersten siralanmis listesinin ilk oyuncusu bye geçer
        if sonuc and bye_gececek_kullanici is None:
            bye_gececek_kullanici = oyuncu
    return bye_gececek_kullanici


def oyuncularin_son_aldigi_rengi_hesapla(oyuncu):
    oyuncunun_son_rengi = oyuncu[1][5][-1]
    if oyuncunun_son_rengi == ' ':  # oyuncu son turda bye geçtiyse 2 önceki turdaki rengine bakılır
        if len(oyuncu[1][5]) > 1:
            oyuncunun_son_rengi = oyuncu[1][5][-2]
        else:  # oyuncu ilk turda bye geçtiyse son rengine b ve s arasından rastgele bir harf verilir. Böylece renk alan diğer rakip adaylarına öncelik verilmiş olur.
            oyuncunun_son_rengi = 'c'

    return oyuncunun_son_rengi


# rakibin bulunması
def rakip_atanan_bul(en_yakin_puanli_rakipler, rakibin_almasi_gereken_renk, bye_gececek_oyuncu):
    rakip_atanan = None
    atanabilecek_rakipler = []  # atanabilecek rakipleri saklamak için bir liste oluşturulur
    for oyuncu in en_yakin_puanli_rakipler:  # en yakın puana sahip oyuncularda dönülür
        sonuc = True
        # oyuncu o turda bye geçerse rakip olamaz
        if oyuncu == bye_gececek_oyuncu:
            sonuc = False
        # oyuncu son 2 turdaki aldığı rengi bir sonraki turda alamaz
        if len(oyuncu[1][5]) > 1 and oyuncu[1][5][-1] == rakibin_almasi_gereken_renk and \
                oyuncu[1][5][-2] == rakibin_almasi_gereken_renk:
            sonuc = False
        if len(oyuncu[1][5]) > 2 and oyuncu[1][5][-1] == ' ' and oyuncu[1][5][-2] == rakibin_almasi_gereken_renk and \
                oyuncu[1][5][-3] == rakibin_almasi_gereken_renk:
            sonuc = False
        if len(oyuncu[1][5]) > 2 and oyuncu[1][5][-2] == ' ' and oyuncu[1][5][-1] == rakibin_almasi_gereken_renk and \
                oyuncu[1][5][-3] == rakibin_almasi_gereken_renk:
            sonuc = False
        if sonuc:
            # koşulları sağlayan rakip atanabilecek rakipler listesine eklenir
            rakip = oyuncu_bilgisini_getir(en_yakin_puanli_rakipler, oyuncu[0])
            atanabilecek_rakipler.append(rakip)

    if len(atanabilecek_rakipler) > 0 and len(atanabilecek_rakipler[0][1][5]) > 0 and rakibin_almasi_gereken_renk != ' ':
        if rakibin_almasi_gereken_renk == SIYAH:
            # önceki turda beyaz olanlara öncelik verilmesi için atanabilecek rakipler listesindeki renkler alfabetik sıralanır.
             oyuncular_renge_sirali = sorted(atanabilecek_rakipler, key=lambda oyuncu: oyuncularin_son_aldigi_rengi_hesapla(oyuncu), reverse=False)
        else:
            # önceki turda siyah olanlara öncelik verilmesi için atanabilecek rakipler listesindeki renkler alfabenin tersine göre sıralanır.
            oyuncular_renge_sirali = sorted(atanabilecek_rakipler, key=lambda oyuncu: oyuncularin_son_aldigi_rengi_hesapla(oyuncu), reverse=True)

    else:
        oyuncular_renge_sirali = atanabilecek_rakipler
    # oyuncular renge sıralı listesindeki ilk eleman rakip atanan olur
    for rakip in oyuncular_renge_sirali:
        if rakip_atanan is None:
            rakip_atanan = rakip

    return rakip_atanan


# rakip arayanı bulma
def rakip_arayan_bul(oyuncular, tur_no, bye_gececek_oyuncu):
    rakip_arayan = None
    for oyuncu in oyuncular:
        sonuc = True
        for masa_no in tur_no:
            # oyuncu bye geçerse rakip arayan olamaz
            if oyuncu == bye_gececek_oyuncu:
                sonuc = False
            # oyuncu o turda daha önce bir masaya yerleştiyse rakip arayan olamaz
            if oyuncu[0] == tur_no[masa_no][0] or oyuncu[0] == tur_no[masa_no][1]:
                sonuc = False
        if sonuc:
            # koşulları sağlayan oyuncular rakip arayan olur
            rakip_arayan = oyuncu_bilgisini_getir(oyuncular, oyuncu[0])
            return rakip_arayan
    return rakip_arayan


# lazım olduğunda oyuncunun bilgilerinin getirilmesi için bir fonksiyon oluşturulur
def oyuncu_bilgisini_getir(oyuncular, lisans_no):
    for oyuncu in oyuncular:
        if lisans_no == oyuncu[0]:
            return oyuncu


# oyuncuların puanlarının ve galibiyet sayılarının hesaplanması ve oynadıkları maçın sonucunun karakterlerinin alınması
def puanlari_mac_sonucu_ve_galibiyet_sayisini_hesaplama(oyuncular, tur_no):
    for masa_no in tur_no:
        beyaz_oyuncu = oyuncu_bilgisini_getir(oyuncular, tur_no[masa_no][0])
        siyah_oyuncu = oyuncu_bilgisini_getir(oyuncular, tur_no[masa_no][1])

        if tur_no[masa_no][2] == 0:
            beyaz_oyuncu[1][1].append(0.5)  # maç berabere bittiyse 2 oyuncuya da 0.5 puan eklenir.
            siyah_oyuncu[1][1].append(0.5)  # berabere kalınılan maçlarda '½' karakteri kullanılır.
            beyaz_oyuncu[1][6] += chr(189)
            siyah_oyuncu[1][6] += chr(189)
        elif tur_no[masa_no][2] == 1:
            beyaz_oyuncu[1][1].append(1)  # maçı beyaz kazandıysa beyaza 1, siyaha 0 puan eklenir.
            siyah_oyuncu[1][1].append(0)
            beyaz_oyuncu[1][6] += '1'  # galibiyet kazanılan maçlar için '1' karakteri eklenir.
            siyah_oyuncu[1][6] += '0'  # mağlubiyet için '0' karakteri eklenir
            beyaz_oyuncu[1][7] += 1  # maçı beyaz kazandıysa beyaza 1 puan galibiyet sayısı eklenir.
        elif tur_no[masa_no][2] == 2:
            siyah_oyuncu[1][1].append(1)  # maçı siyah kazandıysa siyaha 1, beyaza 0 puan eklenir.
            beyaz_oyuncu[1][1].append(0)
            siyah_oyuncu[1][6] += '1'  # galibiyet kazanılan maçlar için '1' karakteri eklenir.
            beyaz_oyuncu[1][6] += '0'  # mağlubiyet için '0' karakteri eklenir
            siyah_oyuncu[1][7] += 1  # maçı siyah kazandıysa siyaha 1 puan galibiyet sayısı eklenir.
        elif tur_no[masa_no][2] == 3:
            beyaz_oyuncu[1][1].append(1)  # siyah maça gelmediyse beyaza 1, siyaha 0 puan eklenir.
            siyah_oyuncu[1][1].append(0)
            beyaz_oyuncu[1][6] += '+'  # maça rakibi gelmeyen oyunculara '+' karakteri eklenir.
            siyah_oyuncu[1][6] += '-'  # maça gelmeyen oyunculara '-' karakteri eklenir
            beyaz_oyuncu[1][7] += 1  # siyah maça gelmediyse beyaz oyuncuya 1 puan galibiyet sayısı eklenir.
        elif tur_no[masa_no][2] == 4:
            siyah_oyuncu[1][1].append(1)  # beyaz maça gelmediyse siyaha 1, beyaza 0 puan eklenir.
            beyaz_oyuncu[1][1].append(0)
            beyaz_oyuncu[1][6] += '-'  # maça gelmeyen oyunculara '-' karakteri eklenir
            siyah_oyuncu[1][6] += '+'  # maça rakibi gelmeyen oyunculara '+' karakteri eklenir.
            siyah_oyuncu[1][7] += 1  # beyaz maça gelmediyse siyah oyuncuya 1 puan galibiyet sayısı eklenir.
        elif tur_no[masa_no][2] == 5:
            siyah_oyuncu[1][1].append(0)  # her iki oyuncu da maça gelmediyse ikisine de 0 puan eklenir.
            beyaz_oyuncu[1][1].append(0)
            beyaz_oyuncu[1][6] += '-'  # maça gelmeyen oyunculara '-' karakteri eklenir
            siyah_oyuncu[1][6] += '-'

        elif tur_no[masa_no][2] is None:  # eğer oyuncu o turu bye geçiyorsa 1 puan eklenir ve '1' karakteri verilir.
            beyaz_oyuncu[1][1].append(1)
            beyaz_oyuncu[1][6] += '1'


# Buchholz-1 (BH-1) ve Buchholz-2 (BH-2) puanlarının hesaplanması
def buchholz_puanlarini_hesaplama(oyuncular, turlar):
    for oyuncu in oyuncular:
        puanlar = []  # Rakiplerin puanlarının tutulması için boş bir liste oluşturulur
        for tur_no in turlar:
            for masa_no in turlar[tur_no]:
                rakip_lisans_no = 0
                if turlar[tur_no][masa_no][0] == oyuncu[0]:
                    rakip_lisans_no = turlar[tur_no][masa_no][1]  # beyaz oyuncunun rakibinin bulunması
                elif turlar[tur_no][masa_no][1] == oyuncu[0]:
                    rakip_lisans_no = turlar[tur_no][masa_no][0]   # siyah oyuncunun rakibinin bulunması

                rakip = oyuncu_bilgisini_getir(oyuncular, rakip_lisans_no)
                if rakip is not None:
                    if oyuncu[1][6][tur_no - 1] == '+':  # oyuncu oynamadan puan alırsa o turda oynanmayan maçlar için hesaplanan puan alınır
                        oynanmayan_puan = oynanmayan_mac_puan_hesapla(oyuncu, tur_no)
                        puanlar.append(float(oynanmayan_puan))  # hesaplanan puan puanlar listesine eklenir
                    elif oyuncu[1][6][tur_no - 1] == '-':  # oyuncu maça gelmezse o turda oynanmayan maçlar için hesaplanan puan alınır
                        oynanmayan_puan = oynanmayan_mac_puan_hesapla(oyuncu, tur_no)
                        puanlar.append(float(oynanmayan_puan))  # hesaplanan puan puanlar listesine eklenir
                    else:
                        puanlar.append(float(sum(rakip[1][1])))  # oynanan maçlarda rakibin puanı puanlar listesine eklenir
                # oyuncu bye geçerse oynanmayan maçlar için hesaplanan puan alınır
                elif turlar[tur_no][masa_no][0] == oyuncu[0] and turlar[tur_no][masa_no][2] is None:
                    oynanmayan_puan = oynanmayan_mac_puan_hesapla(oyuncu, tur_no)
                    puanlar.append(float(oynanmayan_puan))  # hesaplanan puan puanlar listesine eklenir
        if len(puanlar) > 0:
            puanlar.remove(min(puanlar))  # bh1 ve bh2 puanı için en düşük puana sahip rakibinin puanı puanlar listesinden çıkarılır
            # bh1 puanının hesaplanması için puanlar listesindeki kalan rakiplerin puanları toplanır ve oyuncular listesindeki gerekli bölüme o puan atanır.
            oyuncu[1][8] = sum(puanlar)

            puanlar.remove(min(puanlar))  # bh2 puanı için kalan puanlar arasından en düşük puana sahip diğer rakibinin puanı da puanlar listesinden çıkarılır
            # bh2 puanının hesaplanması için puanlar listesindeki kalan rakiplerin puanları toplanır ve oyuncular listesindeki gerekli bölüme o puan atanır.
            oyuncu[1][9] = sum(puanlar)


# oynanmayan maçlar için bh1, bh2, sb ve gs puanlarını hesaplanması
def oynanmayan_mac_puan_hesapla(oyuncu, referans_tur_no):
    puan = 0
    for tur_no in range(1, len(oyuncu[1][1]) + 1):  # tur sayısı kadar dönülür
        if tur_no < referans_tur_no:  # oynanmayan maçın olduğu turdan önceki turlar için
            puan += oyuncu[1][1][tur_no - 1]  # oyuncunun kendisinin o tura kadar kazandığı puan eklenir.
        elif tur_no > referans_tur_no:  # oynanmayan maçın olduğu turdan sonraki turlar için
            puan += 0.5  # kalan her tur için puana 0,5 eklenir.
    return puan


# Sonneborn Berger (SB) puanının hesaplanması
def sonneborn_berger_puanini_hesaplama(oyuncular, turlar):
    for oyuncu in oyuncular:
        puan = 0
        for tur_no in turlar:
            for masa_no in turlar[tur_no]:
                rakip = None
                berabere = False
                if turlar[tur_no][masa_no][0] == oyuncu[0]:  # beyaz oyuncu
                    rakip_lisans_no = turlar[tur_no][masa_no][1]  # beyaz oyuncunun rakibi
                    if turlar[tur_no][masa_no][2] == 0:  # maçın berabere bitme durumu
                        rakip = oyuncu_bilgisini_getir(oyuncular, rakip_lisans_no)
                        berabere = True
                    elif turlar[tur_no][masa_no][2] == 1:  # maçı beyaz oyuncunun kazanma durumu
                        rakip = oyuncu_bilgisini_getir(oyuncular, rakip_lisans_no)
                    elif turlar[tur_no][masa_no][2] is None:  # oyuncunun bye geçme durumu
                        oynanmayan_puan = oynanmayan_mac_puan_hesapla(oyuncu, tur_no)
                        puan += oynanmayan_puan  # oyuncu bye geçerse oynanmayan maçlar için hesaplanan puan alınır
                    elif turlar[tur_no][masa_no][2] == 3:  # siyah oyuncunun maça gelmeme durumu
                        oynanmayan_puan = oynanmayan_mac_puan_hesapla(oyuncu, tur_no)
                        puan += oynanmayan_puan  # oyuncu oynamadan puan alırsa oynanmayan maçlar için hesaplanan puan eklenir

                elif turlar[tur_no][masa_no][1] == oyuncu[0]:  # siyah oyuncu
                    rakip_lisans_no = turlar[tur_no][masa_no][0]  # siyah oyuncunun rakibi
                    if turlar[tur_no][masa_no][2] == 0:  # maçın berabere bitme durumu
                        rakip = oyuncu_bilgisini_getir(oyuncular, rakip_lisans_no)
                        berabere = True
                    elif turlar[tur_no][masa_no][2] == 2:  # maçı siyah oyuncunun kazanma durumu
                        rakip = oyuncu_bilgisini_getir(oyuncular, rakip_lisans_no)
                    elif turlar[tur_no][masa_no][2] == 4:  # beyaz oyuncunun maça gelmeme durumu
                        oynanmayan_puan = oynanmayan_mac_puan_hesapla(oyuncu, tur_no)
                        puan += oynanmayan_puan  # oyuncu oynamadan puan alırsa oynanmayan maçlar için hesaplanan puan eklenir
                if rakip is not None:
                    if berabere:
                        puan += sum(rakip[1][1]) / 2  # maç berabere biterse rakibin puanının yarısı sb puanına eklenir
                    else:
                        puan += sum(rakip[1][1])  # yendiği rakiplerin aldıkları puanlar ve oynanmayan maçlar için hesaplanan puanlar sb puanına eklenir.

        oyuncu[1][10] = puan  # oyuncular listesindeki gerekli bölüme hesaplanan sb puanı atanır.


# Nihai Sıralama Listesinin yazdırılması ve formatlanması
def nihai_siralama_yazdir(oyuncular):
    sira = 1
    print("Nihai Sıralama Listesi:")
    print("SNo   BSNo     LNo   Ad-Soyad           ELO    UKD   Puan    BH-1    BH-2      SB   GS")
    print("---   ----   -----   ---------------   ----   ----   ----   -----   -----   -----   --")
    for oyuncu in oyuncular:
        oyuncu.append(sira)  # oyuncunun sira numarası oyuncu listesinin sonuna eklenir. (2. indexine)
        print(format(oyuncu[2], '3d'), end='   ')
        print(format(oyuncu[1][0], '4d'), end='   ')
        print(format(oyuncu[0], '5d'), end='   ')
        print(format(oyuncu[1][2], '15'), end='   ')
        print(format(oyuncu[1][3], '4d'), end='   ')
        print(format(oyuncu[1][4], '4d'), end='   ')
        print(format(sum(oyuncu[1][1]), '4.2f'), end='   ')
        print(format(oyuncu[1][8], '5.2f'), end='   ')
        print(format(oyuncu[1][9], '5.2f'), end='   ')
        print(format(oyuncu[1][10], '5.2f'), end='   ')
        print(format(oyuncu[1][7], '2d'))

        sira += 1
    print()


# rakip oyuncunun bilgilerinin bulunması
def rakip_oyuncunun_bilgilerini_getir(oyuncular, tur_no, rakip_arayan):
    rakip_lisans_no = 0
    for masa_no in tur_no:
        if tur_no[masa_no][0] == rakip_arayan[0]:  # beyaz oyuncu
            rakip_lisans_no = tur_no[masa_no][1]  # beyaz oyuncunun rakibi olan siyah oyuncu
        elif tur_no[masa_no][1] == rakip_arayan[0]:  # siyah oyuncu
            rakip_lisans_no = tur_no[masa_no][0]  # siyah oyuncunun rakibi olan beyaz oyuncu

    rakip = oyuncu_bilgisini_getir(oyuncular, rakip_lisans_no)
    return rakip


# çapraz tablonun yazdırılması ve formatlanması
def carpraz_tablo_yazdir(oyuncular, turlar):
    print("Çapraz Tablo:")
    print("BSNo    SNo     LNo    Ad-Soyad            ELO    UKD", end='      ')
    for tur_no in turlar:
        print(format(str(tur_no) + '.Tur', '7'), end='    ')
    print("Puan    BH-1    BH-2      SB   GS")
    print("----    ---   -----    ---------------    ----   ----", end="    ")
    for tur_no in turlar:
        print("-------", end="    ")
    print("  ----   -----   -----   -----   --")
    oyuncular_bsnoya_gore_sirali = sorted(oyuncular, key=lambda oyuncu: oyuncu[1][0], reverse=False)
    for oyuncu in oyuncular_bsnoya_gore_sirali:
        print(format(oyuncu[1][0], '4d'), end='    ')
        print(format(oyuncu[2], '3d'), end='   ')
        print(format(oyuncu[0], '5d'), end='    ')
        print(format(oyuncu[1][2], '14'), end='     ')
        print(format(oyuncu[1][3], '4d'), end='   ')
        print(format(oyuncu[1][4], '4d'), end='    ')
        for tur_no in turlar:
            rakip_bs_no = '-'
            oyuncu_renk = '-'
            rakip = rakip_oyuncunun_bilgilerini_getir(oyuncular, turlar[tur_no], oyuncu)
            renk = str(oyuncu[1][5][tur_no - 1])
            if rakip is not None:
                rakip_bs_no = rakip[1][0]
            print(str(rakip_bs_no).rjust(3), end=' ')
            if renk != ' ':
                oyuncu_renk = renk
            print(format(oyuncu_renk, '1'), end=' ')
            print(format(str(oyuncu[1][6][tur_no - 1]), '1'), end='    ')
        print(format(sum(oyuncu[1][1]), '6.2f'), end='   ')
        print(format(oyuncu[1][8], '5.2f'), end='   ')
        print(format(oyuncu[1][9], '5.2f'), end='   ')
        print(format(oyuncu[1][10], '5.2f'), end='   ')
        print(format(oyuncu[1][7], '2'))


# main fonksiyon
def main():
    oyuncular = []  # tüm oyuncuların bilgilerinin saklanması için boş bir liste oluşturulur
    lisans_numarasi = lisans_numarasi_al(oyuncular)  # ilk oyunun lisans numrası alınır
    while lisans_numarasi <= 0:  # ilk oyuncunun lisans numarası 0 dan büyük olmalıdır
        lisans_numarasi = lisans_numarasi_al(oyuncular)
    while lisans_numarasi > 0:  # başka bir oyuncu varsa bu döngüye girilir
        oyuncu = []  # her oyuncunun bilgilerinin saklanması için boş bir liste oluşturulur
        oyuncu_adi = oyuncu_adini_al()  # her oyuncunun ismi alınır
        elo_no = oyuncu_elo_al()  # her oyuncunun elo puanı alınır
        ukd_no = oyuncu_ukd_al()  # her oyuncunun ukd puanı alınır
        oyuncu.append(lisans_numarasi)  # oyuncunun lisans numarası oyuncu listesine eklenir (0. indexte lisans numarası vardır)
        # oyuncunun diğer bilgileri oyuncu listesinin sonuna eklenir(1. indexe eklenir) Sırasıyla BSNo, turlarda aldığı
        # puanlarının tutulduğu liste, oyuncunun adı, elo puanı, ukd puanı, oyuncunun renklerinin olduğu liste,
        # mac sonucunun karakterlerinin olduğu liste, galibiyet sayısı, bh1 puanı, bh2 puanı ve sb puanı eklenir.
        oyuncu.append([0, [], oyuncu_adi, elo_no, ukd_no, [], [], 0, 0.00, 0.00, 0.00])
        oyuncular.append(oyuncu)  # oyuncu listesi oyuncular listesine eklenir
        lisans_numarasi = lisans_numarasi_al(oyuncular)  # her oyuncudan sonra lisans numarası birdaha istenir eğer 0
        # veya 0 dan küçük bir değer girilirse baska oyuncu yoktur demektir döngüden çıkılır.

    oyuncular_siralanmis = sirala(oyuncular)
    oyuncu_bilgilerini_yazdir(oyuncular_siralanmis)
    tur_sayisi = turnuva_biligilerini_al(oyuncular_siralanmis)
    ilk_oyuncunun_rengi = ilk_oyuncunun_rengini_al()
    turlar = {}  # turnuvadaki tüm tur bilgilerini saklamak için dictionary oluşturulur
    masa_sayisi = math.ceil(len(oyuncular) / 2)  # masa sayısının hesaplanması
    for tur_sayisi in range(1, tur_sayisi + 1):
        turlar[tur_sayisi] = {}  # turlar dictionarysine key olarak tur sayısı dictionarysi atanır
        bye_gececek_oyuncu = None
        if len(oyuncular) % 2 == 1:  # eğer oyuncu sayısı tek ise bye geçecek oyuncu bulunur
            bye_gececek_oyuncu = bye_gececek_kullaniciyi_getir(oyuncular_siralanmis, turlar)
        for masa_no in range(1, masa_sayisi + 1):
            turlar[tur_sayisi][masa_no] = [None, None, None]  # tur sayısı dictionarysine, key olarak masa no atanır
            # her turun bilgileri [beyaz oyuncunun lisans numrası, siyah oyuncunun lisans numarası, maçın sonucu] olacak şekilde sözlükte tutulur.
            if bye_gececek_oyuncu is not None and masa_no == masa_sayisi:
                bye_gececek_oyuncu[1][5].append(' ')  # bye geçen oyuncunun rengi yoktur
                turlar[tur_sayisi][masa_no][0] = bye_gececek_oyuncu[0]
            else:  # oyuncu bye geçmiyorsa
                rakip_arayan = rakip_arayan_bul(oyuncular_siralanmis, turlar[tur_sayisi], bye_gececek_oyuncu)

                if len(rakip_arayan[1][5]) == 0:  # ilk tursa
                    rakip_arayanin_rengi = ilk_oyuncunun_rengi  # ilk turda bsnosu tek olanlar rakip arayanlardır. Bsnosu tek olanlara ilk oyuncunun rengi verilir.
                    if rakip_arayanin_rengi == SIYAH:
                        rakip_atananin_rengi = BEYAZ  # rakibe zıt renk verilir
                    else:
                        rakip_atananin_rengi = SIYAH

                else:  # ilk tur değilse
                    rakip_arayanin_rengi = rakip_arayan[1][5][-1]  # rakip arayananın son turda aldığı renk

                    if rakip_arayanin_rengi == ' ':  # rakip arayan bir önceki turda bye geçtiyse
                        if len(rakip_arayan[1][5]) > 1:
                            rakip_arayanin_rengi = rakip_arayan[1][5][-2]  # rakip arayan 2 önceki turdaki rengini alır
                    if rakip_arayanin_rengi == SIYAH:
                        rakip_arayanin_rengi = BEYAZ  # Rakip arayan oyuncuya bir önceki turda aldığı rengin karşıt rengi verilir
                        rakip_atananin_rengi = SIYAH  # rakip atanan kişiye rakip arayanın zıt rengi verilir
                    elif rakip_arayanin_rengi == BEYAZ:
                        rakip_arayanin_rengi = SIYAH
                        rakip_atananin_rengi = BEYAZ
                    else:
                        rakip_atananin_rengi = ' '  # rakip arayan ilk turda bye geçtiyse rakip atananın rengine göre renk alması için (sadece 2. tur için)

                kontrol_edilmis_rakipler = []  # kontrol edilmiş rakipleri saklamak için boş bir liste oluşturulur
                en_yakin_puanli_rakipler = en_yakin_puanli_rakipleri_getir(oyuncular_siralanmis, turlar, tur_sayisi, rakip_arayan, kontrol_edilmis_rakipler)
                rakip_atanan = rakip_atanan_bul(en_yakin_puanli_rakipler, rakip_atananin_rengi, bye_gececek_oyuncu)

                if rakip_atananin_rengi == ' ' and rakip_atanan is not None:  # 2. turda 1. turda bye geçen oyuncu rakip arıyorsa rakibin rengine göre renk ataması yapılır(sadece 2.tur için)
                    for renk in reversed(rakip_atanan[1][5]):
                        if renk != ' ' and rakip_atananin_rengi == ' ':
                            if renk == SIYAH:
                                rakip_atananin_rengi = BEYAZ
                                rakip_arayanin_rengi = SIYAH
                            elif renk == BEYAZ:
                                rakip_atananin_rengi = SIYAH
                                rakip_arayanin_rengi = BEYAZ

                while rakip_atanan is None and len(en_yakin_puanli_rakipler) > 0:  # rakip adayları arasından rakip arayan zıt rengi aldığında uygun rakip bulamadıysa döngüye girilir
                    if rakip_atanan is None:
                        if rakip_arayanin_rengi == SIYAH:  # rakip arayan bir önceki turdaki rengini alması için renkler değiştirilir (kural 1.3)
                            rakip_arayanin_rengi = BEYAZ   # rakip arayan aynı rengi, rakip zıt rengi almış olur
                            rakip_atananin_rengi = SIYAH
                        else:
                            rakip_arayanin_rengi = SIYAH
                            rakip_atananin_rengi = BEYAZ
                    rakip_atanan = rakip_atanan_bul(en_yakin_puanli_rakipler, rakip_atananin_rengi, bye_gececek_oyuncu)
                    if rakip_atanan is None:  # hala uygun bir rakip bulunamadıysa ( kural 1.3e göre de uygun bir rakip bulunamadıysa)
                        if rakip_arayanin_rengi == SIYAH:  # rakip arayanın ve rakip atananın rengi değiştirilir(ilk hali)
                            rakip_arayanin_rengi = BEYAZ
                            rakip_atananin_rengi = SIYAH
                        else:
                            rakip_arayanin_rengi = SIYAH
                            rakip_atananin_rengi = BEYAZ
                        # ve bir sonraki en yakın puana sahip oyuncular kontrol edilir
                        kontrol_edilmis_rakipler.extend(en_yakin_puanli_rakipler)
                        en_yakin_puanli_rakipler = en_yakin_puanli_rakipleri_getir(oyuncular_siralanmis, turlar, tur_sayisi, rakip_arayan, kontrol_edilmis_rakipler)
                        rakip_atanan = rakip_atanan_bul(en_yakin_puanli_rakipler, rakip_atananin_rengi, bye_gececek_oyuncu)
                if rakip_atanan is not None:
                    rakip_arayan[1][5].append(rakip_arayanin_rengi)
                    rakip_atanan[1][5].append(rakip_atananin_rengi)
                    if rakip_arayanin_rengi == BEYAZ:
                        turlar[tur_sayisi][masa_no][0] = rakip_arayan[0]  # beyaz ve siyah oyunların lisans numaraları sözlüğe eklenir
                        turlar[tur_sayisi][masa_no][1] = rakip_atanan[0]
                    else:
                        turlar[tur_sayisi][masa_no][1] = rakip_arayan[0]
                        turlar[tur_sayisi][masa_no][0] = rakip_atanan[0]

        esletirme_tablolarini_yazdir(turlar, tur_sayisi, oyuncular_siralanmis)

        for masa in range(1, masa_sayisi + 1):
            if turlar[tur_sayisi][masa][0] is not None and turlar[tur_sayisi][masa][1] is not None:
                turlar[tur_sayisi][masa][2] = mac_sonuclarini_al(tur_sayisi, masa)
        puanlari_mac_sonucu_ve_galibiyet_sayisini_hesaplama(oyuncular_siralanmis, turlar[tur_sayisi])
        oyuncular_siralanmis = sirala(oyuncular_siralanmis)
    buchholz_puanlarini_hesaplama(oyuncular_siralanmis, turlar)
    sonneborn_berger_puanini_hesaplama(oyuncular_siralanmis, turlar)
    oyuncular_puanlara_gore_siralanmis = sorted(oyuncular, key=lambda oyuncu: (
        sum(oyuncu[1][1]), oyuncu[1][8], oyuncu[1][9], oyuncu[1][10], oyuncu[1][7]), reverse=True)
    nihai_siralama_yazdir(oyuncular_puanlara_gore_siralanmis)
    carpraz_tablo_yazdir(oyuncular_siralanmis, turlar)


# main fonksiyonu çağır
main()
