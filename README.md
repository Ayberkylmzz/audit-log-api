# Audit Log API

Kimin, ne zaman, ne yaptığını kaydeden ve sorgulayan bir REST API — FastAPI ve PostgreSQL ile, katmanlı mimari ve ham SQL kullanılarak (ORM yok) geliştirilmiştir.

## Kullanılan Teknolojiler

- **Python 3.14** + **FastAPI** — web framework
- **uvicorn** — ASGI sunucu
- **PostgreSQL** — veritabanı (ORM kullanılmadan, `psycopg` ile ham SQL)
- **Pydantic** — request/response veri doğrulama
- **pytest** — test

## Mimari

Proje, katmanlı mimari ile yapılandırılmıştır:

```
app/
├── api/            # HTTP route'ları — sadece istek/yanıt
├── schemas/        # Pydantic modelleri (API'nin veri şekli)
├── services/       # iş mantığı
├── repositories/   # ham SQL ile veri erişimi
├── core/           # ortak altyapı: config, DB bağlantısı, kimlik doğrulama
└── main.py         # uygulama giriş noktası
migrations/         # versiyonlanmış SQL şema dosyaları
tests/              # pytest test paketi
```

## Kurulum

1. Repoyu klonla, sanal ortam oluştur:
   ```
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. PostgreSQL'in yerelde çalıştığından emin ol, veritabanını oluştur ve şemayı uygula:
   ```
   createdb audit_log_db
   psql -d audit_log_db -f migrations/001_create_audit_logs_table.sql
   ```

3. `.env.example` dosyasını `.env` olarak kopyala, kendi bilgilerini gir:
   ```
   cp .env.example .env
   ```

4. Sunucuyu çalıştır:
   ```
   uvicorn app.main:app --reload
   ```

5. İnteraktif API dokümantasyonu için: [http://localhost:8000/docs](http://localhost:8000/docs)

## Kimlik Doğrulama

Tüm `/logs` endpoint'leri, `.env`'deki `API_KEY` değeriyle eşleşen bir `X-API-Key` header'ı gerektirir.

## Örnek İstekler

**Yeni bir log kaydı oluşturma**
```
curl -X POST http://localhost:8000/logs \
  -H "Content-Type: application/json" \
  -H "X-API-Key: your-secret-key-here" \
  -d '{"actor":"ayberk","action":"login","resource":"system"}'
```

**Log kayıtlarını listeleme (filtre ve sayfalama ile)**
```
curl "http://localhost:8000/logs?actor=ayberk&limit=10&offset=0" \
  -H "X-API-Key: your-secret-key-here"
```

**Tek bir log kaydını getirme**
```
curl http://localhost:8000/logs/1 \
  -H "X-API-Key: your-secret-key-here"
```

## Testleri Çalıştırma

```
pytest
```
