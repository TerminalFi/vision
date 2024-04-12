
# MiniHTML Library

The MiniHTML library provides a simple and lightweight way to generate HTML content programmatically in Python. It allows you to create HTML elements, style them, and build complex HTML structures using a fluent interface.

## Features

- Create HTML elements programmatically using Python syntax
- Style elements using CSS properties
- Nest elements to build complex HTML structures
- Generate HTML code from the created elements
- Supports basic CSS styling and element querying
- Tries to only support Mini HTML supported tags

## Installation

TODO

## Usage

Here's a simple example demonstrating how to use MiniHTML to create an HTML document:

```python
from minihtml import div, p, h1

# Create some HTML elements
html_content = div().add_child(
    h1("Welcome to MiniHTML"),
    p("This is a simple HTML document generated using MiniHTML.")
)

# Generate HTML code from the elements
html_code = html_content.render()

print(html_code)
```

This will output:

```html
<div>
  <h1>Welcome to MiniHTML</h1>
  <p>This is a simple HTML document generated using MiniHTML.</p>
</div>
```

## Contributing

Contributions are welcome! If you have any ideas for improvement or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
