from fastapi import APIRouter, Request, Body, HTTPException

document_router = APIRouter(prefix="/documents")


@document_router.post("/")
def process_tree(request: Request, tree: dict | str = Body(...)):
    try:
        service = request.state.service
        return service.parse(tree)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
