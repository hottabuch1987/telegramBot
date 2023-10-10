import sqlite3 as sq
from create_bot import bot


def sql_start():
    global base, cur
    base = sq.connect('navien.db')
    cur = base.cursor()
    if base:
        print('подключение к базе данных')
    base.execute('CREATE TABLE IF NOT EXISTS catalog(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.commit()

async def sql_add_commanand(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO catalog VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()


async def sql_reload(message):
    try:
        for ret in cur.execute('SELECT * FROM catalog').fetchall():
            await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')
    except:
        await message.reply('Попробуйте еще раз, произошла ошибка')

async def sql_reaload2():
    return cur.execute('SELECT * FROM catalog').fetchall()

async def sql_delete_commanand(data):
    cur.execute('DELETE FROM catalog WHERE name == ?', (data,))
    base.commit()