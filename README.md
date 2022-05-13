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

 - logsigner -s  \<data>
  
 - logsigner -v  signed/\<data>

 - python3.8 logsigner.py -s dosyaAdi.bz2 (tekli log imzalama)
  
 - python3.8 logsigner.py -s \*.bz2 (coklu log imzalama)
  
 - python3.8 logsigner.py -v signed/dosyaAdi.bz2 (tekli log dosyası doğrulama) 
  
 - python3.8 logsigner.py -v signed/\*.bz2 (coklu log dosyası doğrulama)
 
 
 Sign işlemini her gün otomatik olarak gerçekleştirmek için cron kullanabilirsiniz.
 
 ### Not: cron işlemini gece 00:00'dan sonra çalıştırmalısınız. O güne ait log dosyası gece 00:00'dan sonra bz olarak kayıt olacak. imza anında logun hangi tarihe ait olduğunu logsigner.py yazacaktır.

## Ekran Görüntüleri

![alt text](https://github.com/kurtserdar/logsigner-master/blob/main/1.png?raw=true)
![alt text](https://github.com/kurtserdar/logsigner-master/blob/main/2.png?raw=true)
![alt text](https://github.com/kurtserdar/logsigner-master/blob/main/3.png?raw=true)
![alt text](https://github.com/kurtserdar/logsigner-master/blob/main/4.png?raw=true)
![alt text](https://github.com/kurtserdar/logsigner-master/blob/main/5.png?raw=true)


