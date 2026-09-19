import os
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
root_index = REPO_ROOT / "index.html"
root_assets_dir = REPO_ROOT / "assets"

print(f"Root index exists: {os.path.exists(root_index)}")
assets = os.listdir(root_assets_dir)
print(f"Total assets available in root ({root_assets_dir}): {len(assets)}")
for a in sorted(assets):
    print("  ", a)
