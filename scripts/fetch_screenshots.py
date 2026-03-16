import os
import re
import requests
import time

def process_files():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    posts_dir = os.path.join(base_dir, "posts")
    images_dir = os.path.join(base_dir, "images")
    
    os.makedirs(images_dir, exist_ok=True)
    
    # We only want to process the 13 files we generated. We can filter by those that have "20" (year)
    files = [f for f in os.listdir(posts_dir) if f.endswith(".md") and f != "20250901_AIAgents&Data Platforms.md" and f != "20260101_Trends Cyber Phishing.md"]
    
    # regex to find the first http link in the file
    link_pattern = re.compile(r'\]\((https?://[^\)]+)\)')
    
    for filename in sorted(files):
        print(f"Processing {filename}...")
        filepath = os.path.join(posts_dir, filename)
        
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Extract slug
        slug_match = re.search(r'slug:\s*(.+)', content)
        if not slug_match:
            continue
        slug = slug_match.group(1).strip()
        
        # Extract the first URL at the bottom (after the intro)
        # We can just search for the first http link
        links = link_pattern.findall(content)
        if not links:
            print(f"  No link found in {filename}")
            continue
            
        target_url = links[0]
        print(f"  Found URL: {target_url}")
        
        # Check if already has an image above <!-- more -->
        if f"../images/{slug}.png" in content or f"../images/{slug}.jpg" in content:
            print(f"  Image already exists in {filename}, skipping.")
            continue
            
        # Get screenshot via microlink
        api_url = f"https://api.microlink.io/?url={target_url}&screenshot=true&meta=false"
        try:
            resp = requests.get(api_url, timeout=30)
            data = resp.json()
            if data.get("status") == "success" and data.get("data", {}).get("screenshot"):
                img_url = data["data"]["screenshot"]["url"]
                
                # Download the image
                img_resp = requests.get(img_url, timeout=30)
                img_path = os.path.join(images_dir, f"{slug}.png")
                with open(img_path, "wb") as f_img:
                    f_img.write(img_resp.content)
                
                print(f"  Saved screenshot to {slug}.png")
                
                # Insert the link above <!-- more -->
                img_markdown = f"![Screenshot](../images/{slug}.png)\n\n"
                new_content = content.replace("<!-- more -->", img_markdown + "<!-- more -->")
                
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"  Updated markdown file.")
            else:
                print(f"  Failed to get microlink screenshot for {target_url}: {data}")
        except Exception as e:
            print(f"  Error processing {filename}: {e}")
            
        # sleep slightly to avoid rate limiting
        time.sleep(2)

if __name__ == "__main__":
    process_files()
