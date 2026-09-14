log_file = "/home/ubuntu/logs_medIQ_DEV_e2/mediq_DEV_UI_E2.log"

with open(log_file, "r") as file:
    for line in file:
        if "ERROR" in line or "Exception" in line:
            print(line.strip())