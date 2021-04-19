import asyncio
from pathlib import Path
import shutil


_dir = Path(__file__).parent


class PacketUI:
    def __init__(
            self, src_dir: Path,
            dist_dir: Path,
            node_modules_dir: Path):
        self.src_dir = src_dir.resolve()
        self.dist_dir = dist_dir.resolve()
        self.node_modules_dir = node_modules_dir

    async def build(self):

        # Copy fonts
        print('Copy fonts ...')
        src_dir = self.src_dir.joinpath('font')
        dest_dir = self.dist_dir.joinpath('font')
        shutil.copytree(
            src_dir,
            dest_dir,
            dirs_exist_ok=True,
        )
        print('Finished')

        # Copy normalize.css
        print('Copy normalize.css')
        src = self.node_modules_dir.joinpath('normalize.css/normalize.css')
        dest = self.dist_dir.joinpath('normalize.css')
        shutil.copyfile(src, dest)
        print('Finished')

        # Build packet-ui.js
        cmd = f"npx parcel build --dist-dir {self.dist_dir} " +\
            f"{self.src_dir.joinpath('packet-ui.js')}"
        print(f'{cmd} ...')
        proc = await asyncio.create_subprocess_shell(cmd)
        await proc.communicate()
        print('Finished')

        # Build packet-ui.scss
        cmd = "npx sass --style=compressed " +\
            f"{self.src_dir.joinpath('packet-ui.scss')} " +\
            f"{self.dist_dir.joinpath('packet-ui.css')}"
        print(f'{cmd} ...')
        proc = await asyncio.create_subprocess_shell(cmd)
        await proc.communicate()
        print('Finished')


async def main():
    packet_ui = PacketUI(
        src_dir=_dir.joinpath('src'),
        dist_dir=_dir.joinpath('dist'),
        node_modules_dir=_dir.joinpath('node_modules')
    )
    await packet_ui.build()


asyncio.run(main())
