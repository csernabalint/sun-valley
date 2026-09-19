import os

root_index = r"c:\Users\csern\Desktop\sun valley\index.html"
root_assets_dir = r"c:\Users\csern\Desktop\sun valley\assets"

print(f"Root index exists: {os.path.exists(root_index)}")
assets = os.listdir(root_assets_dir)
print(f"Total assets available in root {root_assets_dir}: {len(assets)}")
for a in sorted(assets):
    print("  ", a)
