# Maintainer: pileton
pkgname=rigby-launcher
pkgver=0.7
pkgrel=1
pkgdesc="Rigby Launcher — a native launcher for Among Us with game version management, auto-download, and itch.io login fixer"
arch=('any')
url="https://github.com/pileton/rigby-launcher"
license=('custom: Rigby Launcher License')
depends=('python>=3.8' 'python-gobject' 'webkit2gtk-4.1' 'wine')
makedepends=('python-setuptools')
source=("$pkgname-$pkgver.tar.gz")
sha256sums=('6e39a80e20a3b9e336dfdbea8a221c5be0e950b1e2dea11f33d84c33e4b90ba3')

package() {
  cd "$srcdir/$pkgname-$pkgver"

  mkdir -p "$pkgdir/usr/bin"
  cat > "$pkgdir/usr/bin/$pkgname" <<EOF
#!/bin/sh
exec env PYTHONPATH="/usr/share/$pkgname:\$PYTHONPATH" python3 -m rigby_launcher "\$@"
EOF
  chmod 755 "$pkgdir/usr/bin/$pkgname"

  mkdir -p "$pkgdir/usr/share/$pkgname"
  cp -r rigby_launcher "$pkgdir/usr/share/$pkgname/"
  chmod +x "$pkgdir/usr/share/$pkgname/rigby_launcher/__main__.py"

  mkdir -p "$pkgdir/usr/share/applications"
  cat > "$pkgdir/usr/share/applications/$pkgname.desktop" <<EOF
[Desktop Entry]
Name=Rigby Launcher
Comment=Launch and manage Among Us
Exec=$pkgname
Icon=$pkgname
Terminal=false
Type=Application
Categories=Game;
EOF

  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
