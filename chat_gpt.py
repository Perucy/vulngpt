from dotenv import load_dotenv
import os
from openai import OpenAI
import re
from main import main_driver

"""
    VulGPT only works with a single CVE per query inorder to avoid token limit errors
    some of the CVEs might cause token limit error (because they have so many documents or too long documents which
    when used to provide chat gpt with context the token limit is exceeded
"""


def gpt_function(vul_res, nes_res, cve_id, query):
    load_dotenv()
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    instruction = (
        f" Answer the user's query about a vulnerability from the provided CVE include the both vulnerability and "
        f"nessus details about it\n"
        "1. Am I affected?\n"
        "    - Which systems are vulnerable?\n"
        "    - Which versions are vulnerable?\n"
        "    - In what context is it vulnerable?\n"
        "2. What could go wrong?\n"
        "    - CVSS score or severity included?\n"
        "    - CVSS source included?\n"
        "    - Does it say what an attacker can do?\n"
        "    - Does it say if exploitable remotely?\n"
        "    - Does it say if exploit is public?\n"
        "   - Does it say if actively being exploited?\n"

        "3. What can I do about it?\n"
        "    - Does it say if a patch is available?\n"
        "    - Are non-patch mitigations included?\n"
        "    -  Step-by-step mitigation instructions?"

        "4. What could go wrong if I patch/mitigate?\n"
        "5. What are the Nessus scan results in detail?\n"

        f"Nessus scan data: {nes_res}"
        f"CVE Details: {vul_res}"
        f"User's query: {query}"
    )
    MODEL = "gpt-4o"

    messages = [
        {"role": "system", "content": "You are a helpful assistant with knowledge about system vulnerabilities."},
        {"role": "user", "content": instruction},
    ]

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages
    )

    return response.choices[0].message.content
