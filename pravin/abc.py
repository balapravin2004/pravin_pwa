import os

def create_web_directory(directory_name):
    """Creates a directory with HTML, CSS, and JS files.

    Args:
        directory_name: The name of the directory to create.
    """

    try:
        # Create the main directory
        os.makedirs(directory_name, exist_ok=True)  # exist_ok prevents error if dir exists

        # Create subdirectories (optional but good practice)
        os.makedirs(os.path.join(directory_name, "css"), exist_ok=True)
        os.makedirs(os.path.join(directory_name, "js"), exist_ok=True)

        # Create the files
        index_html_path = os.path.join(directory_name, "index.html")
        style_css_path = os.path.join(directory_name, "css", "style.css")
        script_js_path = os.path.join(directory_name, "js", "script.js")

        # Write default content to the files (you can customize this)
        with open(index_html_path, "w") as f:
            f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Web Page</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <h1>Hello, World!</h1>

    <script src="js/script.js"></script>
</body>
</html>""")

        with open(style_css_path, "w") as f:
            f.write("/* Basic CSS Styling */\nbody {\n    font-family: sans-serif;\n}\n")

        with open(script_js_path, "w") as f:
            f.write("// JavaScript code goes here\nconsole.log('Hello from script.js!');\n")

        print(f"Directory '{directory_name}' and files created successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")



# Get the directory name from the user (or you can hardcode it)
dir_name = input("Enter the directory name: ")

create_web_directory(dir_name)



# Example usage (hardcoded name):
# create_web_directory("my_website")