import autogen


def describe(file_path):
    
    config_list = [
        {
            "api_key": "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",
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
    )
    # create a UserProxyAgent instance named "user_proxy"
    user_proxy = autogen.UserProxyAgent(
        name="user_proxy",
        human_input_mode="NEVER",
        is_termination_msg=lambda x: True if "TERMINATE" in x.get("content") else False,
        max_consecutive_auto_reply=10,
        code_execution_config={
            "work_dir": "work_dir",
            "use_docker": False,
        },
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


#describe('/home/ameya/Documents/model_host/autogen/test/add3.py')
