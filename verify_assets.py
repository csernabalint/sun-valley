import os

# We will generate index_v2.html with complete content
v2_path = r"c:\Users\csern\Desktop\sun valley\prototypes\sun-valley-b2b\index_v2.html"

# Let's inspect that all assets exist first
assets_dir = r"c:\Users\csern\Desktop\sun valley\prototypes\sun-valley-b2b\assets"
assets = os.listdir(assets_dir)
print(f"Total assets available in {assets_dir}: {len(assets)}")
for a in sorted(assets):
    print("  ", a)
