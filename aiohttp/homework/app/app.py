import json

from aiohttp import web
from sqlalchemy.exc import IntegrityError

from db import Session, engine
from models import Base, AdvModel
from validate import validate, AdvPostModel, AdvPatchModel


app = web.Application()


async def get_adv(adv_id, session):
    adv = await session.get(AdvModel, adv_id)
    if adv is None:
        raise web.HTTPNotFound(
            text=json.dumps({'Status': 'error', 'description': 'adv not found'}),
            content_type='application/json'
        )
    return adv


class Advs(web.View):
    async def get(self):
        adv_id = int(self.request.match_info['adv_id'])
        async with Session() as session:
            adv = await get_adv(adv_id, session)
            return web.json_response(
                {
                    'id': adv.id,
                    'header': adv.header,
                    'description': adv.description,
                    'owner': adv.owner,
                    'creation_date': adv.creation_date.isoformat(),
                }
            )

    async def post(self):
        adv_post_data = await self.request.json()
        async with Session() as session:
            new_adv = AdvModel(**validate(adv_post_data, AdvPostModel))
            session.add(new_adv)
            try:
                await session.commit()
            except IntegrityError:
                raise web.HTTPConflict(
                    text=json.dumps(
                        {
                        'status': 'error',
                        'description': 'adv already exists'
                        }
                    ),
                    content_type='application/json'
                )
            return web.json_response(
                    {
                        'id': new_adv.id,
                        'owner': new_adv.owner,
                        'header': new_adv.header,
                        'description': new_adv.description,
                    }
                )

    async def patch(self):
        adv_id = int(self.request.match_info['adv_id'])
        adv_patch_data = validate(await self.request.json(), AdvPatchModel)
        async with Session() as session:
            adv = await get_adv(adv_id, session)
            for key, value in adv_patch_data.items():
                setattr(adv, key, value)
                session.add(adv)
                await session.commit()
            return web.json_response({'patch status': 'success'})


    async def delete(self):
        adv_id = int(self.request.match_info['adv_id'])
        async with Session() as session:
            adv = await get_adv(adv_id, session)
            await session.delete(adv)
            await session.commit()
            return web.json_response({'delete status': 'success'})


async def orm_context(app):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        await conn.commit()
    yield
    await engine.dispose()


app.cleanup_ctx.append(orm_context)


app.add_routes(
    [
        web.get("/advs/{adv_id:\d+}", Advs),
        web.post("/advs/", Advs),
        web.patch("/advs/{adv_id:\d+}", Advs),
        web.delete("/advs/{adv_id:\d+}", Advs),
    ]
)


if __name__ == "__main__":
    web.run_app(app)
