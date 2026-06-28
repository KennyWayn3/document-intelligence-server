# document-intelligence-server - MCP Server

MCP server for intelligent document processing - extract, classify, summarize PDFs/Docs/Images using vision LLMs

## Installation

### pip
```bash
pip install document-intelligence-server
```

### uvx (recommended)
```bash
uvx document-intelligence-server
```

## Usage

Add to your Claude Desktop config:
```json
{"mcpServers": {"document-intelligence-server": {"command": "uvx", "args": ["document-intelligence-server"]}}}
```

## Available Tools
- **example_tool**: Example

## License
MIT

[![PyPI](https://img.shields.io/pypi/v/document-intelligence-server)](https://pypi.org/project/document-intelligence-server/) [![GitHub](https://img.shields.io/github/stars/KennyWayn3/document-intelligence-server)](https://github.com/KennyWayn3/document-intelligence-server)
