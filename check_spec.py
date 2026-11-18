import json
import sys
import requests

BMC = "http://127.0.0.1:8000"
SYSTEM = "/redfish/v1/Systems/437XR1138R2"

# 1. 讀取規格（模擬向 MES 查訂單規格）
with open("spec.json") as f:
    spec = json.load(f)

# 2. 透過 BMC 讀取實際狀態
data = requests.get(BMC + SYSTEM).json()

actual = {
    "SerialNumber": data["SerialNumber"],
    "Model": data["Model"],
    "BiosVersion": data["BiosVersion"],
    "CpuCount": data["ProcessorSummary"]["Count"],
    "MemoryGiB": data["MemorySummary"]["TotalSystemMemoryGiB"],
    "Health": data["Status"]["Health"],
}

# 3. 逐項比對
fail_count = 0
for item, expected in spec.items():
    value = actual[item]
    if value == expected:
        result = "PASS"
    else:
        result = "FAIL"
        fail_count += 1
    print(f"[{result}] {item}: 規格={expected} 實際={value}")

# 4. 整機判定
print("-" * 40)
if fail_count == 0:
    print("整機判定: PASS")
    sys.exit(0)
else:
    print(f"整機判定: FAIL（{fail_count} 項不符）")
    sys.exit(1)
