# Python Examples

A collection of practical Python utilities and code examples demonstrating various functionality.

## Table of Contents

- [Installation](#installation)
- [Utilities](#utilities)
  - [URL Shortener](#url-shortener)
- [Development](#development)

## Installation

This project uses [uv](https://docs.astral.sh/uv/) for dependency management.

### Prerequisites

- Python 3.8+
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/vikasgautam18/python-examples.git
cd python-examples
```

2. Install dependencies using uv:
```bash
uv sync
```

## Utilities

### URL Shortener

#### Overview

The URL Shortener is a command-line utility that converts long URLs into short, shareable links using the TinyURL service.

**Module:** `python_examples.shorten_url`

#### Features

- Simple URL shortening via TinyURL API
- Command-line interface for easy usage
- Error handling for failed requests
- Lightweight and fast

#### Dependencies

- `requests` - HTTP library for API communication

#### Usage

```bash
uv run python -m python_examples.shorten_url --url "https://example.com/very/long/url/path"
```

**Output:**
```
Shortened URL: https://tinyurl.com/abc123xyz
```

#### Examples

Shorten a GitHub repository URL:
```bash
uv run python -m python_examples.shorten_url --url "https://github.com/vikasgautam18/python-examples"
```

Shorten a documentation URL:
```bash
uv run python -m python_examples.shorten_url --url "https://docs.python.org/3/library/argparse.html"
```

#### How It Works

1. Takes a long URL as input via command-line argument
2. Sends a request to the TinyURL API
3. Receives and returns the shortened URL
4. Handles errors gracefully with informative messages

#### API Reference

**Function:** `shorten_url(url: str) -> str`

**Parameters:**
- `url` (str): The full URL to be shortened

**Returns:**
- `str`: The shortened URL from TinyURL

**Raises:**
- `Exception`: If the API request fails or returns an error status code

#### Limitations

- Requires internet connectivity
- Dependent on TinyURL service availability
- No custom alias support (uses TinyURL's auto-generated codes)

## Development

### Running Tests

```bash
uv run python -m pytest
```

### Code Quality

Format code with Black:
```bash
uv run black src/ tests/
```

Lint with Ruff:
```bash
uv run ruff check src/ tests/
```

Type checking with Mypy:
```bash
uv run mypy src/
```

### Adding Dependencies

To add a new dependency:
```bash
uv add package-name
```

To add a development dependency:
```bash
uv add --dev package-name
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.