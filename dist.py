import asyncio
from pathlib import Path


class PacketUI:
    def __init__(
            self, src_dir: Path,
            dist_dir: Path,
            node_modules_dir: Path):
        self.src_dir = src_dir.resolve()
        self.dist_dir = dist_dir.resolve()
        self.node_modules_dir = node_modules_dir

    async def build(self):
        # Build packet-ui.js
        cmd = f"npx parcel build --dist-dir {self.dist_dir} " +\
            f"{self.src_dir.joinpath('packet-ui.js')}"
        print(f'{cmd} ...')
        proc = await asyncio.create_subprocess_shell(cmd)
        await proc.communicate()
        print('Finished')

        # Build SCSS
        cmd = "npx sass --style=compressed " +\
            f"{self.src_dir.joinpath('packet-ui.scss')} " +\
            f"{self.dist_dir.joinpath('packet-ui.css')}"
        print(f'{cmd} ...')
        proc = await asyncio.create_subprocess_shell(cmd)
        await proc.communicate()
        print('Finished')


async def main():
    base_dir = Path(__file__).parent
    packet_ui = PacketUI(
        src_dir=base_dir.joinpath('src'),
        dist_dir=base_dir.joinpath('dist'),
        node_modules_dir=base_dir.joinpath('node_modules')
    )
    await packet_ui.build()


asyncio.run(main())
