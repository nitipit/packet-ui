import asyncio
import shutil
from pathlib import Path


_dir = Path(__file__).parent


def lib():
    shutil.copytree(
        _dir.joinpath('node_modules/adwaita-icon-web/dist/'),
        'docs/lib/adwaita-icon-web/',
        dirs_exist_ok=True)
    shutil.copyfile(
        _dir.joinpath('node_modules/normalize.css/normalize.css'),
        'docs/lib/normalize.css'
    )


async def packet_ui_js():
    cmd = (
        "npx parcel watch 'src/packet-ui.js' "
        "--dist-dir='docs/lib/packet-ui/'"
    )
    print(cmd)
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)
    await proc.communicate()


async def packet_ui_scss():
    cmd = (
        "npx sass --watch src/packet-ui.scss "
        "docs/lib/packet-ui/packet-ui.css"
    )
    print(cmd)
    proc = await asyncio.create_subprocess_shell(cmd)
    await proc.communicate()


async def engrave():
    cmd = 'engrave dev --server 127.0.0.1:8000 docs-src docs'
    proc = await asyncio.create_subprocess_shell(cmd)
    await proc.communicate()


async def main():
    lib()
    await asyncio.gather(
        engrave(),
        packet_ui_js(),
        packet_ui_scss(),
    )

asyncio.run(main())
