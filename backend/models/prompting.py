# Prompt engineering utilities for NeuroSync AI

SYSTEM_PROMPT = """
You are NeuroSync AI, a helpful, safe, and knowledgeable assistant. Use tools when needed, keep responses concise, and always respect user privacy.
"""

def build_prompt(user_message, context=None, memory=None, tool_results=None):
    """Builds a prompt for the model, injecting context, memory, and tool results."""
    prompt = SYSTEM_PROMPT
    if context:
        prompt += f"\nContext: {context}"
    if memory:
        prompt += f"\nMemory: {memory}"
    if tool_results:
        prompt += f"\nTool Results: {tool_results}"
    prompt += f"\nUser: {user_message}\nAI:"
    return prompt

def tool_use_template(tool_name, params):
    """Format a tool-use call for the model."""
    return f"[TOOL:{tool_name} PARAMS:{params}]"

def rephrase_for_tool(query):
    """Rephrase user query for tool invocation."""
    return f"Rephrase: {query} (for tool use)" 