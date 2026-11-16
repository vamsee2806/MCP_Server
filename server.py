from mcp.server.mcpserver import MCPServer 
mcp = MCPServer("Hello MCP")

@mcp.tool()
def get_greeting(name: str) -> str:
    """Return a greeting for student."""
    return f"Hello,  {name}! Your First MCP tool works."

@mcp.tool()
def add_numbers (a: int, b: int) -> int:
    """Add two numbers."""
    return a + b
@mcp.tool()
def multiply_numbers (a:int, b:int) -> int:
    """Multiply two numbers."""
    return a * b
@mcp.tool()
def divide_numbers (a:int, b:int) -> float:
    """Divide two numbers."""
    return a / b
@mcp.tool()
def subtract_numbers (a:int, b:int) -> int:
    """Subtract two numbers."""
    return a - b
@mcp.tool()
def square_number (a:int) -> int:
    """Square a number."""
    return a * a
@mcp.tool()
def cube_number (a:int) -> int:
    """Cube a number."""
    return a * a * a
if __name__ == "__main__":
    mcp.run()