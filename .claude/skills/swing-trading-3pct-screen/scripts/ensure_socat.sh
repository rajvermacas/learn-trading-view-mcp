#!/usr/bin/env bash

set -euo pipefail

PORT="9222"
LISTEN_SPEC="TCP-LISTEN:${PORT},bind=127.0.0.1,reuseaddr,fork"
TARGET_SPEC="TCP:host.docker.internal:${PORT}"
MATCH="socat ${LISTEN_SPEC} ${TARGET_SPEC}"

log() {
    printf '[ensure_socat] %s\n' "$1"
}

if ! command -v socat >/dev/null 2>&1; then
    log "ERROR: socat is not installed"
    exit 1
fi

if pgrep -af "${MATCH}" >/dev/null 2>&1; then
    log "socat tunnel already running"
    exit 0
fi

log "starting socat tunnel on 127.0.0.1:${PORT}"
nohup socat "${LISTEN_SPEC}" "${TARGET_SPEC}" >/tmp/swing-trading-socat.log 2>&1 &
sleep 1

if pgrep -af "${MATCH}" >/dev/null 2>&1; then
    log "socat tunnel started"
    exit 0
fi

log "ERROR: failed to start socat tunnel"
log "See /tmp/swing-trading-socat.log for details"
exit 1
