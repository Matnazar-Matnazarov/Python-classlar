from asyncpg import create_pool
import asyncio
class PostgreSql:
    def __init__(self):
        self.pool = None
#
    async def create(self):
        self.pool = await create_pool(
            user = "postgres",
            password = "1234",
            host = "localhost",
            database = "uquv_markaz"
        )
#
    async def execute(self, sql, fetch=False, fetchval=False, fetchrow=False, execute=False):
        async with self.pool.acquire() as connection:
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(sql)
                elif fetchval:
                    result = await connection.fetchval(sql)
                elif fetchrow:
                    result = await connection.fetchrow(sql)
                elif execute:
                    result = await connection.execute(sql)
            return result

    async def uquvchilar(self):
        sql = f"select * from uquvchilar"
        return await self.execute(sql, fetch=True)
    async def uquvchi_id(self,ism,familiya):
        sql=f"SELECT id FROM uquvchilar WHERE ism='{ism}' and familiya='{familiya}'"
        return await self.execute(sql,fetchval=True)
    async def id_uquvchi(self,id):
        sql=f"SELECT * FROM uquvchilar WHERE id={id}"
        return await self.execute(sql,fetch=True)
    async def change_ism(self,old_ism, new_ism):
        sql= f"UPDATE uquvchilar SET ism='{new_ism}' WHERE ism='{old_ism}'"
        return await self.execute(sql,execute=True)
    async def chiroyli_chiqarish(self,a):
        s=""
        for i in a:
            for j in i:
                s+=str(j)+' '
            s+='\n'
        return s
async def test():
    db = PostgreSql()
    await db.create()
    users = await db.uquvchilar()
    uquvchi_id=await db.uquvchi_id("Valijon","Dosov")
    print(uquvchi_id)
    print(await db.chiroyli_chiqarish(users))
    id_uquvchi=await db.id_uquvchi(2)
    print(await db.chiroyli_chiqarish(id_uquvchi))
    await db.change_ism('Siroj','siroj')
    users = await db.uquvchilar()
    print(await db.chiroyli_chiqarish(users))
    await db.change_ism('siroj','Siroj')
    users = await db.uquvchilar()
    print(await db.chiroyli_chiqarish(users))
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(test())