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
    cmd = 'engrave dev --server 127.0.0.1:8000 docs-src docs'
    proc = await asyncio.create_subprocess_shell(cmd)
    await proc.communicate()


async def packet_ui():
    src = _dir.joinpath('src').relative_to(_dir)
    src = f'{src}/{{packet-ui.js,packet-ui.scss}}'
    dest_dir = _dir.joinpath('docs/_lib/packet-ui/').relative_to(_dir)
    cmd = f"npx parcel watch '{src}' --dist-dir='{dest_dir}' --watch-for-stdin"
    print(cmd)
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,)
    await proc.communicate()


async def main():
    lib()
    await asyncio.gather(
        packet_ui(),
        engrave(),
    )

asyncio.run(main())
