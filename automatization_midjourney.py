import time
import clipboard
import pyautogui

prompts_file = "new_prompts2.txt"        #prompts_file = "prompts.txt"
processed_prompts_file = "new_processed_prompts.txt"

def write_to_processed_prompts(prompt):
    with open(processed_prompts_file, "a") as file:
        file.write(prompt + "\n")

def remove_processed_prompt(prompt):
    with open(prompts_file, "r") as file:
        prompts = file.readlines()

    with open(prompts_file, "w") as file:
        for line in prompts:
            if line.strip() != prompt:
                file.write(line)

# Read all the prompts from the prompts_file and store them in a list called prompts
with open(prompts_file, "r") as file:
    prompts = [line.strip() for line in file]


for prompt in prompts:
    mj_prompt = "/imagine prompt: " + prompt

    # Print mj_prompt to the console
    print(mj_prompt)

    # Write mj_prompt to the clipboard using clipboard
    clipboard.copy(mj_prompt)

    # Write mj_prompt to the processed_prompts_file
    write_to_processed_prompts(mj_prompt)

    # Remove the processed prompt from the prompts_file
    remove_processed_prompt(prompt)

    # Pause for 4 seconds
    time.sleep(4)
