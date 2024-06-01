import configparser

# Read App configuration from a file
config = configparser.RawConfigParser()
config.read('app.properties')


def get_indeed_base_url():
    return config.get('App', 'indeed.base.url')


def get_indeed_total_page_number_to_search():
    return int(config.get('App', 'indeed.total.page.number.to.search'))


def get_web_scraper_request_wait_time():
    return int(config.get('App', 'web.scraper.request.wait.time'))


def get_web_scraper_zen_rows_api_key():
    return config.get('App', 'web.scraper.zen.rows.api.key')


def get_gemini_api_key():
    return config.get('App', 'gemini.api.key')


def get_indeed_search_keyword():
    return config.get('App', 'indeed.search.keyword')


def get_indeed_search_location():
    return config.get('App', 'indeed.search.location')


def get_indeed_search_job_type():
    return config.get('App', 'indeed.search.job.type')


def get_job_list_file_path():
    return config.get('App', 'job.list.file.path')


def get_resume_file_path():
    return config.get('App', 'resume.file.path')


def get_job_info(job):
    return config.get('App', 'job.list.file.pattern').format(id=job.id, status=job.status)
