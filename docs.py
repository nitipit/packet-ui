import asyncio
import shutil
from pathlib import Path


_dir = Path(__file__).parent


def lib():
    shutil.copytree(
        _dir.joinpath('node_modules/adwaita-icon-web/dist/'),
        'docs/lib/adwaita-icon-web/',
        dirs_exist_ok=True)
    shutil.copytree(
        _dir.joinpath('dist/'),
        'docs/lib/packet-ui/dist/',
        dirs_exist_ok=True)


async def packet_ui_js():
    src = _dir.joinpath('src/packet-ui.js')
    dest_dir = _dir.joinpath('docs/')
    cmd = (
        f"npx parcel watch '{src}' "
        f"--dist-dir='{dest_dir}'"
    )
    print(f'{cmd} ...')
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)
    await proc.communicate()
    print('Finished')


async def packet_ui_scss():
    src = _dir.joinpath('docs-src/packet-ui.scss')
    dest = _dir.joinpath('docs/base.css')
    cmd = f"npx sass --watch {src} {dest}"
    print(f'{cmd} ...')
    proc = await asyncio.create_subprocess_shell(cmd)
    await proc.communicate()
    print('Finished')


async def engrave():
    cmd = 'engrave dev --server 127.0.0.1:8000 docs-src docs'
    proc = await asyncio.create_subprocess_shell(cmd)
    await proc.communicate()


async def main():
    lib()
    await asyncio.gather(
        engrave(),
        # packet_ui_js(),
        # packet_ui_scss(),
    )

asyncio.run(main())
