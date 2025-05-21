import streamlit as st
import re
import os
from openai import OpenAI
from dotenv import load_dotenv

from chat_gpt import *

st.title("VulGPT")

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4o"

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("How can I help you today?"):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        cve_pattern = r'CVE-\d{4}-\d{4,7}'
        cves = re.findall(cve_pattern, prompt)
        if len(cves) == 0:
            stream = client.chat.completions.create(
                model=st.session_state["openai_model"],
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=True,
            )
            response = st.write_stream(stream)

        else:
            vul_res, nes_res = main_driver(cves[0])
            response = gpt_function(vul_res, nes_res, cves[0], prompt)
            st.write(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

