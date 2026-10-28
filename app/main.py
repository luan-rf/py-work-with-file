def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as file:
        for linha in file:
            clean_line = linha.strip()
            if not clean_line:
                continue

            operation, amount = clean_line.split(",")
            amount = int(amount)

            if operation == "supply":
                supply += amount
            elif operation == "buy":
                buy += amount

    result = supply - buy

    result_text = (
        f"supply,{supply}\n"
        f"buy,{buy}\n"
        f"result,{result}\n"
    )

    with open(report_file_name, "w") as file:
        file.write(result_text)
