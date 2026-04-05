windows:
"C:\Program Files\Google\Chrome\Application\chrome.exe"  --remote-debugging-port=9222 --remote-debugging-address=0.0.0.0 --user-data-dir="C:\Projects\learn-trading-view-mcp\chrome-host"

devpod:
curl -H 'Host: localhost' http://host.docker.internal:9222/json

apt-get update && apt-get install -y socat
socat TCP-LISTEN:9222,bind=127.0.0.1,reuseaddr,fork TCP:host.docker.internal:9222
curl -H 'Host: localhost' http://localhost:9222/json


git clone https://github.com/LewisWJackson/tradingview-mcp-jackson.git

~/.codex/config.toml
[mcp_servers.tradingview]
command = "node"
args = ["/workspaces/learn-trading-view-mcp/tradingview-mcp-jackson/src/server.js"]
enabled = true
