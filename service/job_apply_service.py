from util import file_util
from automation.indeed import job_apply_automation


def apply_job(job_status):
    print('Reading file and filtering in jobs that have not been applied')
    jobs = list(filter(lambda x: x.status == job_status, file_util.fetch_job_list()))
    print('Automating job application process for job ids: [{}]'.format(list(map(lambda x: x.id, jobs))))

    print('Applying job using automation')
    for job in jobs:
        automation_job_status = job_apply_automation.apply_job(job.id)

        print('Updating job status to the file based on automation result')
        file_util.update_job_status(job.id, automation_job_status)

