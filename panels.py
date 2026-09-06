"""Panel UI for ConvertKit (Kit) Connector following UI_INTERFACE_STANDARD.md and AUTH_AND_CREDENTIALS_STANDARD.md."""
from __future__ import annotations
from imperal_sdk import ui
from app import ext

def _settings_button() -> ui.UINode:
    return ui.Button(
        "App settings",
        variant="secondary",
        size="sm",
        icon="settings",
        on_click=ui.Call("__panel__convertkit_settings")
    )

def _help_modal() -> ui.UINode:
    return ui.Modal(
        trigger=ui.Button("How do I set this up?", variant="ghost", size="sm"),
        title="Connecting Kit (ConvertKit)",
        children=[
            ui.Text(
                "1. Sign in to your Kit (ConvertKit) account and go to Settings > Advanced > API.
2. Copy your API Key or OAuth Bearer Token.
3. Paste it in the API Key field above and click Connect.
4. Ensure your token has permissions for subscribers, broadcasts, tags, sequences, and forms.",
                variant="body"
            )
        ]
    )

@ext.panel("convertkit_sidebar", slot="left")
async def convertkit_sidebar(ctx, **kwargs) -> ui.UINode:
    return ui.Stack(
        direction="v",
        gap=3,
        align="stretch",
        children=[
            ui.Text("Kit (ConvertKit)", variant="heading"),
            ui.Stack(
                direction="v",
                gap=1,
                align="stretch",
                children=[
                    ui.Text("Manage your Kit email subscribers, broadcasts, and automation sequences.", variant="caption"),
                ]
            ),
            ui.Divider(),
            ui.Stack(
                direction="v",
                gap=2,
                align="stretch",
                children=[
                    ui.Input(
                        name="label",
                        label="Connection Label",
                        placeholder="e.g. Creator Account",
                        type="text"
                    ),
                    ui.Input(
                        name="api_key",
                        label="Kit API Key / Bearer Token",
                        placeholder="Paste your Kit v4 API key or token",
                        type="password"
                    ),
                    ui.Input(
                        name="base_url",
                        label="API Endpoint (Optional)",
                        placeholder="https://api.kit.com/v4",
                        type="text"
                    ),
                    ui.Button(
                        "Connect Kit",
                        variant="primary",
                        on_click=ui.Call("connect_convertkit")
                    ),
                ]
            ),
            ui.Divider(),
            ui.Stack(
                direction="h",
                gap=2,
                align="center",
                children=[
                    _settings_button(),
                    _help_modal(),
                ]
            )
        ]
    )
