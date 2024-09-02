#from langchain_ollama import OllamaLLM
#from langchain_core.prompts import ChatPromptTemplate
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

api_key = str(os.getenv("API_KEY"))
client = openai.OpenAI(
    api_key = api_key,
    base_url="https://api.aimlapi.com",
)

template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

"""model = OllamaLLM(model = "qwen2:0.5b")

def parse_with_ollama(parse_description, dom_content):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    parsed_results = []

    for i,chunk in enumerate(dom_content, start=1):
        response = chain.invoke(
                { "dom_content" : chunk, "parse_description" : parse_description }
            )
        print(f"parsed batch {i} of {len(dom_content)}")
        parsed_results.append(response)

    return "\n".join(parsed_results)

"""
def parse_with_mistral(parse_description, dom_content):

    parsed_results = []
    
    for i,chunk in enumerate(dom_content, start=1):
        chat_completion = client.chat.completions.create(
        model="mistralai/Mistral-7B-Instruct-v0.2",
        messages=[
            {"role": "system", "content":  template.format(dom_content=chunk, parse_description=parse_description)},
            {"role": "user", "content": parse_description},
        ],
        temperature=0.7,
        max_tokens=128,
        )

        response = chat_completion.choices[0].message.content
        parsed_results.append(response)
        print(f"parsed batch {i} of {len(dom_content)}")
    
    return "\n".join(parsed_results)
