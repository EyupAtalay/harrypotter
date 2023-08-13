from PIL import Image
from io import BytesIO
import requests

url = "https://www.webtekno.com/images/editor/default/0003/68/3fb8233a7b94477c001fcb6672a8a164f27067df.jpeg"  # Görüntüyü açmak istediğiniz URL'yi buraya yazın

try:
    response = requests.get(url)
    response.raise_for_status()  # Ağ isteği hatalarını kontrol edin
    image = Image.open(BytesIO(response.content))
    image.show()
except requests.RequestException as e:
    print("Ağ isteği hatası:", e)
except Exception as e:
    print("Hata:", e)
