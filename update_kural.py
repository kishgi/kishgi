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
<div align="center">

### 📝 குறள் {kural['number']}

> **{kural['line1']}**  
> **{kural['line2']}**

</div>

---

**Meaning (தமிழில்):**  
{kural['urai1'].strip()}

**Meaning (English):**  
{kural['en'].strip()}

---

## 👋 About Me

Hi! I'm Kishgi — a developer who appreciates clean code, culture, and creativity.  
I'm currently working on a few cool personal projects and learning more about DevOps and open source.  
Stay tuned for more updates!

📫 You can reach me at: [your-email@example.com]  
🌐 Portfolio: [https://your-portfolio-link.com](https://your-portfolio-link.com)

---

🕉️ *“Thirukkural is not just literature — it's a life manual.”*
"""

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    kural = fetch_random_kural()
    update_readme(kural)
