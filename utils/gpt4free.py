import re
import g4f
import config

def get_response(message, **kwargs):
    response = g4f.ChatCompletion.create(
        model=config.GPT_ENGINE,
        messages=[{"role": "user", "content": message}],
        stream=True,
    )
    for message in response:
        yield message

def bing(response):
    response = re.sub(r"\[\^\d+\^\]", "", response)
    if len(response.split("\n\n")) >= 2:
        result = "\n\n".join(response.split("\n\n")[1:])
        return result
    else:
        return response

if __name__ == "__main__":

    message = rf"""

    """
    answer = ""
    for result in get_response(message, "gpt-4"):
        print(result, end="")