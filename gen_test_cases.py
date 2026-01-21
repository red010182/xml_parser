import os
import random
import string

def gen_random_str(length=8):
    return ''.join(random.choices(string.ascii_letters, k=length))

def save_xml(name, content):
    with open(f"{name}.xml", "w") as f:
        f.write(content)
    print(f"🔥 已產生挑戰案例: {name}.xml")

# 1. 屬性大亂鬥 (測試 Tokenizer 對複雜屬性值的穩定性)
attr_content = "<root>\n"
for i in range(100):
    attrs = " ".join([f"attr_{j}='{gen_random_str(10)}'" for j in range(5)])
    attr_content += f"  <node_{i} {attrs}>Content {i}</node_{i}>\n"
attr_content += "</root>"
save_xml("challenge_attrs", attr_content)

# 2. 地獄深度 2.0 (增加寬度與隨機性，考驗記憶體回收)
def gen_hell_depth(depth=800):
    lines = ["<root>"]
    for i in range(depth):
        # 故意加入不規則空格與換行
        indent = " " * (i % 10)
        lines.append(f"{indent}<layer_{i} type='nest' level='{i}'>")
    lines.append("  <leaf>THE_END</leaf>")
    for i in range(depth-1, -1, -1):
        lines.append(f"</layer_{i}>")
    lines.append("</root>")
    return "\n".join(lines)

save_xml("challenge_depth_800", gen_hell_depth(800))

# 3. 巨量資料測試 (測試串流解析，防止一次性載入導致 OOM)
with open("challenge_massive.xml", "w") as f:
    f.write("<root>\n")
    for i in range(50000):
        f.write(f"  <record id='{i}'>Data block {gen_random_str(20)}</record>\n")
    f.write("</root>")
print("🔥 已產生挑戰案例: challenge_massive.xml")
