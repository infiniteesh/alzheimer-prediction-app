import google.generativeai as genai
genai.configure(api_key="AIzaSyB_CZbXVv6ESIbMHI1LCI-CTnucggNS4ps") 
models = genai.list_models()
for m in models:
    print(m.name)