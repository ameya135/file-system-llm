import autogen
import json
from os import path

def describe(file_path):
    
    config_list = [
        {
            "api_key": "Enter your api key here",
            "model": "gpt-3.5-turbo"
        }
    ]

    llm_config={
        "timeout": 600,
        "cache_seed": 44,  # change the seed for different trials
        "config_list": config_list,
        "temperature": 0,
    }

    assistant = autogen.AssistantAgent(
        name="assistant",
        llm_config=llm_config,
        is_termination_msg=lambda x: True if "TERMINATE" in x.get("content") else False,
        system_message="Describe the code in 3 lines and then type 'TERMINATE' in the same sentence",
    )
    # create a UserProxyAgent instance named "user_proxy"
    user_proxy = autogen.UserProxyAgent(
        name="user_proxy",
        human_input_mode="NEVER",
        is_termination_msg=lambda x: True if "TERMINATE" in x.get("content") else False,
        max_consecutive_auto_reply=1,
        code_execution_config={
            "work_dir": "work_dir",
            "use_docker": False,
        },
        system_message="Describe the code in 2 lines then type 'TERMINATE' after the same sentence.",
    )

    def extract_code_from_file(file_path):
        try:
            with open(file_path, 'r') as file:
                code = file.read()
            return code
        except FileNotFoundError:
            return f"File not found: {file_path}"
        except Exception as e:
            return f"Error reading file: {e}"
    
    code = extract_code_from_file(file_path)

    task1 = f"Describe the code {code} in 2 lines."
    user_proxy.initiate_chat(assistant, message=task1)
    return user_proxy,assistant

def update_json(file_name, res):
    
    file_name = file_name.split("/")[-1]
    json_file_path = './file_metadata.json'
    list_obj = []

    if path.isfile(json_file_path) is False:
        raise Exception("File not found")

    with open(json_file_path) as f:
        list_obj = json.load(f)
        
    list_obj.append({
        "Name": file_name,
        "Description": res
    })

    with open(json_file_path, 'w') as f:
        json.dump(list_obj, f, indent=4, separators=(',', ': '))
