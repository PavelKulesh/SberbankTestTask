from fastapi import APIRouter, Request, Body, HTTPException

router_v1 = APIRouter(prefix="/v1")


@router_v1.post("/files")
def process_tree(request: Request, tree: dict | str = Body(...)):
    try:
        service = request.state.service
        return service.parse(tree)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
