# Hello MCP Project

Name: T. Vamsi Krishna  
Reg No: 261FB04043

## Project Overview
This project is a simple Python-based MCP (Model Context Protocol) server that exposes multiple callable tools for basic operations. The server is defined in [server.py](server.py), and the workspace is configured to launch it through [.vscode/mcp.json](.vscode/mcp.json).

The server uses the `MCPServer` class from the `mcp.server.mcpserver` module and registers each function as an MCP tool using the `@mcp.tool()` decorator. When run as a script, it starts the server with `mcp.run()`.

## MCP Server Configuration
The VS Code MCP configuration in [.vscode/mcp.json](.vscode/mcp.json) defines a `stdio` server named `helloMCP`, which runs the Python interpreter from the workspace virtual environment and executes the `server.py` script.

## Functions in the Server
The following functions are exposed by the server:

- `get_greeting(name: str) -> str`  
  Returns a greeting message for the given name.

- `add_numbers(a: int, b: int) -> int`  
  Adds two integers and returns the sum.

- `multiply_numbers(a: int, b: int) -> int`  
  Multiplies two integers and returns the product.

- `divide_numbers(a: int, b: int) -> float`  
  Divides the first number by the second and returns the floating-point result.

- `subtract_numbers(a: int, b: int) -> int`  
  Subtracts the second number from the first and returns the difference.

- `square_number(a: int) -> int`  
  Computes the square of a number.

- `cube_number(a: int) -> int`  
  Computes the cube of a number.

## How to Run
1. Activate the virtual environment.
2. Run the server script:

```bash
python server.py
```

This starts the MCP server and makes the defined tools available to connected MCP clients.

## Summary
This is a lightweight introductory MCP project for learning how to expose Python functions as tools through the Model Context Protocol. It covers greeting logic and basic arithmetic operations in a simple and easy-to-understand format.
