# python import_slides.py ~/Desktop/PhishingSlides "docs/posts/202601_Trends Cyber Phishing.md"
#python import_slides.py /Users/nfo/OneDrive/CyberTrends2026_EN "docs/posts/202601_Trends Cyber Phishing.md"

import os
import sys
import shutil

def process_slides(exported_folder, markdown_file):
    # Base paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.dirname(os.path.dirname(script_dir))
    images_dir = os.path.join(base_dir, 'docs', 'images')
    
    # Ensure images directory exists
    os.makedirs(images_dir, exist_ok=True)
    
    # Get article name from markdown file (without .md)
    md_basename = os.path.basename(markdown_file)
    article_name, _ = os.path.splitext(md_basename)
    
    # Get all slide images and sort them correctly
    slides = [f for f in os.listdir(exported_folder) if f.startswith('Slide')]
    # Sort logically based on the number directly after "Slide"
    slides.sort(key=lambda x: int(''.join(filter(str.isdigit, x.split('-')[0])) or 0))

    markdown_links = []
    
    for i, slide in enumerate(slides, 1):
        ext = os.path.splitext(slide)[1]
        if not ext:
            ext = '.jpg'
        
        # New clean name: "Article Name-Slide1.jpg"
        new_name = f"{article_name}-Slide{i}{ext}".replace(" ", "_")
        
        src_path = os.path.join(exported_folder, slide)
        dest_path = os.path.join(images_dir, new_name)
        
        # Move and rename the file
        shutil.copy2(src_path, dest_path)
        
        # Create the markdown link (adjust relative path as needed depending on your mkdocs setup)
        # MkDocs usually resolves absolute paths from docs/ or relative paths.
        md_link = f"![Slide {i}](../images/{new_name})"
        markdown_links.append(md_link)
        
        print(f"Moved {slide} -> {new_name}")

    # Append to markdown file
    md_path = os.path.join(base_dir, markdown_file)
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if "<!-- more -->" in content:
        parts = content.split("<!-- more -->", 1)
        new_content = parts[0] + "<!-- more -->\n\n" + "\n\n".join(markdown_links) + "\n" + parts[1]
    else:
        # If no <!-- more --> tag, just append to the end
        new_content = content + "\n\n" + "\n\n".join(markdown_links) + "\n"
        
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"\nSuccessfully added {len(slides)} slides to {markdown_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python import_slides.py <path_to_exported_slide_folder> <path_to_markdown_file>")
        print("Example: python import_slides.py ~/Desktop/MyPresentation docs/posts/202601_Trends_Cyber_Phishing.md")
        sys.exit(1)
        
    process_slides(sys.argv[1], sys.argv[2])
