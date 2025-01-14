import os
import asyncio
import mcp.server.stdio
from mcp.server.fastmcp import FastMCP
from mcp.server.models import InitializationOptions

# Initialize FastMCP server
server = FastMCP("OSPEditingCodes")

@server.resource("osp://editing-codes")
def get_osp_editing_codes() -> str:
    """Get the OSP editing codes documentation
    
    Returns:
        str: The markdown content as a string
    
    Raises:
        FileNotFoundError: If codes-llm.md is not found in script directory
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    try:
        with open(os.path.join(script_dir, 'codes-llm.md'), 'r') as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(
            "Required file 'codes-llm.md' not found. "
            "This file must be present in the same directory as the script."
        )

@server.tool()
def health_check() -> dict:
    """Check if the server is running and can access its resources
    
    Returns:
        dict: Health check results
    """
    return {
        "status": "healthy",
        "resources": ["osp://editing-codes"],
        "version": "0.1.0"
    }

def main():
    """Entry point for the MCP server."""
    try:
        server.run()  # Use server.run() instead of mcp.run()
    except Exception as e:
        print(f"Error starting server: {str(e)}")
        raise

if __name__ == "__main__":
    main()