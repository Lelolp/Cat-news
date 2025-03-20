import random
from django.core.files.base import ContentFile
import requests
from django.conf import settings
from openai import OpenAI


class PostGenerator:
    def __init__(self, key=None, chat_model=None, img_model=None):
        if key:
            self.key = key
        else:
            if settings.GPT_KEY:
                self.key = settings.GPT_KEY
            else:
                raise ValueError('GPT key not provided')
        if chat_model:
            self.chat_model = chat_model
        else:
            self.chat_model = 'gpt-4o-mini-2024-07-18'
        if img_model:
            self.img_model = img_model
        else:
            self.img_model = 'dall-e-2'
        self.base_prompt = "Please generate a fun news post with title of max size 50 symbols,write the answer in the TITLE|CONTENT format,theme of the post is "
        self.theme_prompts = [
                              "food",
                              "recipes",
                              "jokes",
                              "fun fake news",
                              "interesting facts",
                              "cats",
                              "memes",
                              "technological news"
                              ]
        self.prompt = self.base_prompt + random.choice(self.theme_prompts)
        self.client = OpenAI(api_key=self.key)
    def generate_news_post(self, prompt=None):
        if prompt:
            self.prompt = prompt
        response = self.client.chat.completions.create(
            model=self.chat_model,
            messages=[{
                "role": "user",
                "content": self.prompt
            }]
        )
        post = dict()
        post['title'] = response.choices[0].message.content.split('|')[0]
        post['text'] = response.choices[0].message.content.split('|')[1]
        post['image'] = self.save_image_from_url(self.generate_image(prompt=post['title']))
        return post
    def generate_image(self, prompt):
        response = self.client.images.generate(
            model=self.img_model,
            prompt=prompt,
            size="256x256",
            quality="standard",
            n=1,
        )
        return response.data[0].url

    def save_image_from_url(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return ContentFile(content=response.content, name='image.png')
        else:
            return None
