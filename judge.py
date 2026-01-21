import subprocess
import time
import glob
import os

LEGACY_EXE = "./expat_cli"
AGENT_EXE = "./agent_expat_cli"

def run_benchmark(exe, input_file):
    try:
        start_time = time.time()
        with open(input_file, 'r') as f:
            result = subprocess.run([exe], stdin=f, capture_output=True, text=True, timeout=15)
        duration = time.time() - start_time
        return result.stdout, duration, result.returncode
    except subprocess.TimeoutExpired:
        return None, 999, -2 # 超時
    except Exception as e:
        return str(e), 0, -1

def main():
    test_files = sorted(glob.glob("*.xml"))
    print(f"{'Test Case':<25} | {'Result':<10} | {'Time (s)':<10}")
    print("-" * 55)

    for xml in test_files:
        ref_out, ref_time, _ = run_benchmark(LEGACY_EXE, xml)
        cur_out, cur_time, ret = run_benchmark(AGENT_EXE, xml)

        status = "FAIL"
        if ret == 0 and ref_out == cur_out:
            status = "PASS"
        elif ret == -2:
            status = "TIMEOUT"

        print(f"{xml:<25} | {status:<10} | {cur_time:.4f}")

if __name__ == "__main__":
    main()
