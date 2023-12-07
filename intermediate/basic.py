import asyncio


async def send_hello() -> None:
    await asyncio.sleep(2)
    print("Hello")



async def send_bye() -> None:
    await asyncio.sleep(1)
    print('Bye!')


async def main():
    task_1 = asyncio.create_task(send_hello())
    task_2 = asyncio.create_task(send_bye())


    await task_1
    await task_2


asyncio.run(main())



# asyncio.run(send_hello())
# asyncio.run(send_bye())


# def send_helo() -> None: # block 1
#     print('Hello!')
#
#
# def send_bye() -> None: # block 2
#     print('Bye!')
#
#
# send_helo()
# send_bye()
