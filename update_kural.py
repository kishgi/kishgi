import requests

API_URL = "https://getthirukkural.appspot.com/api/3.0/kural/rnd"
APP_ID = "3eak6t4vxmmtu"

def fetch_random_kural():
    params = {
        "appid": APP_ID,
        "format": "json"
    }
    response = requests.get(API_URL, params=params)
    response.raise_for_status()
    return response.json()

def update_readme(kural):
    content = f"""\
# 👋 Welcome to My GitHub

<div align="center">

## 📜 **திருக்குறள் இன்று**  
### _Kural of the Day_ — `#{kural['number']}`

<table>
<tr><td>📖 <strong>பால் (Section)</strong></td><td>{kural['paal']}</td></tr>
<tr><td>📚 <strong>இயல் (Subdivision)</strong></td><td>{kural['iyal']}</td></tr>
<tr><td>🏛️ <strong>அதிகாரம் (Chapter)</strong></td><td>{kural['athigaram']}</td></tr>
</table>

---

### 📝 **குறள்:**  
> **{kural['line1']}**  
> **{kural['line2']}**

---

### 🌱 _**Poetic Translation**_  
> *"{kural['translation'].strip()}”*

---

### 🧠 _**Plain Meaning (English)**_  
> {kural['en'].strip()}

---

### 🗣️ _**Explanation (தமிழில்)**_  
> {kural['urai1'].strip()}

</div>

---

🚀 I’m currently working on cool projects. Stay tuned!
"""

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    kural = fetch_random_kural()
    update_readme(kural)
