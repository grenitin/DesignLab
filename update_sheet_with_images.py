import gspread
import subprocess
import os

CREDENTIALS_FILE = 'credentials.json'
SPREADSHEET_URL = 'https://docs.google.com/spreadsheets/d/1dYj9RUoNNPSyGjJ_A9yP5AFsM4i1SQB3y9M0drY45tg/edit?usp=sharing'
IMAGE_DIR = '/Users/ni3_kr/.gemini/antigravity/brain/7057c040-8e22-4f57-ac0f-6057c127f06f/'

def upload_to_catbox(filepath):
    print(f"Uploading {os.path.basename(filepath)}...")
    cmd = ["curl", "-s", "-F", "reqtype=fileupload", "-F", f"fileToUpload=@{filepath}", "https://catbox.moe/user/api.php"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0 and result.stdout.startswith("http"):
        return result.stdout.strip()
    else:
        print(f"Failed to upload: {result.stdout}")
        return None

def main():
    print("Connecting to Google Sheets...")
    gc = gspread.service_account(filename=CREDENTIALS_FILE)
    sh = gc.open_by_url(SPREADSHEET_URL)
    worksheet = sh.sheet1

    # Find the images
    image_files = sorted([f for f in os.listdir(IMAGE_DIR) if f.endswith('.png')])
    
    # Let's map them to rows 2 through 11 (10 rows of data). 
    # If we fall short of 10 images, we'll loop them.
    if not image_files:
        print("No images found!")
        return

    # Update Headers in column J and K
    worksheet.update_acell('J1', 'Referenced Page')
    worksheet.update_acell('K1', 'Screenshot')

    # Prepare data for columns J and K
    j_col_data = [] # Page URLs
    k_col_data = [] # Image Formulas

    for i in range(10): # For the 10 heuristics
        img_idx = i % len(image_files)
        img_path = os.path.join(IMAGE_DIR, image_files[img_idx])
        
        # Upload
        img_url = upload_to_catbox(img_path)
        
        page_url = "https://www.cardekho.com/carmodels/Tata/Tata_Sierra"
        formula = f'=IMAGE("{img_url}")' if img_url else ""
        
        j_col_data.append([page_url])
        k_col_data.append([formula])
        
    print("Writing URLs to Google Sheet...")
    # Update Range J2:J11
    worksheet.update(values=j_col_data, range_name='J2:J11')
    
    print("Writing IMAGES to Google Sheet...")
    # Update Range K2:K11, we pass raw=False to evaluate the formula
    worksheet.update(values=k_col_data, range_name='K2:K11', raw=False)
    
    print("Done! Check your Google Sheet!")

if __name__ == "__main__":
    main()
