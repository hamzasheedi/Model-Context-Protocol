from mcp.server.fastmcp import FastMCP

mcp = FastMCP("DocumentMCP", stateless_http=True)

docs = {
    "deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
    "report.pdf": "The report details the state of a 20m condenser tower.",
    "financials.docx": "These financials outline the project's budget and expenditures.",
    "outlook.pdf": "This document presents the projected future performance of the system.",
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specifications define the technical requirements for the equipment.",
}

# ------------------ TOOLS ------------------

@mcp.tool()
def read_doc(docs_id: str):
    """Return the content of a document"""
    return docs.get(docs_id, "Document not found")

@mcp.tool()
def edit_doc(docs_id: str, edited_text: str):
    """Edit a document"""
    docs[docs_id] = edited_text
    return f"{docs_id} updated successfully."


# ------------------ RESOURCES ------------------

@mcp.resource(uri="http://127.0.0.1:8000/docs")
def all_doc_id():
    """Return all document IDs"""
    return list(docs.keys())

@mcp.resource(uri="http://127.0.0.1:8000/docs/{doc_id}")
def all_doc_content(doc_id: str):
    """Return the content of a specific document"""
    return docs.get(doc_id, "Document not found")


# ------------------ PROMPTS ------------------

@mcp.prompt()
def rewrite_in_markdown(docs_id: str):
    """Prompt to rewrite a document in Markdown format"""
    return f"Rewrite this document in well-structured, professional Markdown:\n\n{docs[docs_id]}"

@mcp.prompt()
def summarize(docs_id: str):
    """Prompt to summarize a document concisely"""
    return f"Summarize this document briefly and clearly:\n\n{docs[docs_id]}"


# ------------------ APP ------------------

mcp_app = mcp.streamable_http_app()
