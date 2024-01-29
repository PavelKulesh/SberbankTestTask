from fastapi import APIRouter, Request, Body, HTTPException

process_router = APIRouter(prefix="/v1")


@process_router.post("/process_tree")
def process_tree(request: Request, tree: dict | str = Body(...)):
    try:
        service = request.state.service
        return service.parse(tree)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
