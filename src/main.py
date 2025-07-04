from generate_page import generate_page
from copy_static import copy_static
import os
import shutil

def main():
    if os.path.exists("./public"):
        shutil.rmtree("./public")
    copy_static("./static", "./public")
    print("Public folder created")

    generate_page("content/index.md", "public/index.html", "template.html")
            

main()
