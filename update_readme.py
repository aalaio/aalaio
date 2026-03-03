import os
import re
from datetime import datetime

def update_readme():
    readme_path = 'README.md'
    # A minimalistic script to inject the last updated timestamp.
    # Can be extended to fetch from Medium/Hashnode/Dev.to blogs.
    
    if not os.path.exists(readme_path):
        print(f"File not found: {readme_path}")
        return

    now_str = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    marker_start = '<!-- LAST_UPDATED_START -->'
    marker_end = '<!-- LAST_UPDATED_END -->'
    
    injection = f"{marker_start}\n*Stats & Profile auto-updated on: {now_str}*\n{marker_end}"
    
    if marker_start in content and marker_end in content:
        pattern = re.compile(rf"{marker_start}.*?{marker_end}", re.DOTALL)
        new_content = re.sub(pattern, injection, content)
    else:
        new_content = content + f"\n\n<!-- LAST_UPDATED: {now_str} -->"
        
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"README updated successfully at {now_str}.")

if __name__ == '__main__':
    update_readme()
