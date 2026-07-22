#!/bin/bash
set -e

NAME="rigby-launcher"
VERSION="1.0.0"
ROOT="$(dirname "$(dirname "$(readlink -f "$0")")")"
BUILD="$ROOT/packaging/deb-build"
mkdir -p "$BUILD/DEBIAN"
mkdir -p "$BUILD/usr/bin"
mkdir -p "$BUILD/usr/share/applications"
mkdir -p "$BUILD/usr/share/$NAME"

cp -r "$ROOT/rigby_launcher" "$BUILD/usr/share/$NAME/"

cat > "$BUILD/DEBIAN/control" <<EOF
Package: $NAME
Version: $VERSION
Section: games
Priority: optional
Architecture: all
Depends: python3 (>= 3.8), python3-gi, python3-gi-cairo, gir1.2-webkit2-4.1, wine
Maintainer: pileton
Description: Rigby Launcher
 Rigby Launcher - a launcher for Among Us with game version
 management, auto-download, and itch.io login fixer.
EOF

cat > "$BUILD/usr/bin/rigby-launcher" <<'EOF'
#!/bin/sh
exec /usr/share/rigby-launcher/rigby_launcher/__main__.py "$@"
EOF
chmod +x "$BUILD/usr/bin/rigby-launcher"

cat > "$BUILD/usr/share/applications/rigby-launcher.desktop" <<EOF
[Desktop Entry]
Name=Rigby Launcher
Comment=Launch and manage Among Us
Exec=rigby-launcher
Icon=rigby-launcher
Terminal=false
Type=Application
Categories=Game;
EOF

dpkg-deb --build "$BUILD" "$ROOT/${NAME}_${VERSION}_all.deb"
rm -rf "$BUILD"
echo "Built: ${NAME}_${VERSION}_all.deb"
