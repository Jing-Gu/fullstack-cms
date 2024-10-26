from fastapi import APIRouter
import json

router = APIRouter()

with open('json/portfolios.json', 'r') as file:
    portfolios_data = json.load(file)


@router.get("/list")
async def read_portfolios_list():
    return portfolios_data


@router.get("/{portfolio_name}/reports/{uuid}")
async def get_report_by_uuid(uuid: str):
    return {"get_report_by_uuid": uuid}