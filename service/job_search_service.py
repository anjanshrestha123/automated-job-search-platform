from proxy import indeed_proxy
from util import file_util
from dto.job_status import JobStatus
from proxy import gemini_proxy

def search_job():
    print('Searching indeed for jobs matching the parameters')
    jobs = indeed_proxy.fetch_jobs()

    if len(jobs) > 0:
        print('Reading resume content')
        resume_content = file_util.fetch_resume_content()

        print('Updating job status by calling Google Gemini Service and comparing job\'s description with resume')
        update_job_status(resume_content, jobs)

        print('Updating the file with job id and job status')
        file_util.update_job_list(jobs, 'a')
    else:
        print('No new jobs found')


def update_job_status(resume_content, jobs):
    for job in jobs:
        try:
            if not gemini_proxy.is_match(resume_content, job.description):
                job.status = JobStatus.NOT_QUALIFIED
        except Exception as e:
            print("An unexpected error occurred:", e)
            if job is not None:
                job.status = JobStatus.APPLICATION_ERROR
