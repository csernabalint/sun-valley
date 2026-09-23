with open('scripts/compile_v2.py', 'r', encoding='utf-8') as f:
    text = f.read()
    lines = text.splitlines()

output = []
ids_to_check = ['product-list', 'tds-modal', 'sample-request-form', 'sample-product', 'mintakeres', 'kapcsolat']
output.append("=== ID PRESENCE IN HTML ===")
for el in ids_to_check:
    output.append(f'{el}: id="{el}" present -> {f"id=\"{el}\"" in text}')

output.append("\n=== LINES CONTAINING 'minta' OR 'sample' OR 'próba' ===")
for i, line in enumerate(lines, 1):
    low = line.lower()
    if any(k in low for k in ['minta', 'sample', 'próba', 'mintakér', 'tesztminta']):
        output.append(f"Line {i}: {line.strip()}")

with open('scratch/sample_lines_report.txt', 'w', encoding='utf-8') as f:
    f.write("\n".join(output))

print("Report written to scratch/sample_lines_report.txt")
