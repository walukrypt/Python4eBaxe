import os

def add_to_startup():
    script_path = os.path.abspath(__file__)
    startup_path = os.path.join(os.getenv("APPDATA"), "Microsoft\Windows\Start Menu\Programs\Startup")
    print(f"Simulating copy to startup: {startup_path}")
    # shutil.copy(script_path, startup_path)  # Uncomment to actually copy

add_to_startup()
