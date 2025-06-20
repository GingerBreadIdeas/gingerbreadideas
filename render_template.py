# /// script
# dependencies = [
#     "jinja2",
# ]
# ///

from jinja2 import Template


def main():
    # Read the template file
    with open("index.template.html", "r") as f:
        template_content = f.read()

    # Create Jinja template
    template = Template(template_content)

    # Define variables
    variables = {
        "form_url": "https://mailchi.mp/gingerbreadideas/gingerbreadideas-wait-list"
    }

    # Render the template
    rendered_html = template.render(**variables)

    # Print to stdout
    print(rendered_html)


if __name__ == "__main__":
    main()
