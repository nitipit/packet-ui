import asyncio
import shutil
from pathlib import Path

_dir = Path(__file__).parent

async def lib():
    shutil.copytree(
        _dir.joinpath('docs-src/asset/'),
        _dir.joinpath('docs/asset/'),
        dirs_exist_ok=True,
    )

async def parcel():
    cmd = "npx parcel watch --no-cache 'docs-src/*.(js|ts|scss)' --dist-dir docs"
    print(cmd)
    proc = await asyncio.create_subprocess_shell(cmd)
    await proc.communicate()

async def engrave():
    cmd = 'engrave dev docs-src docs --server'
    print(cmd)
    proc = await asyncio.create_subprocess_shell(cmd)
    await proc.communicate()

async def main():
    await asyncio.gather(
        lib(),
        parcel(),
        engrave(),
    )

asyncio.run(main())