import json

def handler(event, context):

    print("Event Received")

    plugins = [
        "grafana-clock-panel",
        "grafana-piechart-panel"
    ]

    for plugin in plugins:
        print(f"Configured plugin: {plugin}")

    return {
        "PhysicalResourceId": "GrafanaPluginInstaller",
        "Status": "SUCCESS"
    }
