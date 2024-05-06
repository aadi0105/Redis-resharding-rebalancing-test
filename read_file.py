def hosts():
    file_path = './inventory'
    ips = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                stripped_line = line.strip()
                ips.append(stripped_line)
        return ips
    except FileNotFoundError:
        return "File not found. Please provide a valid file path."