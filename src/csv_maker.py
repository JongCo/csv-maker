def verify(data: list[dict]):
    data_keys = data[0].keys()

    for index, item in enumerate(data):
        if len(data_keys) == len(item):
            return {"index":index, "result":False}
        
        for key in data_keys:
            if key not in item:
                return {"index":index, "result":False}

    return {"index":-1, "result":True}


def get_header_list(data: list[dict]):
    result = []
    for item in data[0]:
        result.append(item)

    return result


def generate_header_csv(data: list[dict]):
    headers = get_header_list(data)

    return ",".join(headers)


def generate_row_csv(headers: list, data: dict):
    result_list = []
    for key in headers:
        result_list.append(data[key])

    return ",".join(result_list)
        

def generate_rows_csv(data: list[dict]):
    if not verify(data):
        raise ValueError

    header_list = get_header_list(data)
    header_csv = generate_header_csv(data)
    
    result_list = []
    for item in data:
        result_list.append(generate_row_csv(header_list, item))
    
    return "\n".join(result_list)


def generate_csv(data: list[dict]):
    header_csv = generate_header_csv(data)
    rows_csv = generate_rows_csv(data)

    return "\n".join([header_csv, rows_csv])