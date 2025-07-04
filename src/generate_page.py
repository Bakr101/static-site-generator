import os
from extract_title import extract_title
from blocks import markdown_to_html_node

# to_path will be something like /public/index.html
def generate_page(from_path: str, dst_path: str, template_path: str):
    print(f"Generating page from {from_path} to {dst_path} with template {template_path}")
    try:
        with open(from_path, "r", encoding="utf-8") as f:
            markdown = f.read()
        f.close()
    except FileNotFoundError:
        print(f"markdown file {from_path} not found")
        return
    try:
        with open(template_path, "r", encoding="utf-8") as f:
            template = f.read()
        f.close()
    except FileNotFoundError:
        print(f"template {template_path} not found")
        return
    content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    dst_dir = os.path.dirname(dst_path)
    if not os.path.exists(dst_dir) or not os.path.isdir(dst_dir):
        os.mkdir(dst_dir)
    try:
        with open(dst_path, "w", encoding="utf-8") as f:
            f.write(template.replace("{{ title }}", title).replace("{{ content }}", content))
    except Exception as e:
        print(f"Error writing to {dst_path}: {e}")
        return