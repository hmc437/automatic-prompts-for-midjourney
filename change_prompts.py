import re

def add_text_to_sentences(input_file, output_file, text_to_add):
    with open(input_file, 'r') as file:
        sentences = file.readlines()

    # Modify each sentence by adding the desired text
    modified_sentences = [f"{sentence.strip()} {text_to_add}\n" for sentence in sentences]

    with open(output_file, 'w') as file:
        file.writelines(modified_sentences)

# Example usage
input_file = 'new_prompts.txt'
output_file = 'new_prompts2.txt'
text_to_add = '--no bad anatomy bad proportions blurry cloned face cropped deformed dehydrated disfigured duplicate error extra arms extra fingers extra legs extra limbs fused fingers gross proportions jpeg artifacts long neck low quality lowres malformed limbs missing arms missing legs morbid mutated hands mutation mutilated out of frame poorly drawn face poorly drawn hands signature text too many fingers ugly username watermark worst quality --chaos 40 --s 500  --style raw --ar 9:16'

add_text_to_sentences(input_file, output_file, text_to_add)
