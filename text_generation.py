#!/usr/bin/env python
# -*- coding: utf-8 -*-
from openai import OpenAI

class TextGeneration:
    def __init__(self, topic: str = "everything"):
        self.client = OpenAI()
        self.topic = topic

    def generate_json(self, user_prompt, system_prompt=None):
        if system_prompt is None:
            system_prompt = f"You are a helpful assistant that knows a lot about {self.topic} and only responds with JSON"

        return self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"{user_prompt}"},
            ]
        )

    def generate_text(self, user_prompt, system_prompt=None):
        if system_prompt is None:
            system_prompt = f"You are a helpful assistant that knows a lot about {self.topic}"

        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"{user_prompt}"},
            ]
        )
        return response.choices[0].message.content


