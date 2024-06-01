import google.generativeai as genai
from config import config

genai.configure(api_key=config.get_gemini_api_key())


def is_match(resume_content, job_description):
    response = genai.generate_text(prompt="Strictly Answer in 0 or 1. Am I eligible to apply the given job based on the provided resume? Exclude manager, director, and lead roles. resume={} and job_description={}"
                                   .format(resume_content, job_description)).result

    return response.upper().startswith("YES") or response.upper().startswith("1")
