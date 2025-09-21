import os
import time
from PIL import Image
from fpdf import FPDF
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# --- CONFIG ---
CANVA_URL = "https://www.canva.com/design/DAGyWSxFL7M/XMlfNrAi6jA1ygz8Zovv0Q/view"
NUM_SLIDES = 3   # 👈 Change this to the number of slides
WAIT_TIME = 0.5  # seconds to wait before screenshotting each slide

# --- OUTPUT FOLDER ---
OUTPUT_FOLDER = "canva_slides"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# --- SETUP SELENIUM ---
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

# --- OPEN CANVA ---
driver.get(CANVA_URL)
time.sleep(4)  # wait for Canva to load fully

# Click to focus (so arrow keys work)
actions = ActionChains(driver)
actions.move_by_offset(500, 300).click().perform()

screenshots = []

for i in range(NUM_SLIDES):
    # Save screenshot to the folder
    filename = os.path.join(OUTPUT_FOLDER, f"slide_{i+1}.png")
    driver.save_screenshot(filename)
    screenshots.append(filename)
    print(f"Captured {filename}")
    
    # Go to next slide
    webdriver.ActionChains(driver).send_keys(Keys.ARROW_RIGHT).perform()
    time.sleep(WAIT_TIME)

driver.quit()

# --- CREATE PDF FROM SLIDES (Stretch to Fill Page, No White Bars, No Crop) ---
pdf = FPDF()
pdf.set_auto_page_break(0)

A4_WIDTH, A4_HEIGHT = 210, 297  # mm

for img in screenshots:
    pdf.add_page()
    # Stretch image to completely fill A4 (keeps everything, no borders, no crop)
    pdf.image(img, 0, 0, A4_WIDTH, A4_HEIGHT)

pdf_path = os.path.join(OUTPUT_FOLDER, "canva_slides.pdf")
pdf.output(pdf_path, "F")

print(f"✅ Saved all slides into {pdf_path} (stretched to fill page, no white bars, no crop)")
