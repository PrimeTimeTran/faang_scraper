apple_pages = [
    'https://jobs.apple.com/en-us/search?location=United-States-USA&team=Apps-and-Frameworks-SFTWR-AF',
    'https://jobs.apple.com/en-us/search?location=United-States-USA&team=Cloud-and-Infrastructure-SFTWR-CLD',
    'https://jobs.apple.com/en-us/search?location=United-States-USA&team=Core-Operating-Systems-SFTWR-COS',
    'https://jobs.apple.com/en-us/search?location=United-States-USA&team=DevOps-and-Site-Reliability-SFTWR-DSR',
    'https://jobs.apple.com/en-us/search?location=United-States-USA&team=Engineering-Project-Management-SFTWR-EPM',
    'https://jobs.apple.com/en-us/search?location=United-States-USA&team=Information-Systems-and-Technology-SFTWR-ISTECH',
    'https://jobs.apple.com/en-us/search?location=United-States-USA&team=Machine-Learning-SFTWR-MCHLN',
    'https://jobs.apple.com/en-us/search?location=United-States-USA&team=Acoustic-Technologies-HRDWR-ACT',
    'https://jobs.apple.com/en-us/search?location=United-States-USA&team=Analog-and-Digital-Design-HRDWR-ADD',
    'https://jobs.apple.com/en-us/search?location=United-States-USA&team=Architecture-HRDWR-ARCH',
    'https://jobs.apple.com/en-us/search?location=United-States-USA&team=Battery-Engineering-HRDWR-BE',
    'https://jobs.apple.com/en-us/search?location=United-States-USA&team=Camera-Technologies-HRDWR-CAM',
    'https://jobs.apple.com/en-us/search?location=United-States-USA&team=Display-Technologies-HRDWR-DISP',
    'https://jobs.apple.com/en-us/search?location=United-States-USA&team=Engineering-Project-Management-HRDWR-EPM',
    'https://jobs.apple.com/en-us/search?location=United-States-USA&team=Environmental-Technologies-HRDWR-ENVT',
    'https://jobs.apple.com/en-us/search?location=United-States-USA&team=Health-Technology-HRDWR-HT',
    'https://jobs.apple.com/en-us/search?location=United-States-USA&team=Machine-Learning-HRDWR-MCHLN',
    'https://jobs.apple.com/en-us/search?location=United-States-USA&team=Mechanical-Engineering-HRDWR-ME',
    'https://jobs.apple.com/en-us/search?location=United-States-USA&team=Process-Engineering-HRDWR-PE',
    'https://jobs.apple.com/en-us/search?location=United-States-USA&team=Reliability-Engineering-HRDWR-REL',
    'https://jobs.apple.com/en-us/search?location=United-States-USA&team=Sensor-Technologies-HRDWR-SENT',
    'https://jobs.apple.com/en-us/search?location=United-States-USA&team=Silicon-Technologies-HRDWR-SILT',
    'https://jobs.apple.com/en-us/search?location=United-States-USA&team=System-Design-Engineering-HRDWR-SDE',
    'https://jobs.apple.com/en-us/search?location=United-States-USA&team=Wireless-Hardware-HRDWR-WT',
    'https://jobs.apple.com/en-us/search?location=united-states-USA&team=machine-learning-infrastructure-MLAI-MLI',
    'https://jobs.apple.com/en-us/search?location=united-states-USA&team=deep-learning-and-reinforcement-learning-MLAI-DLRL',
    'https://jobs.apple.com/en-us/search?location=united-states-USA&team=natural-language-processing-and-speech-technologies-MLAI-NLP',
    'https://jobs.apple.com/en-us/search?location=united-states-USA&team=computer-vision-MLAI-CV',
    'https://jobs.apple.com/en-us/search?location=united-states-USA&team=applied-research-MLAI-AR',
]

company_specific = {
    "ms": {
        "page_name": "pg"
    },
    "google": {
        "page_name": "page",
        "base_path": "https://www.google.com/about/careers/applications/jobs/results/"
    }
}

urls = {
    "google": {
        'se': 'https://www.google.com/about/careers/applications/jobs/results/?category=DATA_CENTER_OPERATIONS&category=DEVELOPER_RELATIONS&category=HARDWARE_ENGINEERING&category=INFORMATION_TECHNOLOGY&category=MANUFACTURING_SUPPLY_CHAIN&category=NETWORK_ENGINEERING&category=PRODUCT_MANAGEMENT&category=PROGRAM_MANAGEMENT&category=SOFTWARE_ENGINEERING&category=TECHNICAL_INFRASTRUCTURE_ENGINEERING&category=TECHNICAL_SOLUTIONS&category=TECHNICAL_WRITING&category=USER_EXPERIENCE&q=%22Software%20Engineer%22&page=1',
        'data': 'https://www.google.com/about/careers/applications/jobs/results/?category=DATA_CENTER_OPERATIONS&category=DEVELOPER_RELATIONS&category=HARDWARE_ENGINEERING&category=INFORMATION_TECHNOLOGY&category=MANUFACTURING_SUPPLY_CHAIN&category=NETWORK_ENGINEERING&category=PRODUCT_MANAGEMENT&category=PROGRAM_MANAGEMENT&category=SOFTWARE_ENGINEERING&category=TECHNICAL_INFRASTRUCTURE_ENGINEERING&category=TECHNICAL_SOLUTIONS&category=TECHNICAL_WRITING&category=USER_EXPERIENCE&q=Data',
        'ai': 'https://www.google.com/about/careers/applications/jobs/results/?category=DATA_CENTER_OPERATIONS&category=DEVELOPER_RELATIONS&category=HARDWARE_ENGINEERING&category=INFORMATION_TECHNOLOGY&category=MANUFACTURING_SUPPLY_CHAIN&category=NETWORK_ENGINEERING&category=PRODUCT_MANAGEMENT&category=PROGRAM_MANAGEMENT&category=SOFTWARE_ENGINEERING&category=TECHNICAL_INFRASTRUCTURE_ENGINEERING&category=TECHNICAL_SOLUTIONS&category=TECHNICAL_WRITING&category=USER_EXPERIENCE&q=AI',
        'ml': 'https://www.google.com/about/careers/applications/jobs/results/?category=DATA_CENTER_OPERATIONS&category=DEVELOPER_RELATIONS&category=HARDWARE_ENGINEERING&category=INFORMATION_TECHNOLOGY&category=MANUFACTURING_SUPPLY_CHAIN&category=NETWORK_ENGINEERING&category=PRODUCT_MANAGEMENT&category=PROGRAM_MANAGEMENT&category=SOFTWARE_ENGINEERING&category=TECHNICAL_INFRASTRUCTURE_ENGINEERING&category=TECHNICAL_SOLUTIONS&category=TECHNICAL_WRITING&category=USER_EXPERIENCE&q=Machine%20Learning',
    },
    "ms": {
        'se': 'https://jobs.careers.microsoft.com/global/en/search?q=software%20engineer&l=en_us&pgSz=20&o=Relevance&flt=true',
        'data': 'https://jobs.careers.microsoft.com/global/en/search?q=Data&l=en_us&pgSz=20&o=Relevance&flt=true',
        'ai': 'https://jobs.careers.microsoft.com/global/en/search?q=AI&l=en_us&pgSz=20&o=Relevance&flt=true',
        'ml': 'https://jobs.careers.microsoft.com/global/en/search?q=ML&l=en_us&pgSz=20&o=Relevance&flt=true',
    },
    "meta": {
        'se': 'https://www.metacareers.com/jobs?q=Software%20Engineer',
        'data': 'https://www.metacareers.com/jobs?q=Data',
        'ai': 'https://www.metacareers.com/jobs?q=AI',
        'ml': 'https://www.metacareers.com/jobs?q=Machine%20Learning'
    },
    "netflix": {
        'se': 'https://jobs.netflix.com/search?q=Software%20Engineer&location=Remote%2C%20United%20States',
        'data': 'https://jobs.netflix.com/search?q=AI&location=Remote%2C%20United%20States',
        'ai': 'https://jobs.netflix.com/search?q=Data&location=Remote%2C%20United%20States',
        'ml': 'https://jobs.netflix.com/search?q=Machine%20Learning&location=Remote%2C%20United%20States',
    },
    'amazon': {
        'se': 'https://www.amazon.jobs/en/search?offset=0&result_limit=10&sort=relevant&distanceType=Mi&radius=Anykm&latitude=30.43977&longitude=-84.28065&loc_group_id=&loc_query=&base_query=Software%20Engineer&city=&country=USA&region=Florida&county=&query_options=&',
        'data': 'https://www.amazon.jobs/en/search?base_query=AI&loc_query=&latitude=&longitude=&loc_group_id=&invalid_location=false&country=&city=&region=&county=',
        'ai': 'https://www.amazon.jobs/en/search?base_query=Data&loc_query=&latitude=&longitude=&loc_group_id=&invalid_location=false&country=&city=&region=&county=',
        'ml': 'https://www.amazon.jobs/en/search?base_query=Machine+Learning&loc_query=&latitude=&longitude=&loc_group_id=&invalid_location=false&country=&city=&region=&county=',
    },
    'nvidia': {
        'se': 'https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite?q=Software%20Engineer',
        'data': 'https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite?q=DATA',
        'ai': 'https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite?q=AI',
        'ml': 'https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite?q=ML',
    },
    "ms_start_key": 'Showing',
    "ms_end_key": 'results',
    "google_start_key": '1',
    "google_end_key": None,
}

headers = {
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://www.wallstreetzen.com/',
    'User-Agent': 'Chrome 124 on macOS (Sonoma)',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
}
