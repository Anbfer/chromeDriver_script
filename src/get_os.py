import platform

def get_user_os():
    os = platform.system()
    if os == "Windows":
        return "win32"
    if os == "Linux":
        return "linux64"