import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

hero_match = re.search(r'<h1.*?>(.*?)</h1>', text, re.DOTALL)
if hero_match:
    print('Hero H1:')
    for line in hero_match.group(1).splitlines():
        if line.strip():
            print(' ', line.strip())

print('\nR&D step badges:')
rd_badges = re.findall(r'style="background-color:\s*([^;]+);"[^>]*>\s*(\d+)\s*</div>', text)
for color, num in rd_badges:
    print(f'Step {num}: {color}')
