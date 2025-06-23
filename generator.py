import os
from dotenv import load_dotenv
from openai import OpenAI

dotenv_path = "C:/Users/26027317/PycharmProjects/QualityImprover/.env"
load_dotenv(dotenv_path=dotenv_path)

api_key = os.getenv("OPENAI_API_KEY")
print("🔑 OpenAI API Key:", api_key)

if not api_key:
    raise ValueError("API key bulunamadı! Lütfen .env dosyasını ve anahtarı kontrol et.")

client = OpenAI(api_key=api_key)

def build_prompt(data: dict) -> str:
    return f"""
### Özellik Adı
{data['name']}

### Amaç
{data['purpose']}

### Nasıl Çalışır?
{data['how_it_works']}

### Kullanıcıya Ne Gösterilir?
{data['user_facing']}

### Olmaması Gerekenler
{data['not_expected']}

### Donanım / Yazılım Kısıtları
{data['constraints']}

### Kabul Kriteri / Test Senaryosu
{data['acceptance']}

---
Yukarıdaki bilgilerle aşağıdaki başlıklarda profesyonel bir Gereksinim Dokümanı oluştur:

1. Özellik Tanımı  
2. Fonksiyonel Gereksinimler  
3. Fonksiyonel Olmayan Gereksinimler  
4. Kısıtlar  
5. Kabul Kriterleri  
6. İzlenebilirlik
"""

def generate_requirements(inputs: dict) -> str:
    response = client.chat.completions.create(
        model="gpt-4o",  # istersen gpt-3.5-turbo da olur
        messages=[
            {"role": "system", "content": "Profesyonel bir ürün yöneticisi olarak gereksinim dokümanı oluştur."},
            {"role": "user", "content": build_prompt(inputs)}
        ],
        temperature=0.4,
    )
    return response.choices[0].message.content.strip()
