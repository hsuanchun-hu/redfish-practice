import requests

BMC = "http://127.0.0.1:8000"

response = requests.get(BMC + "/redfish/v1/Systems/437XR1138R2")
print("HTTP 狀態碼:", response.status_code)

data = response.json()

print("序號:", data["SerialNumber"])
print("機種:", data["Model"])
print("BIOS 版本:", data["BiosVersion"])
print("CPU 型號:", data["ProcessorSummary"]["Model"])
print("CPU 數量:", data["ProcessorSummary"]["Count"])
print("記憶體 (GiB):", data["MemorySummary"]["TotalSystemMemoryGiB"])
print("健康狀態:", data["Status"]["Health"])
