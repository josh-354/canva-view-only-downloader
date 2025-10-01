## 📦 Requirements
- **Python 3.8+**
- Install dependencies:
  ```bash
  pip install pillow fpdf selenium
Google Chrome installed

ChromeDriver installed (must match your Chrome version)

🔽 How to Get ChromeDriver
Find your Chrome version:

Open Chrome → go to chrome://settings/help

Download the matching ChromeDriver from here:
👉 Download ChromeDriver

Extract the file and place the chromedriver executable in the same folder as your Python script
(e.g. canva_to_pdf.py and chromedriver.exe should be in the same directory).

✅ Example:

Copy code
project/
├── canva_to_pdf.py
├── chromedriver.exe
└── README.md
⚡ Alternative (Automatic Installation)
Instead of downloading manually, you can install it automatically:

bash
Copy code
pip install webdriver-manager
(If you use webdriver-manager, you don’t need to keep chromedriver.exe in the folder.)

⚙️ What to Change in the Code
Inside the script, look for these variables and update them:

python
Copy code
# Canva presentation link (replace with your own)
CANVA_URL = "https://www.canva.com/design/XXXX/view"

# Total number of slides in your Canva presentation
NUM_SLIDES = 64  

# Time (in seconds) to wait before capturing the next slide
WAIT_TIME = 0.5  

# Folder where screenshots and PDF will be saved
OUTPUT_FOLDER = "canva_slides"  