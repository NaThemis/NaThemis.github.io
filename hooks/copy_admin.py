import os
import shutil

def on_post_build(config, **kwargs):
    """
    Copy admin-dashboard.html to the site output directory
    so it's accessible directly but completely ignored by MkDocs navigation/search.
    """
    source_file = os.path.join(config['docs_dir'], '../overrides/admin-dashboard.html')
    target_dir = os.path.join(config['site_dir'], 'admin-dashboard')
    target_file = os.path.join(target_dir, 'index.html')

    # Ensure the target directory exists
    os.makedirs(target_dir, exist_ok=True)

    if os.path.exists(source_file):
        shutil.copy2(source_file, target_file)
        print(f"Successfully copied Admin Dashboard to {target_file}")
    else:
        print(f"Warning: Admin Dashboard source not found at {source_file}")
