#!/bin/sh
cd "$(dirname "$0")"
exec python3 -m rigby_launcher "$@"
