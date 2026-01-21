import subprocess
import glob
import os

# 配置區
LEGACY_EXE = "./expat_cli"        # 原始 C 編譯出的執行檔
AGENT_EXE = "./agent_expat_cli"   # 參賽者重構後的執行檔 (如果是 Go 則為 ./main)

def run_cmd(exe, input_file):
    try:
        with open(input_file, 'r') as f:
            result = subprocess.run([exe], stdin=f, capture_output=True, text=True, timeout=5)
            return result.stdout, result.returncode
    except Exception as e:
        return str(e), -1

def main():
    test_files = glob.glob("*.xml")
    total = len(test_files)
    passed = 0

    print(f"🔍 開始驗證重構正確性 (共 {total} 個測試案例)...")
    print("-" * 50)

    for xml in test_files:
        legacy_out, _ = run_cmd(LEGACY_EXE, xml)
        agent_out, ret = run_cmd(AGENT_EXE, xml)

        if ret != 0:
            print(f"❌ {xml:15} | 執行錯誤 (Exit Code: {ret})")
        elif legacy_out == agent_out:
            print(f"✅ {xml:15} | 通過")
            passed += 1
        else:
            print(f"❌ {xml:15} | 輸出不一致 (可能有邏輯錯誤)")
            # 可選：輸出首個不同之處進行偵錯
    
    score = (passed / total) * 100
    print("-" * 50)
    print(f"🏆 最終得分: {score:.2f} / 100 ({passed}/{total})")

if __name__ == "__main__":
    main()
