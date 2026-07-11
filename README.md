# document-intelligence-server - MCP Server

MCP server for intelligent document processing — extract text, classify, and summarize PDFs, images, and documents using vision LLMs.

## Tools

### `extract_document`
Extract text from a PDF or image file using OCR.
- **`path`** (string, required): Path to the document file

### `classify_document`
Classify a document by type (invoice, report, contract, etc.).
- **`path`** (string, required): Path to the document file

### `summarize_document`
Generate a structured summary from a document.
- **`path`** (string, required): Path to the document file

## Quick Start (local)

```bash
pip install -r requirements.txt
export MCP_BILLING_API=https://mcp-billing-api.onrender.com
uvicorn server:starlette_app --host 0.0.0.0 --port 8000
```

## Usage with Claude Desktop / MCP clients

```json
{
  "mcpServers": {
    "document-intelligence-server": {
      "url": "https://mcp-doc-intel.onrender.com/"
    }
  }
}
```

## Deployed endpoint

`https://mcp-doc-intel.onrender.com/` — Streamable HTTP transport at root path. Health check at `/health`.

## Environment Variables

| Variable | Required | Description |
|---|---|---|
| `MCP_BILLING_API` | Yes | Billing API endpoint |
| `MCP_LICENSE_KEY` | Yes | License key for billing |
| `AGENTICMARKET_SECRET` | No | Secret for AgenticMarket authentication |

## License

MIT

[![PyPI](https://img.shields.io/pypi/v/document-intelligence-server)](https://pypi.org/project/document-intelligence-server/) [![GitHub](https://img.shields.io/github/stars/KennyWayn3/document-intelligence-server)](https://github.com/KennyWayn3/document-intelligence-server)
