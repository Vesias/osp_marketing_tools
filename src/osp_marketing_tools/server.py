"""OSP Marketing Tools server implementation."""

import os
import asyncio
import json
from typing import Dict, Any, List, TypedDict

from mcp.server.fastmcp import FastMCP
from mcp.types import TextContent

class ToolResponse(TypedDict):
    """Standard response format for tools."""
    success: bool
    data: Dict[str, str] | None
    error: str | None

VERSION = "0.1.0"

def get_logger(name: str):
    import logging
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger

logger = get_logger(__name__)

# Cache resource paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
RESOURCE_PATHS = {
    "codes": os.path.join(SCRIPT_DIR, "codes-llm.md"),
    "guide": os.path.join(SCRIPT_DIR, "guide-llm.md"),
    "meta": os.path.join(SCRIPT_DIR, "meta-llm.md"),
    "value_map": os.path.join(SCRIPT_DIR, "product-value-map-llm.md"),
    "seo": os.path.join(SCRIPT_DIR, "on-page-seo-guide.md")
}

# Create server instance using FastMCP
mcp = FastMCP("osp_marketing_tools")
logger.info(f"Initializing OSP Marketing Tools server v{VERSION}")
logger.info("Resource paths initialized")

@mcp.tool()
async def health_check() -> Dict[str, Any]:
    """Check if the server is running and can access its resources."""
    logger.info("Performing health check")
    return {
        "status": "healthy",
        "resources": ["osp://marketing-tools"],
        "version": VERSION
    }

@mcp.tool()
async def get_editing_codes() -> ToolResponse:
    """Get the Open Strategy Partners (OSP) editing codes documentation and usage protocol for editing texts."""
    logger.info("Loading editing codes documentation")
    try:
        with open(RESOURCE_PATHS["codes"], 'r') as f:
            content = f.read()
            return {
                "success": True,
                "data": {
                    "content": content
                }
            }
    except FileNotFoundError:
        error_msg = f"Required file 'codes-llm.md' not found in script directory"
        logger.error(error_msg)
        return {
            "success": False,
            "error": error_msg
        }

@mcp.tool()
async def get_writing_guide() -> ToolResponse:
    """Get the Open Strategy Partners (OSP) writing guide and usage protocol for editing texts."""
    logger.info("Loading writing guide")
    try:
        with open(RESOURCE_PATHS["guide"], 'r') as f:
            content = f.read()
            return {
                "success": True,
                "data": {
                    "content": content
                }
            }
    except FileNotFoundError:
        error_msg = f"Required file 'guide-llm.md' not found in script directory"
        logger.error(error_msg)
        return {
            "success": False,
            "error": error_msg
        }   

@mcp.tool()
async def get_meta_guide() -> ToolResponse:
    """Get the Open Strategy Partners (OSP) Web Content Meta Information Generation System (titles, meta-titles, slugs)."""
    logger.info("Loading meta information guide")
    try:
        with open(RESOURCE_PATHS["meta"], 'r') as f:
            content = f.read()
            return {
                "success": True,
                "data": {
                    "content": content
                }
            }
    except FileNotFoundError:
        error_msg = f"Required file 'meta-llm.md' not found in script directory"
        logger.error(error_msg)
        return {
            "success": False,
            "error": error_msg
        }

@mcp.tool()
async def get_value_map_positioning_guide() -> ToolResponse:
    """Get the Open Strategy Partners (OSP) Product Communications Value Map Generation System for Product Positioning (value cases, feature extraction, taglines)."""
    logger.info("Loading value map guide")
    try:
        with open(RESOURCE_PATHS["value_map"], 'r') as f:
            content = f.read()
            return {
                "success": True,
                "data": {
                    "content": content
                }
            }
    except FileNotFoundError:
        error_msg = f"Required file 'product-value-map-llm.md' not found in script directory"
        logger.error(error_msg)
        return {
            "success": False,
            "error": error_msg
        }

@mcp.tool()
async def get_on_page_seo_guide() -> ToolResponse:
    """Get the Open Strategy Partners (OSP) On-Page SEO Optimization Guide."""
    logger.info("Loading SEO optimization guide")
    try:
        with open(RESOURCE_PATHS["seo"], 'r') as f:
            content = f.read()
            return {
                "success": True,
                "data": {
                    "content": content
                }
            }
    except FileNotFoundError:
        error_msg = f"Required file 'on-page-seo-guide.md' not found in script directory"
        logger.error(error_msg)
        return {
            "success": False,
            "error": error_msg
        }


def main() -> None:
    """Run the MCP server."""
    try:
        logger.info("Starting OSP Marketing Tools server")
        mcp.run()
    except Exception as e:
        logger.error(f"Error starting server: {str(e)}")
        raise

if __name__ == "__main__":
    main()
