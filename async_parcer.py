import asyncio
import aiohttp
import json
import sys


async def foo_1(session):
    dates = ['2023-01-10', '2023-01-11', '2023-01-12']
    total_value = 0
    for a in dates:
        data = await session.get(f'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/{a}/currencies/uah.json')
        jn = await data.json()
        usd_value = jn['uah']['usd']
        total_value += float(usd_value)
    average_value = total_value / 3
    return average_value
    # print(f'Average usd prise durin 3 days is {average_value} usd per one uah')


async def foo_2(session):
    data = await session.get('https://hp-api.onrender.com/api/characters')
    jn = await data.json()
    q = 0  # quantity of characters
    wand_length_total = 0
    for a in jn:
        wand_length = a['wand']['length']
        if wand_length is None:
            pass
        else:
            wand_length_total += wand_length
            q += 1
    average_wands_length = wand_length_total / q
    return average_wands_length
    # print(f'Average length of known wand of Harry Potter characters is {average_wands_length}')


async def foo_3(session):
    data = await session.get(
        'https://api.open-meteo.com/v1/forecast?latitude=50.45&longitude=30.52&hourly=temperature_2m')
    jn = await data.json()
    time1 = jn['hourly']['temperature_2m'][7]
    time2 = jn['hourly']['temperature_2m'][13]
    time3 = jn['hourly']['temperature_2m'][19]
    time4 = jn['hourly']['temperature_2m'][25]
    average_temp = (time1 + time2 + time3 + time4) / 4
    return average_temp
    # print(f'Average temperature in Kiev is {average_temp} C')


async def main():
    loop = asyncio.get_running_loop()
    async with aiohttp.ClientSession(loop=loop) as session:
        results = await asyncio.gather(foo_1(session), foo_2(session), foo_3(session))
    print(results)


if __name__ == '__main__':
    asyncio.run(main())
