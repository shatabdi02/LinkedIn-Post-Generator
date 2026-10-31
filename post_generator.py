from llm_helper import llm

def get_length_str(length):
    if length == "Short":
        return "1 to 10 lines"
    if length == "Medium":
        return "10 to 20 lines"
    if length == "Long":
        return "20 to 30 lines"

def generate_post(length,language,tag):
  length_str= get_length_str(length)
  prompt=f'''
    Generate a LinkedIn post using the below information. No preamble.

    1) Topic: {tag}
    2) Length: {length_str}
    3) Language: {language}
    If Language is Hinglish then it means it is a mix of Hindi and English. 
    The script for the generated post should always be English.
    '''
  response = llm.invoke(prompt)
  return response.content

if __name__ == "__main__":
  post = generate_post("Short","English","Construction Costs")
  print(post)

