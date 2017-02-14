from slackclient import SlackClient
from re import findall

sc = SlackClient(
    """xoxp-113334704304-114716829062-136564333234-
        c7062029b92267c3a4360ee3d55fd385""")


def send_error_message(message: str):
    sc.api_call(
        "chat.postMessage",
        channel="@johnkellyguitar",
        text="I'm Broke\n" + message,
        username="Jeffery"
    )


def format_report(data: dict) -> list:
    formatted_report = []
    for key in data:
        formatted_report.append({
            'text': key + ': ' + str(data[key]),
            'color':  'good' if data[key] > 50 else 'danger'
        })
    return formatted_report


def send_report(report: dict):
    sc.api_call(
        "chat.postMessage",
        channel="@johnkellyguitar",
        text="You requested a report every 6 hours, this is how we're doing",
        attachments=format_report(report),
        username="Jeffery"
    )


def send_completed_message(accuracy: int):
    sc.api_call(
        "chat.postMessage",
        channel="@johnkellyguitar",
        text="I'm done\nAccuracy: " + str(accuracy) + "%",
        username="Jeffery"
    )
