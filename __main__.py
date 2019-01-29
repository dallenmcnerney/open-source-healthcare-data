from request_data import save_web_file

# Medicare exclusion list
exclusion_list_url = 'https://oig.hhs.gov/exclusions/downloadables/UPDATED.csv'

save_web_file(exclusion_list_url, 'mdc_exclusion_list.csv')
