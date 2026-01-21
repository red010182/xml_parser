import os

def save_xml(name, content):
    with open(f"{name}.xml", "w") as f:
        f.write(content)
    print(f"✅ 已產生: {name}.xml")

# 1. 基礎測試
save_xml("test_basic", "<root><a/><b/><c>Hello</c></root>")

# 2. 複雜屬性測試 (考驗 Tokenizer 對引號與空格的處理)
save_xml("test_attr", '<root><node id="1" class="main" data-ptr="0x123">Content</node></root>')

# 3. 地獄深度測試 (考驗 Stack 與 Context 管理)
def gen_deep(depth=500):
    lines = ["<root>"]
    for i in range(depth):
        lines.append(f"{'  '*(i+1)}<layer_{i} index='{i}'>")
    lines.append(f"{'  '*(depth+1)}DEEP_CONTENT")
    for i in range(depth-1, -1, -1):
        lines.append(f"{'  '*(i+1)}</layer_{i}>")
    lines.append("</root>")
    return "\n".join(lines)

save_xml("test_deep", gen_deep(500))

# 4. 特殊字元測試 (考驗 Entity 處理)
save_xml("test_special", "<root><data> &lt; &gt; &amp; &quot; &apos; </data></root>")
