---
name: mcp-integrations
description: "Class-level MCP integration workflows: configure Hermes native MCP clients, connect stdio/HTTP servers, expose tools, and operate domain-specific MCP servers such as TouchDesigner."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [mcp, model-context-protocol, tools, integrations, touchdesigner]
---

# MCP Integrations

Use this umbrella when connecting Hermes to MCP servers or operating an MCP-backed domain integration.

## Native MCP client workflow

1. Identify server transport: stdio command, HTTP/SSE, or streamable HTTP.
2. Add/configure the server in Hermes config or with the Hermes MCP CLI.
3. Test connectivity and tool discovery before assuming tools are available.
4. Configure tool selection if the server exposes too many or risky tools.
5. Restart/reset the agent session as needed so discovered tools appear in the tool list.

## Domain MCP servers

Domain servers such as TouchDesigner expose many specialized tools. Load their domain knowledge after the generic MCP setup is working:

- Confirm the target app/server is running.
- List available MCP tools and required connection parameters.
- Use small probes before building complex scenes/workflows.
- Verify side effects in the target application, not just MCP call success.

## Former narrow skills absorbed

- `native-mcp`: Hermes native MCP client setup and tool registration.
- `touchdesigner-mcp`: TouchDesigner/twozero MCP operation patterns and reference catalogs.
