from generate_page import generate_pages_recursively
from copy_static import copy_static
import os
import shutil
import sys

def main():
    print("Generating pages...")
    if len(sys.argv) < 2:
        base_path = "/"
    else:
        base_path = sys.argv[1]
    
    if os.path.exists("./docs"):
        shutil.rmtree("./docs")
    copy_static("./static", "./docs")
    print("docs folder created")

    generate_pages_recursively("content", "template.html", "docs", base_path)
            

main()
