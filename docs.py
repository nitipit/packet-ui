import asyncio
import shutil
from pathlib import Path


_dir = Path(__file__).parent


def lib():
    shutil.copytree(
        _dir.joinpath('node_modules/adwaita-icon-web/dist/'),
        'docs/_lib/adwaita-icon-web/',
        dirs_exist_ok=True)
    shutil.copytree(
        _dir.joinpath('node_modules/highlight.js/styles/'),
        'docs/_lib/highlight.js/',
        dirs_exist_ok=True)


async def engrave():
    proc = await asyncio.create_subprocess_shell(
        'engrave dev --server 127.0.0.1:8000 docs-src docs')
    await proc.communicate()


async def packet_ui_js():
    src = _dir.joinpath('src/packet-ui.js')
    dest_dir = _dir.joinpath('docs/_lib/packet-ui/')
    proc = await asyncio.create_subprocess_shell(
        f"npx parcel watch '{src}' --dist-dir='{dest_dir}'"
    )
    await proc.communicate()


async def packet_ui_css():
    src = _dir.joinpath('src/packet-ui.scss')
    dest = _dir.joinpath('docs/_lib/packet-ui/packet-ui.css')
    proc = await asyncio.create_subprocess_shell(
        f"npx sass --watch {src} {dest}"
    )
    await proc.communicate()


async def main():
    lib()
    await asyncio.gather(
        packet_ui_js(),
        packet_ui_css(),
        engrave(),
    )

asyncio.run(main())
