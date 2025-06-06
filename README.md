<!--  
Author: Ishwor Prasad Rijal  
Email: ishorprasadrijal@gmail.com  
Contact: [Email Ishwor Prasad Rijal](mailto:ishorprasadrijal@gmail.com)  
-->

# 🚀  Performance Testing Tool

> This project was built to simplify performance testing—even for non-developers! Whether you're testing a login-protected system (e.g., SAML-based) or public URLs, you don’t need to know Python, Locust, or Playwright to run it. After significant research, especially around SAML authentication, I developed this tool to work with almost any web application.

---

### <span style="color: red;">⚠️ WARNING: Unauthorized Testing is Illegal</span>

> <span style="color: red;">🚫 **DO NOT** run performance tests on any site without **explicit permission**. Unauthorized testing may be illegal, unethical, and could breach the site's terms of use.</span>  
>
> <span style="color: red;">✅ Only test systems you own or are explicitly authorized to test.</span>  
>
> 🔍 For more information or questions, contact: [ishorprasadrijal@gmail.com](mailto:ishorprasadrijal@gmail.com)

---

## 📚 Overview

This project enables automated performance testing of web applications by combining:

- 🕷️ **[Locust](https://locust.io/)** — for load testing
- 🎭 **[Playwright for Python](https://playwright.dev/python/)** — for automated browser login and cookie extraction

You can simulate multiple users accessing various endpoints using real, authenticated sessions.

---

## 🎯 Purpose

- ✅ Automate load testing of authenticated and public endpoints
- ✅ Simulate real-user behavior with valid session cookies
- ✅ Automatically handle cookie renewal using Playwright
- ✅ Test multiple endpoints listed in `links.txt`

---

## ⚙️ How It Works

1. **Configuration** via `.env` (stores credentials and cookies).
2. **Login & Cookie Extraction** using Playwright if no valid cookie exists.
3. **Load Testing** with Locust against endpoints from `links.txt`.

---

## 📦 Requirements

- Python 3.8+
- [`locust`](https://locust.io/)
- [`playwright`](https://playwright.dev/python/)
- [`python-dotenv`](https://pypi.org/project/python-dotenv/)

---

## 🚀 Installation

1. **Clone this repository** or copy the project files.

2. **Install dependencies:**

   ```bash
   pip install locust playwright python-dotenv
   playwright install
   ```

3. **Configure `.env` file:**

   ```ini
   BASE_URL=https://your.targetsite.com
   USERNAME=your-email@example.com    # Leave blank if login not required
   PASSWORD=yourpassword              # Leave blank if login not required
   COOKIE=                            # Auto-filled by the script
   ```

4. **Add endpoints in `links.txt`:**

   Each line should contain a path or full URL. Example:

   ```
   /
   /about
   /contact
   ```

---

## 🧪 Usage

1. **Start Locust:**

   ```bash
   locust -f locustfile.py
   ```

2. **Open the Locust Web UI:**

   - Navigate to [http://localhost:8089](http://localhost:8089)
   - Set the number of users and spawn rate
   - Start the test and monitor results

---

## 🧠 How Authentication Works

- On the first run or when the cookie is invalid, Playwright logs in using `.env` credentials.
- It extracts the session cookie and updates the `.env` file.
- All requests during testing use this session cookie.

---

## 🔧 Customization Notes

- If your login page has different input names or button selectors, edit the relevant lines in `locustfile.py`.
- You can leave `USERNAME` and `PASSWORD` blank if login isn’t needed.
- Ensure the `.env` file remains secure and is not shared or committed.

---

## 🆘 Troubleshooting

- **Module not found?**  
  Run: `pip install locust playwright python-dotenv`

- **Login not working?**  
  Double-check:
  - Credentials in `.env`
  - Login selectors in `locustfile.py`
  - Network or site restrictions

---

## 📜 License

This project is for educational, demo, and authorized internal testing purposes only.

---

## 🙋 Contact

For issues, suggestions, or help, feel free to reach out:  
📧 [ishorprasadrijal@gmail.com](mailto:ishorprasadrijal@gmail.com)