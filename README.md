
# Vision Library

The Vision library provides a simple and lightweight way to generate HTML content programmatically in Python. It allows you to create HTML elements, style them, and build complex HTML structures using a fluent interface.

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

Here's a simple example demonstrating how to use Vision to create an HTML document:

```python
from vision import body, div, p, h1, Tag
from vision.context import Context

ctx = Context()
root = Tag(ctx, "html")
with root:
  with body(ctx):
    with div(ctx):
      h1(ctx, "Welcome to MiniHTML")
      p(ctx, "This is a simple HTML document generated using MiniHTML.")

print(root.render())
```

This will output:

```html
<html>

<body>
    <div>
        <h1>Welcome to MiniHTML</h1>
        <p>This is a simple HTML document generated using MiniHTML.</p>
    </div>
</body>

</html>

```

## Contributing

Contributions are welcome! If you have any ideas for improvement or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
