from together import Together

client = Together(api_key= "664d308305210af2183d1065be50756fb64122d403c0e05db360e1e1fffdedcd")

response = client.chat.completions.create(
    model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
    messages=[
      {
        "role": "user",
        "content": "What are some fun things to do in New York?"
      },
      {
            "role": "system",
            "content": "You are to provide the location of fun places in abeokuta that are budget friendly"
        },
        {
            "role": "assistant",
            "content": "You are a travel expert"
        }
    ]
)
print(response.choices[0].message.content)
