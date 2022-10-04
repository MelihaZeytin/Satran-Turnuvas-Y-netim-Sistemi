# Satranc-Turnuvasi-Yonetim-Sistemi

Bireysel satranç turnuvalarında kullanılmak üzere, Uluslararası Satranç Federasyonu’nun (FIDE) belirlediği İsviçre Sistemi eşleştirme kurallarına benzer kurallara dayalı olarak her turdaki eşleştirmeleri yapmak, turnuva sonunda başarı sıralamasını ve çapraz tabloyu görüntülemek için bir program geliştirilmesi istenmektedir. Bunun için, öncelikle turnuvaya katılan her oyuncu için aşağıdaki bilgiler programa girilecektir:
- Lisans numarası (LNo): 0’dan büyük tekil (unique) tam sayı (0 ya da negatif bir değer girilmesi, başka oyuncu olmadığını belirtecektir.)
- Ad-soyad: programda hepsi büyük harfe çevrilerek ve Türkçe ile uyumlu olarak kullanılmalıdır.
- Uluslararası (FIDE) kuvvet puanı (ELO): 0, 1000 veya daha büyük tam sayı (ELO puanı yoksa 0)
- Ulusal kuvvet puanı (UKD): 0, 1000 veya daha büyük tam sayı (UKD puanı yoksa 0)

Turnuva başlangıcında, tüm oyuncuların turnuva puanları (bundan sonra Puan diye bahsedilecektir) 0’dır. Oyuncular, başlangıçta ve her tur öncesinde eşleştirme amacıyla aşağıdaki ölçütlere göre sıralanırlar (ölçütlerin önceliği aşağı doğru azalmaktadır):
1. Puan (büyükten küçüğe doğru)
2. ELO (büyükten küçüğe doğru)
3. UKD (büyükten küçüğe doğru)
4. Ad-soyad (Türkçe ile uyumlu alfabetik sıra)
5. LNo (küçükten büyüğe doğru)

Başlangıçta, tüm oyuncular yukarıda belirtildiği şekilde sıralanarak bir başlangıç sıralama listesi oluşturulur ve bu listeye göre, eşleştirmelerde kullanılmak üzere oyunculara 1’den başlayarak birer başlangıç sıra numarası (BSNo) verilir. Oluşturulan başlangıç sıralama listesi aşağıdaki şekilde görüntülenir:

![image](https://user-images.githubusercontent.com/109876399/193888477-f47cd360-135b-42fc-bb31-09e31cddfbf0.png)

Daha sonra, turnuvadaki tur sayısı ve başlangıç sıralamasına göre ilk oyuncunun ilk turdaki rengi (b/s) programa girilir. İlk turda, BSNo’su tek olanlar bu rengi, çift olanlar diğer rengi alır. Tur sayısı; oyuncu sayısının 2 tabanına göre logaritmasının, yukarıya doğru en yakın tamsayıya yuvarlanması ile bulunan sayıdan daha az ve oyuncu sayısının 1 eksiğinden daha çok olamaz.
İsviçre Sistemi’nin genel kuralları aşağıdaki şekildedir:
- Elenme yoktur, tüm oyuncular, tüm turlarda oynarlar.
- İki oyuncu birbirleriyle sadece bir defa oynayabilir.
- Birbirleriyle eşleştirilen iki oyuncu, eşit puanlı veya aralarındaki puan farkı olabildiğince az olmalıdır.
- Oyuncu sayısı tek ise, tur öncesi yapılan sıralamada en alttaki oyuncu o turda eşleştirilmez, tur atlar (o turu BYE geçer), rengi yoktur ve 1 puan alır.
- İster rakibi gelmediği için, ister tur atladığı için daha önceki turlarda oynamadan puan almış bir oyuncu, o turda tur atlatılamaz.
- Olanaklı ise, oyuncular bir önceki turdaki renklerinin karşıt rengini alırlar. Olanaklı ise, oyuncular siyah ve beyaz renkleri eşit sayıda alırlar.
- Hiç bir oyuncu arka arkaya üç kez aynı rengi alamaz. Bir oyuncu bir rengi diğerinden en çok 2 kez fazla alabilir.
- Tur atlamalar renk hesabında dikkate alınmaz.

Her tur öncesinde, oyuncular daha önce belirtilen şekilde sıralanır ve ilk oyuncudan başlanarak sırayla, eşleştirilmemiş her oyuncuya uygun bir rakip bulunarak masalara yerleştirilir (masa numaraları (MNo) 1’den başlar). Bunun için, yukarıdaki genel kurallar çerçevesinde, aşağıdaki yöntem izlenir:

1. Rakip aranan oyuncuyla aynı puana sahip oyuncu grubu içerisinde aşağıdaki öncelik sırasına göre rakip ara:

1.1. Rakip aranan oyuncuya bir önceki turda aldığı rengin karşıt rengi verilerek, önceki turda aldığı rengin karşıt rengini alacak, sıralamada en yakın oyuncu

1.2. Rakip aranan oyuncuya bir önceki turda aldığı rengin karşıt rengi verilerek, önceki turda aldığı renkle aynı rengi alacak (renk kurallarına aykırı değilse), sıralamada en yakın oyuncu

1.3. Rakip aranan oyuncuya bir önceki turda aldığı renkle aynı renk verilerek (renk kurallarına aykırı değilse), önceki turda aldığı rengin karşıt rengini alacak, sıralamada en yakın oyuncu

2. Uygun bir rakip bulunamadıysa, bir alt puana sahip oyuncu grubu üzerinde 1.1, 1.2 ve 1.3 adımlarını sırayla tekrarla

3. Uygun bir rakip bulununcaya kadar 2. adımı tekrarla

Bütün eşleştirmeler tamamlandıktan sonra, o turdaki eşleştirme listesi aşağıdaki şekilde görüntülenir (Tur atlayan oyuncu varsa, en sonda belirtilir ve karşısına BYE yazılır):
![image](https://user-images.githubusercontent.com/109876399/193888908-d620f780-3b22-4e10-82db-453a33782070.png)

Daha sonra bu turda oynanan her maçın sonucu, aşağıdaki sayılar (0-5) ile programa girilir:
- 0: beraberlik, yani maç sonucu ½ - ½
- 1: beyaz galip, yani maç sonucu 1 - 0
- 2: siyah galip, yani maç sonucu 0 - 1
- 3: siyah maça gelmemiş, yani maç sonucu + - -
- 4: beyaz maça gelmemiş, yani maç sonucu - - +
- 5: her iki oyuncu da maça gelmemiş, yani maç sonucu - - -

Oyuncuların turnuva sonundaki puanları, maçlarda aldıkları puanların toplanmasıyla belirlenir. Galibiyet için 1 puan, beraberlik için 0,5 puan ve mağlubiyet için 0 puan verilir. Rakibi gelmeyen veya tur atlayan oyuncu 1 puan alır, maça gelmeyen oyuncu 0 puan alır. Turnuva sonunda eşit puan alan oyuncuların sıralamasını belirlemek için aşağıdaki eşitlik bozma ölçütleri uygulanır (ölçütlerin önceliği aşağı doğru azalmaktadır):
- Buchholz-1 alttan (BH-1): En düşük puan alan 1 rakibi dışındaki rakiplerinin aldığı puanların toplamı
- Buchholz-2 alttan (BH-2): En düşük puan alan 2 rakibi dışındaki rakiplerinin aldığı puanların toplamı
- Sonneborn Berger (SB): Yendiği rakiplerin aldıkları puanların ve berabere kaldığı rakiplerin aldıkları puanların yarılarının toplamı
- Galibiyet Sayısı (GS): Oynayarak kazandığı ve rakibinin gelmediği maçların sayısı

BH-1, BH-2 ve SB puanları hesaplanırken, oynanmayan maçlar (tur atlama veya rakibin gelmemesi durumları) için, oyuncunun kendisinin o tura kadar kazandığı puana kalan her tur için 0,5 puan eklenmesiyle bulunan puan dikkate alınır.
Bütün turlar tamamlandıktan sonra, oyuncuların puanları ve yukarıda belirtilen eşitlik bozma ölçütleri dikkate alınarak, 1’den başlayan sıra numaraları (SNo) ile nihai sıralama listesi oluşturulur ve aşağıdaki şekilde görüntülenir:

![image](https://user-images.githubusercontent.com/109876399/193889163-466470c3-bade-4209-9953-163a1e5d3d56.png)

Son olarak, tüm oyuncuların yaptığı maçları gösteren çapraz tablo, başlangıç sıralamasına göre sıralı olarak aşağıdaki şekilde görüntülenir:

![image](https://user-images.githubusercontent.com/109876399/193889221-b07673e7-63d4-4551-82d9-98e816034472.png)

Çapraz tabloda, bir oyuncunun başka bir oyuncuyla eşleştirildiği her tur için; rakip oyuncunun başlangıç sıra numarası, oyuncunun rengi (b/s) ve oyuncu için maçın sonucu aralarında birer boşluk bırakılarak yazılır, maç sonucu için aşağıdaki karakterler kullanılır:
- 1: galibiyet
- 0: mağlubiyet
- ½: beraberlik (½ karakterinin ASCII kodu 171’dir)
- +: rakibi gelmemiş
- -: kendisi gelmemiş
Eğer oyuncu bir turda tur atlamışsa (eşleştirilmemişse), çapraz tabloda o tur için rakip oyuncu ve renk - karakteri ile belirtilirken, maçın sonucu 1 ile belirtilir.

-----------------------

# Input/output

![image](https://user-images.githubusercontent.com/109876399/193891738-1bd5e188-24af-456e-bbe5-b774948321b9.png)
![image](https://user-images.githubusercontent.com/109876399/193891872-357de89b-7844-4256-a5ca-f0c5c9d53579.png)
![image](https://user-images.githubusercontent.com/109876399/193891918-6c4a5f44-9e9d-42e4-9c25-1997bd490881.png)



