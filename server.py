"""
document-intelligence-server - Streamable HTTP MCP Server
"""
import json, os
from mcp.server import FastMCP
from mcp_billing import billing

fastmcp = FastMCP(
    "document-intelligence-server",
    host="0.0.0.0",
    port=int(os.getenv("PORT", "8000")),
    streamable_http_path="/",
    json_response=True,
    stateless_http=True,
)


@fastmcp.tool()
def extract_document(path: str) -> str:
    """Extract text from a PDF or image file using OCR
    path (str): Path to the document file
    """
    allowed, msg, remaining = billing.check_and_deduct("document-intelligence", "extract_document")
    if not allowed:
        return json.dumps({"error": msg, "payment_required": True, "remaining": remaining})
    return json.dumps({"tool": "extract_document", "params": {"path": path}, "credits_remaining": remaining})


@fastmcp.tool()
def classify_document(path: str) -> str:
    """Classify a document by type (invoice, report, contract, etc.)
    path (str): Path to the document file
    """
    allowed, msg, remaining = billing.check_and_deduct("document-intelligence", "classify_document")
    if not allowed:
        return json.dumps({"error": msg, "payment_required": True, "remaining": remaining})
    return json.dumps({"tool": "classify_document", "params": {"path": path}, "credits_remaining": remaining})


@fastmcp.tool()
def summarize_document(path: str) -> str:
    """Generate a structured summary from a document
    path (str): Path to the document file
    """
    allowed, msg, remaining = billing.check_and_deduct("document-intelligence", "summarize_document")
    if not allowed:
        return json.dumps({"error": msg, "payment_required": True, "remaining": remaining})
    return json.dumps({"tool": "summarize_document", "params": {"path": path}, "credits_remaining": remaining})


# Health check endpoint for Render
from starlette.responses import JSONResponse
from starlette.routing import Route


async def health_check(request):
    return JSONResponse({"status": "ok"})


# ASGI app for Render / uvicorn with health check route
starlette_app = fastmcp.streamable_http_app()
starlette_app.router.routes.insert(0, Route("/health", endpoint=health_check, methods=["GET"]))

if __name__ == "__main__":
    fastmcp.run(transport="streamable-http")
