import web

from gpt import Gpt

urls = (
    '/msg/(\w+)', 'Msg'
)

GPT = Gpt()


class Msg:
    def GET(self, msg):
        print(msg)
        res = GPT.test_openai_api(msg)
        return res


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
