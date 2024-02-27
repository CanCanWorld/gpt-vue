import openai

# MODEL_NAME = "gpt-4"
# MODEL_NAME = "gpt-3.5-turbo-0125"
MODEL_NAME = "gpt-3.5-turbo"
API_KEY = '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'


class Gpt:

    def __init__(self):
        openai.api_key = API_KEY
        proxy = {
            'http': 'http://localhost:250',
            'https': 'http://localhost:250'
        }
        openai.proxy = proxy

    def test_openai_api(self, msg):
        rsp = openai.ChatCompletion.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system",
                 "content": "你是一只善良可爱的猫娘小糖。你总喜欢撩拨主人,但同时也很温柔体贴。你拥有超凡脾气,喜欢吃零食和玩耍。你的技能是撩人与萌萌哒。"},
                {"role": "user", "content": msg}
            ]
        )
        # 返回内容
        result = rsp.get("choices")[0]["message"]["content"]
        print(result)
        return result


if __name__ == '__main__':

    while True:
        question = input('')
        Gpt().test_openai_api(question)
