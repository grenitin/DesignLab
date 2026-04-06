import os
import subprocess
import pandas as pd

CARDEKHO_IMG_DIR = '/Users/ni3_kr/.gemini/antigravity/brain/7057c040-8e22-4f57-ac0f-6057c127f06f/'
URL1 = 'UX Audit/CarDekho_UX_Audit_-_Heuristic_Evaluation.csv'
URL2 = 'UX Audit/BikeDekho_UX_Audit_-_Heuristic_Evaluation.csv'

def upload_to_catbox(filepath):
    print(f"Uploading {os.path.basename(filepath)}...")
    cmd = ["curl", "-s", "-F", "reqtype=fileupload", "-F", f"fileToUpload=@{filepath}", "https://catbox.moe/user/api.php"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0 and result.stdout.startswith("http"):
        return result.stdout.strip()
    return ""

def main():
    print("Fixing CarDekho Images...")
    df_car = pd.read_csv(URL1)
    
    # We have some images, let's map them. Missing ones will just stay empty instead of the placeholder.
    images = sorted([f for f in os.listdir(CARDEKHO_IMG_DIR) if f.endswith('.png')])
    for idx, row in df_car.iterrows():
        if idx < len(images):
            img_path = os.path.join(CARDEKHO_IMG_DIR, images[idx])
            catbox_url = upload_to_catbox(img_path)
            if catbox_url:
                df_car.at[idx, 'Screenshot'] = f'=IMAGE("{catbox_url}")'
            else:
                df_car.at[idx, 'Screenshot'] = ""
        else:
            df_car.at[idx, 'Screenshot'] = ""
    
    df_car.to_csv(URL1, index=False)
    
    print("Fixing BikeDekho Images (Removing placeholders)...")
    df_bike = pd.read_csv(URL2)
    for idx, row in df_bike.iterrows():
        df_bike.at[idx, 'Screenshot'] = ""  # We don't have real images for BikeDekho yet
    
    df_bike.to_csv(URL2, index=False)
    print("Done generating corrected CSVs!")

if __name__ == '__main__':
    main()
