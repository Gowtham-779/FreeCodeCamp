def number_of_files(file_size, unit, drive_size):
    if unit == "B":
        file_size = file_size/ 1000/1000/1000
    elif unit == "KB":
        file_size = file_size/1000/1000
    elif unit == "MB":
        file_size = file_size/1000

    return int(drive_size/file_size)