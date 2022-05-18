from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.uix.progressbar import ProgressBar
import os
from kivy.core.window import Window
from kivy.uix.checkbox import CheckBox

Window.clearcolor = (1, 1, 1, 1)



class Program(App):

    def resimYukle(self,dosya_yolu):
        # Format listesi
        liste = ["png","gif","jpeg","jpg"]

        # Dosyaların listesini alma
        dosyaListesi = os.listdir(r"C:\Users\sherlock\Desktop\yandex-images")
        self.sayac = 0
        self.bar.max = len(dosyaListesi)
        self.bar.value = 0

        # Resim dosyalarını tespit etme
        for i in dosyaListesi:
            if(i.split(".")[-1] in liste):
                self.resimListesi.append(i)

            self.sayac += 1
            self.bar.value = self.sayac

        # Resimlerin yüklenmesi bittikten sonra, görüntüleme ekranını başlatmak üzere
        # self.basla fonksiyonuna git
        self.yukleniyor.text = "SORULAR YÜKLENDİ"
        Clock.schedule_once(self.basla,1.5)

    def build(self):
        self.resimYolu = r"C:\Users\sherlock\Desktop\yandex-images"+os.sep
        self.resimListesi = list()
        self.resimSirasi = 0

        self.yukleniyor = Label(text = "SORULAR YÜKLENİYOR...")
        self.bar = ProgressBar()

        self.govde = BoxLayout(orientation = "vertical")
        self.govde.add_widget(self.yukleniyor)
        self.govde.add_widget(self.bar)


        # Resimleri yüklemek üzere, self.resimYukle fonksiyonuna git
        Clock.schedule_once(lambda event = None:self.resimYukle(self.resimYolu),1)

        return self.govde

    def basla(self,event = None):
        # Ekrandaki tüm araçları kaldırıyoruz
        self.govde.clear_widgets()

        # Ve yeni araçlarımızı ekliyoruz
        self.bilgi = Label(text = "[color=#05f]Yazbel[/color] SORU Görüntüleyici",
                               markup = True,
                               size_hint_y = .1)
        self.resim = Image(source = self.resimYolu+self.resimListesi[0],
                           allow_stretch = True,
                           keep_ratio = True)


        # Geri ve ileri butonlarını taşıyan BoxLayout
        self.butonBar = BoxLayout(size_hint_y = .15)

        self.ileri = Button(text = "ileri",
                            size_hint_x = .2,
                            on_release = self.ileriYukle
                            )

        self.geri = Button(text = "geri",
                           size_hint_x = .2,
                           on_release = self.geriYukle)

        self.butonBar.add_widget(self.geri)
        self.butonBar.add_widget(Widget())
        self.butonBar.add_widget(self.ileri)

        self.govde.add_widget(self.bilgi)
        self.govde.add_widget(self.resim)
        self.govde.add_widget(self.butonBar)

#     CHECKBOX OLUŞTURFUGUM YEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRR

        self.first_check = CheckBox(group='test', size_hint_x=0.95, size_hint_y=0.1, color=[0, 0, 0])
        self.second_check = CheckBox(group='test', size_hint_x=0.95, size_hint_y=0.1, color=[0, 0, 0])
        self.third_check = CheckBox(group='test', size_hint_x=0.95, size_hint_y=0.1, color=[0, 0, 0])
        self.four_check = CheckBox(group='test', size_hint_x=0.95, size_hint_y=0.1, color=[0, 0, 0])
        self.five_check = CheckBox(group='test', size_hint_x=0.95, size_hint_y=0.1, color=[0, 0, 0])

        self.label1 = Label(text='A', color='red', font_size=20, size_hint_x=1.03, size_hint_y=.1)
        self.label2 = Label(text='B', color='red', font_size=20, size_hint_x=1.03, size_hint_y=.1)
        self.label3 = Label(text='C', color='red', font_size=20, size_hint_x=1.03, size_hint_y=.1)
        self.label4 = Label(text='D', color='red', font_size=20, size_hint_x=1.03, size_hint_y=.1)
        self.label5 = Label(text='E', color='red', font_size=20, size_hint_x=1.03, size_hint_y=.1)

        self.govde.add_widget(self.first_check)
        self.govde.add_widget(self.label1)
        self.govde.add_widget(self.second_check)
        self.govde.add_widget(self.label2)
        self.govde.add_widget(self.third_check)
        self.govde.add_widget(self.label3)
        self.govde.add_widget(self.four_check)
        self.govde.add_widget(self.label4)
        self.govde.add_widget(self.five_check)
        self.govde.add_widget(self.label5)



# LABELLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL










    def ileriYukle(self,event = None):
        self.resimSirasi += 1

        # Eğer resim sırası listemizin boyutunu aşmamışsa
        if(self.resimSirasi < len(self.resimListesi)):
            try:
                self.resim.source = self.resimYolu+self.resimListesi[self.resimSirasi]
                self.bilgi.text = self.resimListesi[self.resimSirasi]
            except Exception as e:
                self.bilgi.text = "Yuklenemedi: {}".format(self.resimListesi[self.resimSirasi])

        # Eğer liste boyutunu aşmışsa, bunu sıfırlıyoruz
        else:
            try:
                self.resimSirasi = 0
                self.resim.source = self.resimYolu+self.resimListesi[self.resimSirasi]
                self.bilgi.text = self.resimListesi[self.resimSirasi]

            except Exception as e:
                self.bilgi.text = "Yuklenemedi: {}".format(self.resimListesi[self.resimSirasi])


    def geriYukle(self,event = None):
        self.resimSirasi -= 1

        # Eğer resim sırası listemizin boyutunun altına düşmemişse
        if(self.resimSirasi >= 0):
            try:
                self.resim.source = self.resimYolu+self.resimListesi[self.resimSirasi]
                self.bilgi.text = self.resimListesi[self.resimSirasi]
            except Exception as e:
                print(e)
                self.bilgi.text = "Yuklenemedi: {}".format(self.resimListesi[self.resimSirasi])

        # Eğer düşmüşse, yani negatif olduysa
        # sırayı listenin sonuna alıyoruz
        else:
            try:
                self.resimSirasi = len(self.resimListesi)-1
                self.resim.source = self.resimYolu+self.resimListesi[self.resimSirasi]
                self.bilgi.text = self.resimListesi[self.resimSirasi]
            except Exception as e:
                print(e)
                self.bilgi.text = "Yuklenemedi: {}".format(self.resimListesi[self.resimSirasi])


#Program().run()



