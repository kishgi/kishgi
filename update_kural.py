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
<div align="left">

> "**{kural['line1']}**  
> **{kural['line2']}**" — *குறள் {kural['number']}*

</div>

**பொருள்:**  
{kural['urai1'].strip()}

**Meaning (English):**  
{kural['en'].strip()}


## 
### Who am I?
Hi! I'm Kishgi - Software Engineering undergraduate passionate about DevOps and DevSecOps.  
- 🔧 Passionate about **DevOps, Cloud, and Infrastructure Automation**  
- ⚡ Focused on building **reliable CI/CD pipelines** and automating workflows   
- 💻 Exploring **cloud-native solutions** and **secure deployment practices** 

### Tools of my trade?
- **DevOps:** Docker, Kubernetes, Ansible, Terraform, Jenkins, GitHub Actions, GitLab 
- **DevSecOps:** SonarQube, Trivy, Prometheus, Grafana 
- **Cloud:** AWS, Azure
- **Programming & Scripting:** Python, Bash, JavaScript  


[![](https://img.shields.io/badge/linkedin-0a66c2)](http://linkedin.com/in/kishgi) [![](https://img.shields.io/badge/portfolio-8A2BE2)](http://kishgi.vercel.app)

</pre>

*“Thirukkural is not just literature - it's a life manual. Come again tomorrow for another one”*
"""

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    kural = fetch_random_kural()
    update_readme(kural)
