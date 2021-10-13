import asyncio

from scripts.data_cleaning import create_frame as s_cf


async def request_data(bsm, engine):
    socket = bsm.trade_socket('BTCUSDT')

    while True:

        await socket.__aenter__()
        msg = await socket.recv()

        frame = s_cf(msg)
        frame.to_sql('BTCUSDT', engine, if_exists='append', index=False)
        print(frame)