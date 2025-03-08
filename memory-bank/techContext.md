# Technical Context: OSP Marketing Tools

## Technology Stack

### Core Technologies
1. **Python**
   - Version: 3.10+
   - Role: Primary implementation language
   - Key Features Used:
     - Asyncio for async/await pattern
     - Type hints for code clarity
     - Modern string handling for markdown processing

2. **MCP (Model Context Protocol)**
   - Framework: FastMCP
   - Purpose: Server implementation and tool exposure
   - Key Components:
     - Tool decorators
     - Resource management
     - Request/response handling

3. **Markdown**
   - Usage: Resource file format
   - Purpose: Store methodology guides and documentation
   - Benefits:
     - Human-readable
     - Version control friendly
     - Easy to maintain

### Development Tools

1. **Package Management**
   ```toml
   [tool.poetry]
   name = "osp_marketing_tools"
   version = "0.1.0"
   description = "OSP Marketing Tools MCP Server"
   ```

2. **UV Package Manager**
   - Purpose: Modern Python package management
   - Features:
     - Fast dependency resolution
     - Reproducible builds
     - Virtual environment management

3. **Version Control**
   - System: Git
   - Platform: GitHub
   - Structure:
     - Main branch for stable releases
     - Feature branches for development

## Development Environment

### Setup Requirements
1. **System Requirements**
   - Python 3.10 or higher
   - UV package manager
   - Git for version control

2. **Environment Setup**
   ```bash
   # Install UV
   pip install --user uv
   
   # Clone repository
   git clone https://github.com/open-strategy-partners/osp_marketing_tools
   
   # Install dependencies
   cd osp_marketing_tools
   uv venv
   uv pip install -e .
   ```

3. **Configuration**
   - MCP server configuration in client settings
   - Environment variables (if needed)
   - Logging configuration

### IDE Configuration
- Python extension settings
- Type checking enabled
- Linting configuration
- Markdown preview support

## Dependencies

### Core Dependencies
1. **mcp-sdk**
   - Purpose: MCP protocol implementation
   - Version: Latest stable
   - Usage: Server implementation

2. **FastMCP**
   - Purpose: MCP server framework
   - Features:
     - Async support
     - Tool registration
     - Error handling

### Optional Dependencies
1. **Development Tools**
   - pytest for testing
   - black for code formatting
   - mypy for type checking
   - flake8 for linting

## Technical Constraints

### Server Constraints
1. **Resource Management**
   - Resources must be markdown files
   - Files must be in package directory
   - File naming convention: *-llm.md

2. **Performance**
   - Async implementation required
   - Memory-efficient resource loading
   - Response time considerations

3. **Error Handling**
   - Graceful failure modes
   - Clear error messages
   - Consistent error format

### Integration Constraints
1. **MCP Protocol**
   - Protocol version compatibility
   - Tool interface requirements
   - Response format standards

2. **Client Compatibility**
   - Claude Desktop
   - Cursor IDE
   - LibreChat
   - Other MCP-enabled clients

### Security Considerations
1. **Resource Access**
   - File system security
   - Resource validation
   - Error exposure limits

2. **Input Validation**
   - Tool parameter validation
   - Resource path validation
   - Error message sanitization

## Deployment Configuration

### Local Development
```json
{
    "mcpServers": {
        "osp_marketing_tools": {
            "command": "uvx",
            "args": [
                "--from",
                "git+https://github.com/open-strategy-partners/osp_marketing_tools@main",
                "osp_marketing_tools"
            ]
        }
    }
}
```

### Production Setup
1. **Installation**
   - Via UV package manager
   - From GitHub repository
   - Through pip (if published)

2. **Configuration**
   - Client-specific setup
   - Resource path configuration
   - Logging settings

## Monitoring & Maintenance

### Health Checks
- Server status endpoint
- Resource availability checks
- Version information

### Logging
- Structured logging format
- Error tracking
- Performance monitoring

### Updates
- Resource content updates
- Server version updates
- Dependency management

## Testing Strategy

### Unit Tests
- Tool functionality
- Resource loading
- Error handling

### Integration Tests
- Client interaction
- Resource processing
- Tool chain testing

### Performance Tests
- Response times
- Memory usage
- Resource loading efficiency
