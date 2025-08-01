from fastapi import APIRouter

router = APIRouter()

@router.get("/dashboard", summary="Главный экран", description="Отображает сводку данных по криптовалютам")
async def get_dashboard():
    return {
        "title": "Crypto Analyzer Dashboard",
        "menu": ["Home", "Analyze", "Strategies", "Backtest", "Settings"],
        "data": {
            "market_cap": "1.5T",
            "btc_price": "65000",
            "eth_price": "3500"
        }
    }

