from slackclient import SlackClient
from re import findall

sc = SlackClient("""xoxp-113334704304-114716829062-136564333234-c7062029b92267c3a4360ee3d55fd385""")


def send_error_message(message):
    sc.api_call(
        "chat.postMessage",
        channel="@johnkellyguitar",
        text="I'm Broke\n" + message,
        username="Jeffery"
    )


def send_report(report):
    formatted_report = []
    for key in report:
        formatted_report.append({
            'text': key + ': ' + str(report[key]),
            'color':  'good' if report[key] > 50 else 'danger'
        })
    sc.api_call(
        "chat.postMessage",
        channel="@johnkellyguitar",
        text="You requested a report every 6 hours, this is how we're doing",
        attachments=formatted_report,
        username="Jeffery"
    )


def send_completed_message(accuracy):
    sc.api_call(
        "chat.postMessage",
        channel="@johnkellyguitar",
        text="I'm done\nAccuracy: " + str(accuracy) + "%",
        username="Jeffery"
    )
