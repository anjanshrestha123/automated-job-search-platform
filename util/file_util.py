from config import config
from dto.job import Job
from dto.job_status import JobStatus
import fitz


def fetch_job_list():
    job_list = []
    for job_info in open(config.get_job_list_file_path(), 'r').read().splitlines():
        job_info_split = job_info.split(',')
        job_list.append(Job(job_info_split[0], None, JobStatus[job_info_split[1]]))

    return job_list


def fetch_resume_content():
    document = fitz.open(config.get_resume_file_path())

    # Extract resume content
    resume_content = '\n'.join([document.load_page(page_num).get_text() for page_num in range(document.page_count)])

    return resume_content


def update_job_list(jobs, update_mode):
    with open(config.get_job_list_file_path(), update_mode) as file:
        for job in jobs:
            if job is not None:
                job_info = config.get_job_info(job)
                file.write('{}\n'.format(job_info))


def update_job_status(job_id, job_status):
    # Fetch all jobs from file
    jobs = fetch_job_list()

    # Update status
    for job in jobs:
        if job.id == job_id:
            job.status = job_status

    # Update the whole file with new status
    update_job_list(jobs, 'w')
