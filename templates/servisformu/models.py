# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import timezone

from django.db import models






class Teknisyen ( models.Model ) :
    Aktif               =       models.BooleanField(default = 1)
    AdSoyad             =       models.CharField ( u'Adı Soyadı', max_length = 250 )
    KayitTarihi         =       models.DateField ( u"Kayıt Tarihi", default=timezone.now)

    def __unicode__(self):
        return self.AdSoyad

    class Meta:
        verbose_name_plural             =       u"Teknisyenler"
        verbose_name                    =       u"Teknisyen"


    def Yazdir ( self ) :
        return '<a href="/yazdir/%s" target="_blank">Yazdır</a>' % self.id
    Yazdir.short_description       =       u'Yazdır'
    Yazdir.allow_tags              =       True

    def EkAlanTest(self):
        return self.AdSoyad.replace(' ', '_______')
    EkAlanTest.short_description       =       u'Burası alanın başlığı'




import random,  string

class Musteriler ( models.Model ) :
    Aktif               =       models.BooleanField(default = 1)
    Kodu                =       models.CharField ( u'Müşteri Kodu', default=''.join(random.choice(string.digits) for x in range(8)), max_length = 8 )
    Unvan               =       models.CharField ( u'Ticari Ünvan', max_length = 250 )
    Yetkili             =       models.CharField ( u'Yetkili Adı Soyadı', max_length = 250 )
    Telefon             =       models.CharField ( u'Telefon', max_length = 13, blank = True )
    KayitTarihi         =       models.DateField ( u"Kayıt Tarihi", default=timezone.now)

    def __unicode__(self):
        # return self.Kodu + " " + self.Yetkili
        return "Müşteri Kodu: %s - Adı: %s" % (self.Kodu, self.Yetkili)

    class Meta:
        verbose_name_plural             =       u"Müşteriler"
        verbose_name                    =       u"Müşteri"


    def AramaYap ( self ) :
        if self.Telefon:
            return '<a href="tel:%s" target="_blank">Numarayı Ara</a>' % self.Telefon
        else:
            return 'Telefon No kayıt edilmedi'

    AramaYap.short_description       =       u'Ara'
    AramaYap.allow_tags              =       True



class Durumlar (models.Model ):
    Durumu              =       models.CharField(u'Durum', max_length=30, help_text='Metin alanının altında kayıt girerken yardımcı olabilecek konuları anlatan kısa bir açıklama yazabilirsiniz.')

    def __unicode__(self):
        return self.Durumu

    class Meta:
        verbose_name_plural             =       u"Durumlar"
        verbose_name                    =       u"Durum"



class Aksesuarlar (models.Model ):
    Adi              =       models.CharField(u'Adi', max_length=30, help_text='Ürünle beraber getirilen tüm aksesuarlar. Örn: Batarya, Çanta' )

    def __unicode__(self):
        return self.Adi

    class Meta:
        verbose_name_plural             =       u"Aksesuarlar"
        verbose_name                    =       u"Aksesuar"




class ServisForm ( models.Model ) :
    Musteri             =       models.ForeignKey ( Musteriler )
    TeslimEden          =       models.CharField ( u'Teslim Eden', max_length = 130 )
    # TeslimAlan          =       models.ForeignKey ( Teknisyen, default=int(Teknisyen.objects.get(id=1).id)  )
    TeslimAlan          =       models.ForeignKey ( Teknisyen  )
    FormNo              =       models.CharField ( u'Form No', default=''.join(random.choice(string.digits) for x in range(8)), max_length = 8 )
    KayitTarihi         =       models.DateTimeField ( u"Kayıt Tarihi", default=timezone.now)

    def __unicode__(self):
        return self.FormNo

    class Meta:
        verbose_name_plural             =       u"Formlar"
        verbose_name                    =       u"Servis Formu"

    def Yazdir ( self ) :
        return '<a href="/yazdir/%s" target="_blank">Yazdır</a>' % self.id
    Yazdir.short_description       =       u'Yazdır'
    Yazdir.allow_tags              =       True




class Urunler ( models.Model ) :
    ServisFormu         =       models.ForeignKey ( ServisForm )
    Cins                =       models.CharField ( u'Cinsi', max_length = 30 )
    Marka               =       models.CharField ( u'Marka', max_length = 50 )
    Model               =       models.CharField ( u'Model', max_length = 50 )
    SeriNo              =       models.CharField ( u'Seri No', max_length = 250 )
    GarantiBitis        =       models.DateField ( u"Garanti Bitiş", default=timezone.now )
    Sikayet             =       models.TextField ( u'Şikayet' )
    Aksesuar            =       models.ManyToManyField ( Aksesuarlar, blank=True )
    Durum               =       models.ForeignKey ( Durumlar )
    Not                 =       models.TextField ( u'Yapılan İşlemler', blank=True )
    TeslimatTarihi      =       models.DateField ( u"Teslimat Tarihi", default=timezone.now, blank=True )
    def __unicode__(self):
        return "%s %s %s" % (self.Cins, self.Marka, self.Model)

    class Meta:
        verbose_name_plural             =       u"Ürünler"
        verbose_name                    =       u"Ürün"
