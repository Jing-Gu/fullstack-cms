import json
import os
import logging
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()

JSON_FILE_PATH = 'json/portfolios.json'


def get_portfolios_from_json():
    if os.path.exists(JSON_FILE_PATH):
        with open(JSON_FILE_PATH, 'r') as file:
            return json.load(file)
    return []


def save_portfolios_to_json(data):
    with open(JSON_FILE_PATH, 'w') as file:
        json.dump(data, file, indent=4)


def get_reports_from_portfolio_from_json(pf_slug):
    file_path = f'json/{pf_slug}.json'
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    return []


def save_reports_to_json(pf_slug, report):
    file_path = f'json/{pf_slug}.json'
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            reports = json.load(file)
    else:
        reports = []

    reports.append(report)
    with open(file_path, 'w') as file:
        json.dump(reports, file, indent=4)


def get_report_by_uuid_from_json(pf_slug, uuid):
    reports = get_reports_from_portfolio_from_json(pf_slug)
    if reports:
        for report in reports:
            if report['uuid'] == uuid:
                return report
    else:
        return None


def get_portfolios_from_dynamodb():
    # Load data from DynamoDB
    pass


def save_portfolios_to_dynamodb(data):
    # Save data to DynamoDB
    pass


def get_reports_from_portfolio_from_dynamodb(pf_slug):
    # Load data from DynamoDB
    pass


def save_reports_to_dynamodb(pf_slug, report):
    # Save data to DynamoDB
    pass


def get_report_by_uuid_from_dynamodb(pf_slug, uuid):
    # Get data from DynamoDB
    pass


# Abstracted functions to load and save data
def get_portfolios():
    if os.getenv('ENV') == 'production':
        return get_portfolios_from_dynamodb()
    else:
        return get_portfolios_from_json()


def save_portfolios(data):
    if os.getenv('ENV') == 'production':
        save_portfolios_to_dynamodb(data)
    else:
        save_portfolios_to_json(data)


def get_reports_from_portfolio(pf_slug: str):
    print("get reports")
    if os.getenv('ENV') == 'production':
        return get_reports_from_portfolio_from_dynamodb(pf_slug)
    else:
        return get_reports_from_portfolio_from_json(pf_slug)


def save_reports(pf_slug: str, report):
    if os.getenv('ENV') == 'production':
        save_reports_to_dynamodb(pf_slug, report)
    else:
        save_reports_to_json(pf_slug, report)


def get_report_by_uuid(pf_slug: str, uuid: str):
    logger.info(f"Fetching report with UUID {uuid} from portfolio {pf_slug}")
    if os.getenv('ENV') == 'production':
        return get_report_by_uuid_from_dynamodb(pf_slug, uuid)
    else:
        return get_report_by_uuid_from_json(pf_slug, uuid)
