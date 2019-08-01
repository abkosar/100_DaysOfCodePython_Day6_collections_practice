# Top 10 agencies that has the most job postings and what's the average salary from and salary to
# For those agencies what are the top 5 postings


import csv
from collections import defaultdict, namedtuple, Counter

TOP_AGENCIES = 10
TOP_POSITIONS = 5

Job = namedtuple('Job', 'job_title salary_range_from salary_range_to')


def get_job_postings():
    jobs = defaultdict(list)
    with open('./nyc-jobs.csv', 'rb') as csvfile:
        reader = csv.DictReader(csvfile,
                                delimiter=',',
                                dialect=csv.excel)

        for row in reader:
            job = Job(row['Civil Service Title'],
                      row['Salary Range From'],
                      row['Salary Range To'])
            jobs[row['Agency']].append(job)
    return jobs


def get_number_of_jobs_by_agency(agency_job_defaultdict):
    agency_job_count = dict()
    for agency in agency_job_defaultdict.keys():
        job_list = agency_job_defaultdict[agency]
        agency_job_count[agency] = len(job_list)

    return agency_job_count


def get_top_jobs_by_agency(job_objects_list):
    agencies = job_objects_list.keys()
    agency_job_counts = dict()

    for agency in agencies:
        job_objects = job_objects_list[agency]
        job_names = []

def print_results():
    jobs_by_agencies = get_job_postings()
    job_count_by_agency = get_number_of_jobs_by_agency(jobs_by_agencies)
    job_count_by_agency = sorted(job_count_by_agency.items(), key=lambda x: x[1], reverse=True)

    agency_entry = '{counter}. {agency:<52} {job_count}'
    sep_line = "-" * 40

    print(sep_line)
    for i in range(TOP_AGENCIES):
        print(agency_entry.format(counter=i+1, agency=job_count_by_agency[i][0], job_count=job_count_by_agency[i][1]))
        print(sep_line)


def main():
    print_results()


if __name__ == "__main__":
    main()


