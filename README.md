# logsigner-master
5651 sayılı yasa gereğince toplanmış olan logları imzalar. 

Aşağıdaki adımlar pfSense üzerinde yapılmıştır. Tüm Unix/Linux OS'larda imzalama ve doğrulama fonksiyonları çalışır.

logsigner.py hala geliştirme aşamasındadır. 

## Ön Hazırlık (pfSense)

logsigner.py, Python ve Cryptodome kütüphanesine ihtiyaç duyar.
  - /usr/local/etc/pkg/repos/pfSense.conf
  - /usr/local/etc/pkg/repos/FreeBSD.conf
 conf dosyalarında bulunan FreeBSD: { enabled: no } -> FreeBSD: { enabled: yes } olarak değiştirilmelidir.
 
  - pkg install py38-pycryptodomex-3.12.0
  - logsigner.py dosyasının /var/log/ dizini altına kopyalanması (ya da hangi dizinde log imzalanacaksa)

## Kullanım

 logsigner -s  <data>
  
 logsigner -v  signed/<data>

 python3.8 logsigner.py -s \dosyaAdi.bz2 (tekli log imzalama)
  
 python3.8 logsigner.py -s \*.bz2 (coklu log imzalama)
  
 python3.8 logsigner.py -s signed\dosyaAdi.bz2 (coklu log imzalama) 
  
 python3.8 logsigner.py -v signed/\*.bz2 (coklu log dosyası doğrulama)



