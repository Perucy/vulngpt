"""
    Author Perucy Mussiba
    Purpose: Utilizes the NVD API to retrieve information from the NVD website for a given CVE
    Project: VulGPT\nvd_api.py

"""

"""
    get_nvd_vuln_description
    
    Args:
        nvd_info (json): a json object containing information about the NVD website for a given CVE
    
    Return: 
        str: CVE's description
"""
def get_nvd_vuln_description(nvd_info):
    return nvd_info['vulnerabilities'][0]['cve']['descriptions'][0]['value']


"""
    gets cvss data for a given CVE
    
    Args:
        nvd_info (json): a json object containing information about the NVD website for a given CVE
        
    Return:
         str: cvss information
"""
def get_cvss_data(nvd_info):
    cvss_info = {}

    for version in nvd_info['vulnerabilities'][0]['cve']['metrics']:
        key = version
        value = nvd_info['vulnerabilities'][0]['cve']['metrics'][version]
        cvss_info[key] = value

    return cvss_info


"""
    gets reference links for a given CVE
    
    Args:
        nvd_info (json): a json object containing information about the NVD website for a given CVE
        
    Return:
        list : CVE's reference links'
        
"""
def get_references(nvd_info):
    return nvd_info['vulnerabilities'][0]['cve']['references']


"""
    gets software configurations for a given CVE
    
    Args:
        nvd_info (json): a json object containing information about the NVD website for a given CVE
        
    Return:
        list : CVE's software configurations'
        
"""
def get_known_software_config(nvd_info):
    return nvd_info['vulnerabilities'][0]['cve']['configurations']
