#!/usr/bin/env bash
set -euo pipefail
echo "User: $(whoami)"
echo "Date: $(date -u +"%Y-%m-%d %H:%M:%S %Z")"
echo "Hostname: $(hostname)"
echo
echo "Disk usage:"
df -h

