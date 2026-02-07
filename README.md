# 🚀 XML 核心引擎轉生挑戰賽 (C to Modern Language)

## 1. 專案背景

本專案基於全球最知名的 XML 解析庫 **Expat**。Expat 是一個採用 C 語言編寫、基於事件驅動（Stream-oriented）的解析引擎，被廣泛應用於 Mozilla、Python、PHP 等核心專案中。

這是一場考驗 **「AI Agent 協作」** 與 **「複雜 Context 管理」** 的競賽。你將面對約 **12,000 行** 密集的 C 語言代碼，你的任務是利用 AI 工具將其重構成 **Go** 或 **Rust**。

---

## 2. 挑戰難度：為什麼你不能直接複製貼上？

這不是簡單的語法翻譯，這套系統具備以下難點：

* **深層狀態機**：`xmlparse.c` 維護了一個極度複雜的解析狀態機。
* **低階位元組操作**：`xmltok.c` 處理了多種字元編碼（UTF-8, UTF-16, ISO-8859-1）的底層切分。
* **Context 溢出陷阱**：由於代碼總量大且模組間高度耦合，一次性將代碼餵給 AI 會導致邏輯幻覺。你必須展示如何分段、分模組地引導 AI 建立正確的「介面契約」。

---

## 3. 快速開始

### 編譯 C 語言基準版本

在參賽前，請先確保你能編譯並執行原始版本，作為你的測試基準：

```bash
make
```

### 驗證原始版本

```bash
echo '<root><node>Hello AI</node></root>' | ./expat_cli
```

---

## 4. 任務規格 (Specification)

### 目標

1. **語言**：使用 **Go 1.2x+** 或 **Rust 1.7x+**。
2. **介面**：維持純 CLI 模式，讀取 `STDIN`，輸出 `STDOUT`。
3. **輸出格式**：必須與 `expat_cli` 的標籤輸出格式 100% 一致。
* `START: tag_name`
* `END: tag_name`
* 如果有屬性，需依照 C 版順序印出 `ATTR: key = value`。



### 嚴禁行為

* 禁止直接調用語言內建的高階 XML 庫（如 `encoding/xml` 或 `serde-xml`）。
* 必須保留原有的 Tokenizer、Role Parser 與 State Machine 的分層邏輯。

---

## 5. 自動化測試與評分

Repo 內附帶了專業的測試工具，請務必在提交前跑過所有案例：

1. **產生測試案例**：
```bash
python3 gen_test_cases.py
```


2. **執行自動評分**：
將你編譯好的程式命名為 `agent_expat_cli`，然後執行：
```bash
python3 judge.py
```



### 測試案例說明：

* `challenge_attrs.xml`: 測試多重屬性與複雜空白處理。
* `challenge_depth_800.xml`: **地獄級難度**。測試標籤棧（Stack）是否會溢位，以及層級邏輯是否正確。
* `challenge_massive.xml`: 測試大型檔案的串流解析效能與記憶體回收。

---


## 6. 目錄結構

* `main.c`: 題目入口程式。
* `Makefile`: 編譯指令。
* `gen_test_cases.py`: 高難度資料產生器。
* `judge.py`: 自動評分與效能分析腳本。

---

**準備好接受挑戰了嗎？讓 AI 成為你的副駕駛，帶領這套經典引擎進入現代語言的世界吧！**


```
cargo install cargo-llvm-cov
rustup component add llvm-tools-preview
```
