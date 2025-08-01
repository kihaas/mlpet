from fastapi import APIRouter

router = APIRouter()

@router.get("/analyze", summary="Анализ", description="Анализ выбранных криптовалют")
async def analyze_data():
    return {"status": "analyzing", "details": "Analysis started..."}
