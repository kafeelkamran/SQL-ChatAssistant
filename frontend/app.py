import gradio as gr
import requests

def chat_with_assistant(user_query):
    url = "http://127.0.0.1:8000/query"  
    payload = {"query": user_query}
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, json=payload, headers=headers)
        response_data = response.json()
        
        return response_data.get("message", "No response received.")  # Use .get() to avoid KeyError

    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

iface = gr.Interface(
    fn=chat_with_assistant,
    inputs="text",
    outputs="text",
    title="SQLite Chat Assistant",
    description="Ask queries about employees, managers, and salary expenses."
)

iface.launch()
