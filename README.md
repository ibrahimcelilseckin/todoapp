# Todo App

Bu, basit bir Todo uygulamasıdır. Kullanıcılar, yapılacak işleri ekleyebilir, tamamlanmış işleri işaretleyebilir ve silebilirler. Uygulama Flask web framework'ü kullanılarak geliştirilmiştir.

## Özellikler

- Yeni Todo (yapılacak iş) ekleyebilme
- Todo'yu tamamlanmış olarak işaretleyebilme
- Todo'yu geri alabilme (tamamlanmış işin geri alınması)
- Todo'yu silebilme
- Basit ve kullanıcı dostu arayüz

## Teknolojiler

- **Flask**: Python tabanlı web framework
- **HTML/CSS**: Kullanıcı arayüzü için temel yapı ve stil
- **SQLite/PostgreSQL**: Veritabanı (seçime bağlı)
- **JavaScript (isteğe bağlı)**: Dinamik içerik için (animasyonlar, AJAX vb.)
  
## Kurulum

### Gereksinimler

- Python 3.x
- Pip (Python paket yöneticisi)

### Adımlar

1. **Repo'yu klonla**:
    ```bash
    git clone https://github.com/<ibrahimcelilseckin>/todo-app.git
    cd todo-app
    ```

2. **Gerekli paketleri yükle**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Veritabanını başlat** (SQLite ya da PostgreSQL seçimine göre):
    - Eğer SQLite kullanıyorsanız, veritabanı otomatik olarak oluşturulacaktır.
    - Eğer PostgreSQL kullanıyorsanız, `config.py` dosyasındaki veritabanı ayarlarını yapılandırarak `flask db init` komutunu çalıştırabilirsiniz.

4. **Uygulamayı başlat**:
    ```bash
    flask run
    ```

    Bu komut, uygulamanızı yerel sunucuda çalıştıracak ve [http://localhost:5000](http://localhost:5000) adresinde erişilebilir olacaktır.

## Kullanım

- **Todo Ekleme**: Uygulamanın ana sayfasındaki input alanına yeni bir todo girip "Ekle" butonuna tıklayın.
- **Todo Tamamlandı**: Bir todo'nun tamamlandığını işaretlemek için "Tamamlandı" butonuna tıklayın.
- **Todo Geri Al**: Tamamlanmış bir todo'yu geri almak için "Geri Al" butonuna tıklayın.
- **Todo Silme**: Bir todo'yu silmek için çöp kutusu simgesine tıklayın.

## Katkıda Bulunma

1. Bu repo'yu kendi bilgisayarınıza klonlayın:
    ```bash
    git clone https://github.com/<kullanıcı_adı>/todo-app.git
    ```

2. Yeni bir branch oluşturun:
    ```bash
    git checkout -b yeni-ozellik
    ```

3. Yapmak istediğiniz değişiklikleri gerçekleştirin ve commit edin:
    ```bash
    git add .
    git commit -m "Yapılacak iş ekleme özelliği"
    ```

4. Değişikliklerinizi GitHub'a gönderin:
    ```bash
    git push origin yeni-ozellik
    ```

5. GitHub üzerinden bir pull request (PR) oluşturun.

## Lisans

Bu proje [MIT Lisansı](LICENSE) ile lisanslanmıştır.
