SUCCESS = 0
ERROR_FILE_NOT_FOUND = 1
ERROR_PERMISSION_DENIED = 2

def read_file(filename):
    try:
        with open(filename) as f:
            return SUCCESS, f.read()
    except FileNotFoundError:
        return ERROR_FILE_NOT_FOUND, None

code, data = read_file("test.txt")
if code != SUCCESS:
    print(f"Failed with error code: {code}")