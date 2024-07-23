# Caesar Cipher :lock::key:

Bu, Caesar Şifreleme tekniğini kullanarak metni kodlamak ve çözmek için bir grafiksel kullanıcı arayüzü (GUI) uygulamasıdır. Uygulama Python ve Tkinter kütüphanesi kullanılarak oluşturulmuştur ve ek olarak art ve Pillow kütüphanelerine bağımlıdır.

## Özellikler
- **Metni Şifrele:** Mesajınızı bir kaydırma değeri kullanarak kodlayın.
- **Metni Çöz:** Aynı kaydırma değerini kullanarak şifrelenmiş mesajınızı çözün.
- **Dinamik Alfabe Genişletme:** Metinde belirli harfler varsa otomatik olarak alfabeyi genişletir.

## Kullanım
1.   Uygulamayı çalıştırın:
```sh
python encrypt-decrypt.py
```
2. GUI Kullanımı:
- **Mesajınızı yazın:** Kodlamak veya çözmek istediğiniz metni sağlanan giriş alanına girin.
- **Kaydırma numarasını yazın:** Caesar Cipher için sayısal kaydırma değerini girin.
- **Encrypt ve Decrypt:** Mesajı kodlamak için "ENCRYPT" butonuna veya mesajı çözmek için "DECRYPT" butonuna tıklayın.
- Sonuç, butonların altındaki metin alanında görüntülenecektir.

&emsp; ![](https://github.com/emrenos/encrypt-decrypt/blob/main/crpyt-gif.gif)

## Kurulum
1. Repoyu klonlayın: 
```sh
git clone https://github.com/emrenos/encrypt-decrypt.git
cd encrypt-decrypt
```
2. Gerekli kütüphaneleri yükleyin:
```sh 
pip install Pillow
```
3. Tkinter'in yüklü olduğundan emin olun:
Tkinter genellikle Python ile birlikte gelir, ancak manuel olarak yüklemeniz gerekirse, paket yöneticinizle bunu yapabilirsiniz. Örneğin:
- &emsp; **On Ubuntu:**
```sh
sudo apt-get install python3-tk
```
- &emsp;  **On macOS with Homebrew:**
```sh
brew install python-tk
```

## Gelecek Güncellemeler
1. **GUI Entegrasyonu** :white_check_mark:
2. **Gelişmiş Şifreleme Yöntemi**: Şifreleme yöntemi, güvenliği artırmak için Caesar Cipher metodundan daha üst bir algoritmaya yükseltilecektir.

##
