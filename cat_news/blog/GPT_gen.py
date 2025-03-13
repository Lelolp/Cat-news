import requests
def generate_news_post():
    # Define the prompt to be sent
    prompt = 'Please generate a fun news post with title of max size 50 symbols and content choose of the themes like food recepies or jokes or fun fake news or interestinght facts or cats or mems or techonolagy news.submit the answer in the "TITLE|CONTENT" format"'

    # Enter E-mail to generate API
    api_key = '4b6a6dcf208b1d0244efe2dbd0414c56'

    # Define the default model if none is specified
    default_model = 'gpt-3.5-turbo'

    # Uncomment the model you want to use, and comment out the others
    #model = 'gpt-4'
    # model = 'gpt-4-32k'
    # model = 'gpt-3.5-turbo-0125'
    model = default_model

    # Build the URL to call
    api_url = f'http://195.179.229.119/gpt/api.php?prompt={requests.utils.quote(prompt)}&api_key={requests.utils.quote(api_key)}&model={requests.utils.quote(model)}'

    try:
        # Execute the HTTP request
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad HTTP status codes

        # Parse and print the response
        data = response.json()
        return data['content']

    except requests.RequestException as e:
        # Print any errors
        print(f'Request Error: {e}')