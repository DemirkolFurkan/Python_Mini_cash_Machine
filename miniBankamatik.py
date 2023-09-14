class BankaHesabi:
    
    def __init__(self, hesap):

        self.hesap = hesap
        print('Hesabınız oluşturuldu. Güncel Bakiyeniz = ' , self.hesap[tc]['balance'])
        self.displayAnswer()
    
    def displayAnswer(self):    # İşlemleri ekranda görüntüleyip. İşlem cevabını alıp Methoda gönderildi.

        answer = int(input('Para Çekme (1)\nPara Yatırma (2)\nBakiye Sorgulama (3)\nÇıkış (4)\nİşlem Kodunu Giriniz : '))
        self.processAnswer(answer)

    def processAnswer(self, answer):    # İşlem için verilen cevaplar if ile kontrol edilip gerekli methodlara atandı.
        self.answer = answer
        
        if self.answer == 1:    # Para çekme işlemi
            self.withdrawMoney()
        elif self.answer == 2:  # Para yatırma işlemi
            self.addMoney()     
        elif self.answer == 3:  # Bakiye Sorgulama İşlemi
            self.balanceInquiry()
        elif self.answer == 4:  # Çıkış
            print('İşleminiz Sonlanmıştır...'.upper())
        else:
            print('Geçersiz işlem kodu lütfen tekrar deneyiniz...'.upper())



    def withdrawMoney(self):    # Para Çekme işlemi Gerçekleştirilmiştir. Kullanıcıdan istenilen miktar alınıp Kullanıcının Bakiyesinden eksiltilmiş ve daha sonra bakiye gösterme methoduna aktarılmıştır.
                                # İstenilen miktar yetersiz ise ekrana mesaj verilip tekrar işlem seşme mothoduna yönlendirilmiştir.
        hsp = self.hesap[tc]['balance']
        pull = int(input('Çekmek istediğiniz Tutarı Giriniz : '))

        if hsp < pull:
            print('\nYetersiz Bakiye Lütfen Geçerli Miktar Giriniz.\n'.upper())
            self.displayAnswer()
        elif hsp >= pull:
            total = hsp - pull
            self.hesap[tc]['balance'] = total
            print('\nPara Çekme İşleminiz Gerçekleştirildi.')
            self.balanceInquiry()

    def addMoney(self):     # Para Yatırma işlemi Gerçekleştirilmiştir. işlem gerçekleşince mesajı verip bakiye gösterimi için bakiye methoduna yönlendirilmiştir.

        amount = int(input('Eklenicek Tutarı Giriniz : '))
        total = self.hesap[tc]['balance'] + amount              
        self.hesap[tc]['balance'] = total
        print('\nPara Yatırma işleminiz gerçekleştirilmiştir...')
        self.balanceInquiry()

    def balanceInquiry(self):   # Bakiye Sorgulama işlemi haricinde Para Çekme ve Yatırma işlemlerindede bu methoda yönlendirilmiş daha sonra işleme devam edip etmeyeceğini öğrenmek için farklı methoda yönlendirilmiştir.

        print('\nGüncel Bakiyeniz : '.upper(), self.hesap[tc]['balance'], '\n')
        self.continueProcessing()
        

    def continueProcessing(self):   # Bütün işlemlerden sonra bu methoda yönlendirilip kullanıcının devam edip etmeyeceği bilgisi alınmıştır. ve verilen cevaba göre methoda yönlendirilmiş yada işlem sona ermiştir.

        continueProc = str(input('farklı bir işlem yapmak istiyormusunuz(E/H) : '.upper()))
        if continueProc == 'e' or continueProc == 'E':
            self.displayAnswer()
        elif continueProc == 'H' or continueProc == 'h':
            print('İşleminiz Sona Ermiştir.'.upper())
        else:
            print('Geçersiz İşlem Karakteri Hesabınızdan Çıkış Yapılıyor'.upper())


tc = str(input('Tc Numaranız : '))
name = str(input('Adınız : '))
surname = str(input('Soyadınız : '))
balance = int(input('Aktarılacak Bakiyenizi Giriniz : '))

hesap = {
    tc :{
        'name' : name,
        'surname' : surname,
        'balance' : balance
    }
}

bank = BankaHesabi(hesap)