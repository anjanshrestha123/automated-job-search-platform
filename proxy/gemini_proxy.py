import google.generativeai as genai
from config import config
from util.common_util import get_first_element
import re

genai.configure(api_key=config.get_gemini_api_key())


def is_match(resume_content, job_description):

    response = genai.GenerativeModel('gemini-1.5-flash').generate_content("Strictly Answer in 0 or 1. Am I eligible to apply the given job based on the provided resume? Exclude manager, director, and lead roles. resume={} and job_description={}"
                                   .format(resume_content, job_description)).text

    return response.upper().startswith('YES') or response.upper().startswith("1")


def fetch_answer(question, profile, returns_number=False):
    try:
        print(f'Question: {question}')
        response = genai.GenerativeModel('gemini-1.5-flash').generate_content("Find answer, provide N/A if there is no answer: Question: {}. My profile = {} "
                        .format(question, profile)).text
        answer = int(get_first_element(re.findall(r'\d+', response), '0')) if returns_number else response.replace('\n', ' ')
        print(f'Answer: {answer}')

        return answer
    except Exception as e:
        print("Error occurred during calling Gemini API: {}".format(e))
        return 'N/A'


def fetch_boolean_answer(question, profile):
    try:
        print(f'Question: {question}')
        response = genai.GenerativeModel('gemini-1.5-flash').generate_content("Strictly Answer in 0 or 1. Question = {} . My profile = {}"
                        .format(question, profile)).text
        answer = 'YES' in response.upper().split(' ') or '1' in response.upper().split(' ')
        print(f'Answer: {answer}')

        return answer
    except Exception as e:
        print("Error occurred during calling Gemini API: {}".format(e))
        return False


def fetch_correct_answer(question, options, profile):
    try:
        print(f'Question: {question}, Options: {options}')
        response = genai.GenerativeModel('gemini-1.5-flash').generate_content("Give me just the option name without extra character. Question = {}, options={}, My profile = {} ".format(
                question, options, profile)).text
        answer = list(filter(lambda x: x.upper() in response.upper() or response.upper() in x.upper(), options))[0]
        print(f'Answer: {answer}')

        return answer
    except Exception as e:
        print("Error occurred during calling Gemini API: {}".format(e))
        return None