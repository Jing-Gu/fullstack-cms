import uuid
import re
from fastapi import APIRouter, HTTPException
from app.api.v1.database.db import get_portfolios, get_reports_from_portfolio, save_portfolios, save_reports, get_report_by_uuid

router = APIRouter()

def generate_uuid():
    return str(uuid.uuid4())


def create_slug(name):
    return re.sub(r'\W+', '-', name.lower())


@router.get("/list")
async def get_portfolios_list():
    return get_portfolios()


@router.get("/{pf_slug}/menu")
async def get_portfolio_menu(pf_slug: str): # for kendo menu
    for portfolio in get_portfolios():
        if portfolio['slug'] == pf_slug:
            if 'menu' not in portfolio or not portfolio['menu']:
                return {"menu": []}
            return portfolio['menu']
    raise HTTPException(status_code=404, detail=f"Portfolio {pf_slug} not found")


# TODO: update menu by post and put


@router.post("/{pf_slug}/reports")
async def create_report(pf_slug: str, report: dict):
    for portfolio in get_portfolios():
        if portfolio['slug'] == pf_slug:
            report['uuid'] = generate_uuid()
            report['slug'] = create_slug(report['name'])
            save_reports(pf_slug, report)
            # menu levels should be updated by now, then add just uuid to the menu
            return report
    raise HTTPException(status_code=404, detail=f"Portfolio {pf_slug} not found")


@router.get("/{pf_slug}/reports")
async def get_reports(pf_slug: str):
    reports = get_reports_from_portfolio(pf_slug)
    if reports:
        return reports
    raise HTTPException(status_code=404, detail=f"Portfolio {pf_slug} not found")


@router.get("/{pf_slug}/reports/{report_uuid}")
async def get_report(pf_slug: str, report_uuid: str):
    report = get_report_by_uuid(pf_slug, report_uuid)
    if report:
        return report
    raise HTTPException(status_code=404, detail=f"Report with uuid {report_uuid} is not found in portfolio {pf_slug}")

