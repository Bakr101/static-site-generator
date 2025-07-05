from generate_page import generate_pages_recursively
from copy_static import copy_static
import os
import shutil

def main():
    if os.path.exists("./public"):
        shutil.rmtree("./public")
    copy_static("./static", "./public")
    print("Public folder created")

    generate_pages_recursively("content", "template.html", "public")
            

main()
