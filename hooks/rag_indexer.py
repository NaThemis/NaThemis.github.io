import json
import os
import re
from bs4 import BeautifulSoup

def on_post_build(config, **kwargs):
    """
    Metadata:
    priority: 100
    """
    site_dir = config['site_dir']
    index_data = []

    # Iterate safely through the site directory
    if not os.path.exists(site_dir):
        print(f"Site directory {site_dir} does not exist. Skipping RAG indexing.")
        return

    print("Building RAG index...")
    
    for root, dirs, files in os.walk(site_dir):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                
                # relative path for URL
                rel_path = os.path.relpath(file_path, site_dir)
                
                # Skip some pages (e.g. 404, tags)
                if file in ["404.html", "sitemap.xml", "tags.html"]:
                    continue

                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()

                    soup = BeautifulSoup(content, "html.parser")
                    
                    # Extract Main Content (Material for MkDocs usually puts content in article)
                    # Use a more specific selector to avoid wide pages if needed, but article is standard
                    # Update: Targeted .md-content__inner to ensure we get the full post content
                    article = soup.select_one(".md-content__inner")
                    if not article:
                        article = soup.find("article") # Fallback
                    
                    if not article:
                        print(f"[SKIP] No content found in {rel_path}")
                        continue

                    # Get Title
                    h1 = article.find("h1")
                    title = h1.get_text().strip() if h1 else rel_path

                    # Get Text Content
                    text = article.get_text(separator=" ", strip=True)
                    if len(text) < 100:
                        continue

                    # Create chunks (simple fixed size window)
                    chunk_size = 1000
                    overlap = 100
                    
                    for i in range(0, len(text), chunk_size - overlap):
                        chunk_text = text[i:i + chunk_size]
                        index_data.append({
                            "url": rel_path,
                            "title": title,
                            "content": chunk_text
                        })

                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

    output_path = os.path.join(site_dir, "rag_index.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(index_data, f)
    
    print(f"RAG Index created with {len(index_data)} chunks at {output_path}")
