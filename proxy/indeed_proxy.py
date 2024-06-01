import urllib.parse
from bs4 import BeautifulSoup
import time
from zenrows import ZenRowsClient
from dto.job import Job
from dto.job_status import JobStatus
from util import file_util
from config import config


def fetch_jobs():
    fetched_job_ids = set([job_id for i in range(config.get_indeed_total_page_number_to_search()) for job_id in scrape_job_ids(i * 10)])
    existing_job_ids = set([job.id for job in file_util.fetch_job_list()])
    new_job_ids = fetched_job_ids - existing_job_ids

    jobs = [scrape_job_info(job_id) for job_id in new_job_ids]

    return jobs


def get_page_content_soup(job_search_url):
    print('Scrapping: {}'.format(job_search_url))
    client = ZenRowsClient(config.get_web_scraper_zen_rows_api_key())
    page = client.get(job_search_url, params={"js_render": "true"})

    return BeautifulSoup(page.content, "html.parser")


def scrape_job_ids(start):
    job_search_url = config.get_indeed_base_url() + '/jobs/?' + urllib.parse.urlencode(get_job_search_params(start))
    page_content_soup = get_page_content_soup(job_search_url)
    anchor_tags = page_content_soup.findAll('a')

    # Extract job id from the page
    job_ids = [tag.get('data-jk') for tag in anchor_tags if tag.get('data-jk') is not None]
    time.sleep(config.get_web_scraper_request_wait_time())

    return job_ids


def scrape_job_info(job_id):
    params = {
        'jk': job_id
    }
    job_info_url = config.get_indeed_base_url() + '/viewjob/?' + urllib.parse.urlencode(params)
    page_content_soup = get_page_content_soup(job_info_url)

    job_description = page_content_soup.find(id='jobDescriptionText')
    time.sleep(config.get_web_scraper_request_wait_time())

    if job_description is not None:
        return Job(job_id, job_description.text.replace(',', '').replace('\n', ''), JobStatus.NOT_APPLIED)


def get_job_search_params(start):
    params = {
        'q': config.get_indeed_search_keyword(),
        'start': start
    }

    if config.get_indeed_search_location() != 'all':
        params['l'] = config.get_indeed_search_location()

    if config.get_indeed_search_job_type() != 'all':
        params['sc'] = '0kf:jt({});'.format(config.get_indeed_search_job_type())

    return params
