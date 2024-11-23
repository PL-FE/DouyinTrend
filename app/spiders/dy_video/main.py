import asyncio

from app.spiders.dy_video.dy import Douyin
from app.controllers.dy import dy_controller

async def main():
    urls = ['https://www.douyin.com/user/MS4wLjABAAAA1eKHyNikJZO_COBSzfGAy_s_U4coVcjaYnVmSAkZHnql8J32jnIuPAPbk_sN8tjQ?from_tab_name=main']
    douyin = Douyin()
    data = douyin.inits(urls)
    print(data)

    await dy_controller.bulk_upsert(data)


if __name__ == '__main__':
   asyncio.run(main())