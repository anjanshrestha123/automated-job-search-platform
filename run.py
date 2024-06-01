from service import job_search_service
from service import job_apply_service
from dto.job_status import JobStatus

# Run the search and apply
job_search_service.search_job()
job_apply_service.apply_job(JobStatus.NOT_APPLIED)

# Reprocess automation error jobs
# job_apply_service.apply_job(JobStatus.AUTOMATION_NOT_SUPPORTED)