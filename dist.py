import asyncio
from pathlib import Path
import shutil


class PacketUI:
    def __init__(
            self, src_dir: Path,
            dist_dir: Path,
            node_modules_dir: Path):
        self.src_dir = src_dir.resolve()
        self.dist_dir = dist_dir.resolve()
        self.node_modules_dir = node_modules_dir

    async def _src_copy(self):
        # Copy SCSS
        src_dir = self.src_dir.joinpath('style')
        dest_dir = self.dist_dir.joinpath('style')
        print(f'copy: {src_dir} -> {dest_dir} ...')
        shutil.copytree(src_dir, dest_dir, dirs_exist_ok=True)
        print('Finished')

        # Copy UI JS & SCSS
        src_dir = self.src_dir.joinpath('ui')
        dest_dir = self.dist_dir.joinpath('ui')
        print(f'copy: {src_dir} -> {dest_dir} ...')
        shutil.copytree(src_dir, dest_dir, dirs_exist_ok=True)
        print('Finished')

        cmd = f"npx parcel build --dist-dir {self.dist_dir} " +\
            f"{self.node_modules_dir.joinpath('normalize.css/normalize.css')}"
        print(f'{cmd} ...')
        proc = await asyncio.create_subprocess_shell(cmd)
        await proc.communicate()
        print('Finished')

        # Copy Fonts
        src_dir = self.src_dir.joinpath('font')
        dest_dir = self.dist_dir.joinpath('font')
        print(f'copy: {src_dir} -> {dest_dir} ...')
        shutil.copytree(
            src_dir,
            dest_dir,
            dirs_exist_ok=True,
        )
        print('Finished')

    async def build(self):
        # Build packet-ui.js
        cmd = f"npx parcel build --dist-dir {self.dist_dir} " +\
            f"{self.src_dir.joinpath('packet-ui.js')}"
        print(f'{cmd} ...')
        proc = await asyncio.create_subprocess_shell(cmd)
        await proc.communicate()
        print('Finished')

        # Build SCSS
        cmd = f"npx sass --style=compressed {self.src_dir}:{self.dist_dir}"
        print(f'{cmd} ...')
        proc = await asyncio.create_subprocess_shell(cmd)
        await proc.communicate()
        print('Finished')

        # Copy source files
        await self._src_copy()


async def main():
    base_dir = Path(__file__).parent
    packet_ui = PacketUI(
        src_dir=base_dir.joinpath('src'),
        dist_dir=base_dir.joinpath('dist'),
        node_modules_dir=base_dir.joinpath('node_modules')
    )
    await packet_ui.build()


asyncio.run(main())
