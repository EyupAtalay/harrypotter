import requests

url = "https://hp-api.onrender.com/api/characters"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    for character in data:
        year_of_birth = character["yearOfBirth"]
        if isinstance(year_of_birth, int) and 0 <= year_of_birth <= 4000:
            print(character['name'] + "\tOynayan aktöri: " +
                  character['actor'] + "\t saç rengi: "+
                  character['hairColour'] + "\tgöz rengi: " +
                  character['eyeColour'] + "\t doğum tarihi: " +
                  str(year_of_birth))
else:
    print("İstek başarısız oldu. Hata kodu:", response.status_code)
