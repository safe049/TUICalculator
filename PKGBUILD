# Maintainer: safe049 <safe049@163.com>

pkgname=tui-calculator
pkgver=1.0.0
pkgrel=1
pkgdesc="A simple TUI calculator with modern UI."
arch=('any')
url="https://github.com/safe049/TUICalculator"
license=('MIT')
depends=('python')
source=("git+https://github.com/safe049/TUICalculator.git")
md5sums=('SKIP')

package() {
    # 进入项目源目录
    cd "$srcdir/$pkgname"
    
    # 确保 dist 目录存在
    if [ -d "dist" ]; then
        # 将 dist 目录中的 TUIc 文件复制到 /usr/bin
        install -Dm755 dist/TUIc "$pkgdir/usr/bin/TUIc"
    else
        echo "Error: dist directory does not exist."
        exit 1
    fi
}