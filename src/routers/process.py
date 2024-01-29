from fastapi import APIRouter, Request, Body, HTTPException

process_router = APIRouter(prefix="/v1")


@process_router.post("/parse_tree")
async def process_tree(request: Request, tree: dict | str = Body(...)):
    try:
        service = request.state.service
        return await service.parse(tree)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
