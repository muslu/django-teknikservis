# -*- coding: utf-8 -*-

from django.contrib import admin
from servisformu.models import Teknisyen, Musteriler, Durumlar, Aksesuarlar, ServisForm, Urunler

class TeknisyenAdmin(admin.ModelAdmin):
    list_display            =       ['Aktif', 'AdSoyad', 'Yazdir', 'EkAlanTest']
    list_per_page           =       20
    exclude                 =       ( 'KayitTarihi', )

    list_filter             =       ['Aktif', 'AdSoyad', ]
    search_fields           =       ['AdSoyad', ]
    date_hierarchy          =       'KayitTarihi'




    # def has_add_permission(self, request):
    #     try:
    #         if not request.user.is_superuser:
    #             try:
    #                 KayitSayisi         =   self.model.objects.count()
    #             except:
    #                 KayitSayisi         =   0
    #             KalanLimit          =   2
    #
    #             if KayitSayisi      >=  KalanLimit:
    #                 return False
    #             else:
    #                 return True
    #     except:
    #         return True
    #
    # def get_list_display(self, request):
    #     g_l     =   super(TeknisyenAdmin, self).get_list_display(request)
    #
    #     try:
    #         if not request.user.is_superuser:
    #             g_l.remove('user')
    #     except:
    #         pass
    #     return g_l



def SecilileriGuncelle(modeladmin, request, queryset):
    print queryset.query
    for k in queryset:
        if k.Yetkili.startswith("Muslu"):
            k.Yetkili = k.Yetkili + u"___Musluilebaşlıyordu"
        k.save()
    return ""
SecilileriGuncelle.short_description = u"Seçilileri Güncelle"


class MusterilerAdmin(admin.ModelAdmin):
    list_display            =       ( 'Kodu', 'Unvan', 'Yetkili', 'Aktif', 'AramaYap')
    list_per_page           =       80
    exclude                 =       ( 'KayitTarihi', )
    search_fields           =       ( 'Yetkili', 'Unvan' )
    list_display_links = ('Unvan', 'Yetkili')
    actions                 =       (SecilileriGuncelle,)
    actions_on_bottom       =       True
    actions_on_top          =       True



class DurumlarAdmin(admin.ModelAdmin):
    list_display            =       ('Durumu',)
    list_per_page           =       80


class AksesuarlarAdmin(admin.ModelAdmin):
    list_display            =       ('Adi',)
    list_per_page           =       5


class UrunlerInline(admin.StackedInline):
    model                   =       Urunler
    extra                   =       0
    max_num                 =       5



class ServisFormAdmin(admin.ModelAdmin):
    inlines                 =       [ UrunlerInline, ]
    list_display            =       ( 'FormNo', 'Musteri', 'TeslimEden', 'TeslimAlan', 'KayitTarihi', 'Yazdir' )
    list_per_page           =       50
    ordering                =       ( '-KayitTarihi', )
    date_hierarchy          =       'KayitTarihi'
    search_fields           =       ( 'FormNo', 'Musteri__Yetkili', 'Musteri__Telefon' )
    exclude                 =       ( 'KayitTarihi', )


    def formfield_for_foreignkey(self, db_field, request, **kwargs):

        if db_field.name == 'TeslimAlan':
            kwargs["queryset"] = Teknisyen.objects.filter(Aktif=True)

        if db_field.name == 'Musteri':
            kwargs["queryset"] = Musteriler.objects.filter(Aktif=True)

        return super(ServisFormAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)



admin.site.register(ServisForm, ServisFormAdmin)
admin.site.register(Aksesuarlar, AksesuarlarAdmin)
admin.site.register(Durumlar, DurumlarAdmin)
admin.site.register(Musteriler, MusterilerAdmin)
admin.site.register(Teknisyen, TeknisyenAdmin)