# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 23:51:09 2022

@author: lenovo
"""

import numpy as np
import pickle
import streamlit as st

#Diğer projeyi bu projeyle birleştiriyor, bağlantı sağlıyor.
#import apriori_ipynb_adlı_dosyanın_kopyası as apr
import projecagrideneme as dnm

#def islem_gonder(islem,urun,guven_degeri,destek_degeri):
 #   #hangi işlemi istiyoruz onu da parametre olarak gönderiyoruz.
  #  sonuc=dnm.main(islem,urun,guven_degeri,destek_degeri)
   # return sonuc




def main():
    #başlık için
    st.title("Market Sepet Analizi")
    urunler_adlari=(dnm.main("urun_adlari"))
    st.subheader('Hangi ürünü hangi ürünün yanına koyarsanız satışlarınız artar? Hesaplayalım :)')
    
    urun=st.selectbox('Hangi ürünün satışını arttırmak istiyorsunuz?', urunler_adlari)
    guven_degeri=st.text_input("Güven değerini giriniz")
    destek_degeri=st.text_input("Destek değerini giriniz")
    islem=st.selectbox('Hangi işlemi yapmak istiyorsunuz?', ['Ürünler hem destek hem de güven değerine göre filtrelensin','Güven değerine göre filtrelensin.','Destek değerine göre filtrelensin.','Ürünün ne kadar satıldığını göreyim.','Tüm ürünlerin satış değerlerini göreyim'])
    
    if islem=='Ürünler hem destek hem de güven değerine göre filtrelensin':
        islem="ikili_filtreleme"
    elif islem=='Güven değerine göre filtrelensin.':
        islem="guvene_gore_filtreleme"
    elif islem=='Destek değerine göre filtrelensin.':
        islem="destege_gore_filtreleme"
    elif islem=='Ürünün ne kadar satıldığını göreyim.':
        islem="urun_nekadar_satilmis"
    else: 
        islem="satis_miktarlari"
    
    sonuc=""
    if st.button('Hesapla'):
        sonuc=dnm.main(islem,urun,guven_degeri,destek_degeri)
    st.success(sonuc)
    
    
if __name__=="__main__":
    main()