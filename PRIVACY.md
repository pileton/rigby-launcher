# Rigby Launcher Privacy Policy

Rigby Launcher sends one anonymous install event when a new installation
starts. The event only says that a new installation started. It does not
include your name, itch.io account, game data, settings, installed mods, or a
persistent identifier.

On first launch, a prompt lets you choose whether to include your operating
system family (for example, Windows or Linux) in that event. Choosing
**Install count only** sends the install event without the OS field. This lets
us count installations without knowing who installed the launcher.

The event is sent through a proxy to a private Discord webhook. The proxy keeps
the webhook URL private. As with any web request, the proxy and Discord may
process standard request metadata such as IP address and time; the launcher
does not add those fields itself.

The event is sent at most once per installation. Local markers in the
launcher's data folder prevent repeats and rate limiting. Failed attempts are
not retried automatically. Existing installations are not counted as new users.

For questions or removal requests, open an issue at
<https://github.com/pileton/rigby-launcher/issues>.
