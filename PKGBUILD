pkgname=kavach-xedu
pkgver=1
pkgrel=1
pkgdesc="Study APP for Kavach OS"
arch=('any')
url="https://github.com/Project-K-Official/kavach-studyblu"
license=('GPL3.0')
depends=('python3' 'python-pyqt5')
makedepends=('git')
source=("git+$url.git")
sha256sums=('SKIP')

package() {
        install -d  ${pkgdir}/usr/share/kavach-xedu
        install -d  ${pkgdir}/usr/share/applications
        install -d  ${pkgdir}/usr/bin/xedu
        install -d  ${pkgdir}/etc/skel/.config/autostart

	cp -r  ${srcdir}/kavach-studyblu/xedu/* "${pkgdir}/usr/bin/xedu/"
	cp -r ${srcdir}/kavach-studyblu/xedu/main.py "${pkgdir}/usr/bin/xedu/kavach-xedu"	
	chmod +x "${pkgdir}/usr/bin/xedu/kavach-xedu"

	cp -r ${srcdir}/kavach-studyblu/kedu.desktop "${pkgdir}/etc/skel/.config/autostart/kavach-StudyBlu.desktop"
	chmod +x "${pkgdir}/etc/skel/.config/autostart/kavach-StudyBlu.desktop"
     
	cp -r ${srcdir}/kavach-studyblu/kedu.desktop "${pkgdir}/usr/share/applications/kavach-SudyBlu.desktop"
}
