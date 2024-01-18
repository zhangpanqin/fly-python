class JiraAPI:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def run(self, name=str):
        def demo2(name=str):
            return f"${name}-111"

        print(name)
        demo_ = demo2(name)
        print(demo2)
        return demo_


if __name__ == '__main__':
    jira_api = JiraAPI("22", "11")
    jira_api.run("demo")
