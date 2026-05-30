# Service Toggle

A lightweight **GTK4 / Adwaita** app for Ubuntu that lets you start and stop
background services with one click, and switch CPU core counts to control
power consumption — all without opening a terminal.

![screenshot placeholder](data/icons/service-toggle.svg)

---

## Features

| | |
|---|---|
| 🐳 Docker | Start / stop containers on demand |
| 🤖 Ollama | Local AI model server |
| 🖥 Virtual Machines | KVM / QEMU via libvirt |
| 🖨 Printing | CUPS print spooler |
| 📶 Bluetooth | Bluetooth stack |
| 🔒 Tailscale | Tailscale VPN |
| 📡 Avahi | Local network mDNS discovery |
| ⚡ CPU Presets | Switch between 8 / 16 / max cores |

- Live **core activity bar** shows which CPUs are active
- **Spinner** feedback while services start/stop
- **Refresh** button to re-check all states
- Works without a password (uses your existing `sudo` rules)
- Pins to the GNOME dock correctly

---

## Requirements

- Ubuntu 24.04+ (or any distro with GNOME 46+, GTK4, Adwaita)
- Python 3.10+
- `python3-gi`, `gir1.2-adw-1`, `gir1.2-gtk-4.0`
- `systemd` + `sudo`

---

## Install

### Option 1 — .deb (recommended)

Download the latest `.deb` from [Releases](../../releases/latest) then:

```bash
sudo dpkg -i service-toggle_*.deb
sudo apt-get install -f   # install any missing dependencies
```

### Option 2 — Flatpak (any Linux distro)

Download `service-toggle.flatpak` from [Releases](../../releases/latest) then:

```bash
flatpak install service-toggle.flatpak
```

### Option 3 — Manual (one command)

```bash
git clone https://github.com/oguzemrebal/service-toggle
cd service-toggle
sudo cp service_toggle/__main__.py /usr/local/bin/service-toggle
sudo chmod +x /usr/local/bin/service-toggle
sudo cp data/service-toggle.desktop /usr/share/applications/
sudo cp data/icons/service-toggle.svg /usr/share/icons/hicolor/scalable/apps/
sudo gtk-update-icon-cache -f /usr/share/icons/hicolor/
sudo update-desktop-database /usr/share/applications/
```

---

## Sudo setup (passwordless)

The app uses `sudo systemctl` and `sudo tee` to control services and CPU cores.
Add this to `/etc/sudoers.d/service-toggle` so it works without a password prompt:

```
%sudo ALL=(ALL) NOPASSWD: /usr/bin/systemctl, /usr/bin/tee /sys/devices/system/cpu/*/online
```

---

## Building from source

```bash
git clone https://github.com/oguzemrebal/service-toggle
cd service-toggle
pip install build
python -m build
```

Or build the `.deb` manually:

```bash
cd packaging/deb
dpkg-deb --root-owner-group --build service-toggle_1.0.0
```

---

## Publishing a new release

```bash
git tag v1.0.1
git push origin v1.0.1
```

GitHub Actions will automatically build the `.deb` and `.flatpak`, then create a release.

---

## License

[GPL-3.0](LICENSE)
