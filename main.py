import random

işlemsirasi = 0
ikiyüzadedi = int(input("200'lük  banknot sayısını giriniz : "))
yüzadedi = int(input("100'lük banknot sayısını giriniz : "))
elliadedi = int(input("50'lik banknot sayısını giriniz : "))
yirmiadedi = int(input("20'lik banknot sayısını giriniz : "))
onadedi = int(input("10'luk banknot sayısını giriniz : "))
a, c, a_iki_yüz, a_yüz, a_elli, a_yirmi, a_on, v_iki_yüzlük, v_yüzlük, v_ellilik, v_yirmilik, v_onluk = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
saat = [8, 00]
karar = ""
k = list(i for i in range(0, 101, 10))
for x in range(10):
    v = random.randint(1, 10)
    k[x] += v
print("Para yatıracak sıradaki kişiler: ", k)
while True:
    işlem_gören_para = random.randrange(10, 2001, 10)
    para = işlem_gören_para
    zaman = random.randint(10, 31)
    boş = random.randint(1, zaman)
    işlemsirasi += 1
    toplampara = (200 * ikiyüzadedi) + (100 * yüzadedi) + (50 * elliadedi) + (20 * yirmiadedi) + (10 * onadedi)
    if işlemsirasi == k[0] or işlemsirasi == k[1] or işlemsirasi == k[2] or işlemsirasi == k[3] or işlemsirasi == k[
        4] or işlemsirasi == k[5] or işlemsirasi == k[6] or işlemsirasi == k[7] or işlemsirasi == k[8] or işlemsirasi == \
            k[9]:
        a += 1
        karar = "Yatıracak"
        a_iki_yüz = işlem_gören_para // 200
        ikiyüzadedi += a_iki_yüz
        işlem_gören_para -= 200 * a_iki_yüz

        a_yüz = işlem_gören_para // 100
        yüzadedi += a_yüz
        işlem_gören_para -= 100 * a_yüz

        a_elli = işlem_gören_para // 50
        elliadedi += a_elli
        işlem_gören_para -= 50 * a_elli

        a_yirmi = işlem_gören_para // 20
        yirmiadedi += a_yirmi
        işlem_gören_para -= 20 * a_yirmi

        a_on = işlem_gören_para // 10
        onadedi += a_on
        işlem_gören_para -= 10 * a_on
        bakiye = (200 * ikiyüzadedi) + (100 * yüzadedi) + (50 * elliadedi) + (20 * yirmiadedi) + (10 * onadedi)
        print(a + c, " . kişi : ", para, "TL ", karar, ": ", end="")
        if saat[1] < 60:
            saat[1] += boş
            if saat[1] >= 60:
                saat[0] += 1
                saat[1] -= 60
                if saat[0] == 24:
                    saat[0] -= 24
                    print("---> saat: {}:{} ".format(saat[0], saat[1]))
                else:
                    print("---> saat: {}:{} ".format(saat[0], saat[1]))
            else:
                print("---> saat: {}:{} ".format(saat[0], saat[1]))

        print(
            " {} tane ikiyüzlük , {} tane yüzlük , {} tane ellilik  , {} tane yirmilik ,  {} tane onluk  alındı.".format(
                a_iki_yüz, a_yüz, a_elli, a_yirmi, a_on))
        print(
            " {}  tane ikiyüzlük ,  {} tane yüzlük ,  {} tane ellilik  ,  {} tane yirmilik ,  {} tane  onluk kaldı.".format(
                ikiyüzadedi, yüzadedi, elliadedi, yirmiadedi, onadedi))
        print("Toplam bakiye = ", bakiye)
        print()
    # elif işlemsirasi != k[0] and işlemsirasi !=k[1] and işlemsirasi != k[2] and işlemsirasi !=k[3] and işlemsirasi != k[4]and işlemsirasi != k[5]and işlemsirasi != k[6] and işlemsirasi != k[7] and işlemsirasi!= k[8]and işlemsirasi!=k[9]:
    else:
        karar = "Çekecek"
        v_iki_yüzlük = işlem_gören_para // 200
        if ikiyüzadedi != 0:
            if ikiyüzadedi >= v_iki_yüzlük:
                ikiyüzadedi -= v_iki_yüzlük
            # işlem_gören_para -= 200 * v_iki_yüzlük
            else:
                v_iki_yüzlük = ikiyüzadedi
                ikiyüzadedi -= v_iki_yüzlük
                # işlem_gören_para -= v_iki_yüzlük * 200
        else:
            v_iki_yüzlük = 0
        işlem_gören_para -= v_iki_yüzlük * 200
        v_yüzlük = işlem_gören_para // 100
        if yüzadedi != 0:
            if yüzadedi >= v_yüzlük:
                yüzadedi -= v_yüzlük
                # işlem_gören_para -= 100 * v_yüzlük
            else:
                v_yüzlük = yüzadedi
                yüzadedi = 0
            # işlem_gören_para -= yüzadedi * 100
        else:
            v_yüzlük = 0
        işlem_gören_para -= 100 * v_yüzlük
        v_ellilik = işlem_gören_para // 50
        if elliadedi != 0:
            if elliadedi >= v_ellilik:
                elliadedi -= v_ellilik
                # işlem_gören_para -= 50 * v_ellilik
            else:
                v_ellilik = elliadedi
                elliadedi = 0
                # işlem_gören_para -= elliadedi * 50
        else:
            v_ellilik = 0
        işlem_gören_para -= 50 * v_ellilik
        v_yirmilik = işlem_gören_para // 20
        if yirmiadedi != 0:
            if yirmiadedi >= v_yirmilik:
                yirmiadedi -= v_yirmilik
            # işlem_gören_para -= 20 * v_yirmilik
            else:
                v_yirmilik = yirmiadedi
                yirmiadedi = 0
                # işlem_gören_para -= yirmiadedi * 20
        else:
            v_yirmilik = 0
        işlem_gören_para -= 20 * v_yirmilik
        v_onluk = işlem_gören_para // 10
        if onadedi >= v_onluk:
            onadedi -= v_onluk
            işlem_gören_para -= 10 * v_onluk
        else:
            v_onluk = onadedi
            onadedi = 0
        bakiye = (200 * ikiyüzadedi) + (100 * yüzadedi) + (50 * elliadedi) + (20 * yirmiadedi) + (10 * onadedi)
        c += 1
        if toplampara < para:
            para = bakiye
            print(a + c, " . kişi : ", toplampara, "TL Çekti ve işlem bitti... ", end="")
            if saat[1] < 60:
                saat[1] += boş
                if saat[1] >= 60:
                    saat[0] += 1
                    saat[1] -= 60
                    if saat[0] == 24:
                        saat[0] -= 24
                        print("---> saat: {}:{} ".format(saat[0], saat[1]))
                    else:
                        print("---> saat: {}:{} ".format(saat[0], saat[1]))
                else:
                    print("---> saat: {}:{} ".format(saat[0], saat[1]))
            print(
                " {} tane ikiyüzlük , {} tane yüzlük , {} tane ellilik  , {} tane yirmilik ,  {} tane onluk  verilecek.".format(
                    v_iki_yüzlük, v_yüzlük, v_ellilik, v_yirmilik, v_onluk))
            print(
                " {}  tane ikiyüzlük ,  {} tane yüzlük ,  {} tane ellilik  ,  {} tane yirmilik ,  {} tane  onluk kaldı.".format(
                    ikiyüzadedi, yüzadedi, elliadedi, yirmiadedi, onadedi))
            print("------İşlem Bitti-----")
            break
        print(a + c, " . kişi : ", para, "TL ", karar, " : ", end="")
        if saat[1] < 60:
            saat[1] += boş
            if saat[1] >= 60:
                saat[0] += 1
                saat[1] -= 60
                if saat[0] == 24:
                    saat[0] -= 24
                    print("---> saat: {}:{} ".format(saat[0], saat[1]))
                else:
                    print("---> saat: {}:{} ".format(saat[0], saat[1]))
            else:
                print("---> saat: {}:{} ".format(saat[0], saat[1]))
        print(
            " {} tane ikiyüzlük , {} tane yüzlük , {} tane ellilik  , {} tane yirmilik ,  {} tane onluk  verilecek.".format(
                v_iki_yüzlük, v_yüzlük, v_ellilik, v_yirmilik, v_onluk))
        print(
            " {}  tane ikiyüzlük ,  {} tane yüzlük ,  {} tane ellilik  ,  {} tane yirmilik ,  {} tane  onluk kaldı.".format(
                ikiyüzadedi, yüzadedi, elliadedi, yirmiadedi, onadedi))
        print("Kalan bakiye = ", bakiye)
        print()
