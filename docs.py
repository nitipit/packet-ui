import asyncio
import shutil
from pathlib import Path


_dir = Path(__file__).parent


def lib():
    shutil.copytree(
        _dir.joinpath('node_modules/adwaita-icon-web/dist/'),
        'docs/lib/adwaita-icon-web/',
        dirs_exist_ok=True)


async def engrave():
    cmd = 'engrave dev --server 127.0.0.1:8000 docs-src docs'
    proc = await asyncio.create_subprocess_shell(cmd)
    await proc.communicate()


async def main():
    lib()
    await engrave()

asyncio.run(main())
