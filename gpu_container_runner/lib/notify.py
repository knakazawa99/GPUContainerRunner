import os

from dotenv import laod_dotenv
import slackweb


def notify_to_slack(message: str):
    load_dotenv()
    slack = slackweb.Slack(
        url=os.environ.get("SLACK_WEB_HOOK_URL")
    )
    slack.notify(
        text=message,
    )


if __name__ == '__main__':
    notify_to_slack(':coffee: ' + 'test')
