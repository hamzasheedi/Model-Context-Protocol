from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server with enhanced metadata for 2025-06-18 spec
mcp = FastMCP(
    name="hello-server",
    stateless_http=True # When true we don't need handshake or initialize things.
)

@mcp.tool()
def search_online(query:str):
    return("Showing Result For {query}")


mcp_app = mcp.streamable_http_app()