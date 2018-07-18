# from collections import OrderedDict

# res = OrderedDict(LOCATION_CHOICES)
# OrderedDict([('dc_china_telecom', 'DC - China Telecom'),
#              ('dc_sds', 'DC - SDS'),
#              ('e_shan_office', "E'Shan Office"),
#              ('puming_offce', 'Puming Offce'),
#              ('aliyun', 'AliYun')])

LOCATION_CHOICES = (
    ('dc_china_telecom', 'DC - China Telecom'),
    ('dc_sds', 'DC - SDS'),
    ('e_shan_office', "E'Shan Office"),
    ('puming_offce', 'Puming Offce'),
    ('aliyun', 'AliYun'),
)
ASSET_STATUS_CHOICES = (
    ('decommissioned', 'Decommissioned'),
    ('deactive', 'Deactive'),
    ('active', 'Active'),
    ('implementing', 'Implementing'),
    ('not_owned_by_dxc', 'Not owned by DXC'),
)
ENVIRONMENT_CHOICES = (
    ('dr', 'DR'),
    ('pre_production', 'Pre-Production'),
    ('production', 'Production'),
    ('sit', 'SIT'),
)
APP_CATEGORY_CHOICES = (
    ('lewtan', 'LEWTAN'),
    ('mft', 'MFT'),
    ('security', 'Security'),
    ('jump_for_vpn', 'Jump for VPN'),
    ('bpodat', 'BPODAT'),
    ('vmware', 'VMware'),
    ('core_service', 'Core Service'),
    ('bur', 'BUR'),
    ('wscp', 'WSCP'),
    ('poc', 'POC'),
    ('rta', 'RTA'),
    ('imaging', 'IMAGING'),
    ('sod', 'SOD'),
    ('lan_localization', 'LAN localization'),
    ('jump_server_for_dxc_hosting', 'Jump Server for DXC Hosting'),
    ('dris', 'DRIS'),
    ('aes_server', 'AES Server'),
    ('carrs', 'CARRS'),
    ('test', 'Test'),
    ('rtcs', 'RTCS'),
    ('exchange_upgrade_poc', 'Exchange Upgrade POC'),
    ('siem', 'SIEM'),
    ('svn', 'SVN'),
    ('hris', 'HRIS'),
    ('waf', 'WAF'),
)
Device_Type_CHOICES = (
    ('virtual_machine', 'Virtual Machine'),
    ('physical_machine', 'Physical Machine'),
    ('backup_device', 'Backup Device'),
    ('storage', 'Storage'),
    ('ecs', 'ECS'),
)
OS_TYPE_CHOICES = (
    ('windows', 'WINDOWS'),
    ('linux', 'LINUX'),
    ('esx', 'ESX'),
)
Operating_System_CHOICES = (
    ('microsoft_windows_7_32_bit', 'Microsoft Windows 7 (32-bit)'),
    ('microsoft_windows_7_64_bit', 'Microsoft Windows 7 (64-bit)'),
    ('linux_redhat_el_6.7_64bit', 'LINUX RedHat EL 6.7 64bit'),
    ('novell_suse_linux_enterprise_11_64_bit', 'Novell SUSE Linux Enterprise 11 (64-bit)'),
    ('windows7', 'Windows 7'),
    ('windows7_x64', 'Windows 7 x64'),
    ('microsoft_windows_server_2012_r2_64_bit', 'Microsoft Windows Server 2012 R2 (64-bit)'),
    ('other_linux_64_bit', 'Other Linux (64-bit)'),
    ('windows10', 'Windows 10'),
    ('microsoft_windows_server_2008_r2_64_bit', 'Microsoft Windows Server 2008 R2 (64-bit)'),
    ('linux_redhat_el_5.8', 'LINUX RedHat EL 5.8'),
    ('vmware_esxi_6.0.0_4192238', 'VMware ESXi, 6.0.0, 4192238'),
    ('microsoft_windows_server_2003_standard', 'Microsoft Windows Server 2003 Standard'),
)
SOFTWARE_TYPE_CHOICES = (
    ('db', 'DB'),
    ('middleware', 'MIDDLEWARE'),
)
NETWORK_ZONE_CHOICES = (
    ('infra_zone', 'Infra zone'),
    ('app_db_zone', 'APP/DB zone'),
    ('web_zone', 'Web zone'),
)
NETWORK_TYPE_CHOICES = (
    ('biz_ip', 'Biz IP'),
    ('mgmt_ip', 'Mgmt IP'),
    ('backup_ip', 'Backup IP'),
    ('vmotion_oob_ip', 'vMotion\OOB IP'),
    ('internet_ip_port', 'Internet IP (Port)'),
)
for choice in [ASSET_STATUS_CHOICES]:
    res = dict(choice)
    res1 = {v: k for k, v in res.iteritems()}
    print str(res1)
    print str(res1).replace("\'", "\"")
    print '-' * 30

loc = {"AliYun": "aliyun", "DC - SDS": "dc_sds", "Puming Offce": "puming_offce", "E'Shan Office": "e_shan_office", "DC - China Telecom": "dc_china_telecom"}

ass = {"Active": "active", "Implementing": "implementing", "Decommissioned": "decommissioned", "Not owned by DXC": "not_owned_by_dxc", "Deactive": "deactive"}

d1 = {'Production': 'production', 'DR': 'dr', 'Pre-Production': 'pre_production', 'SIT': 'sit'}
d10 = {"Production": "production", "DR": "dr", "Pre-Production": "pre_production", "SIT": "sit"}

d2 = {'LEWTAN': 'lewtan', 'Exchange Upgrade POC': 'exchange_upgrade_poc', 'HRIS': 'hris', 'WSCP': 'wscp',
      'Test': 'test', 'AES Server': 'aes_server', 'RTA': 'rta', 'SOD': 'sod', 'BUR': 'bur', 'DRIS': 'dris',
      'CARRS': 'carrs', 'MFT': 'mft', 'IMAGING': 'imaging', 'SIEM': 'siem', 'POC': 'poc',
      'Jump Server for DXC Hosting': 'jump_server_for_dxc_hosting', 'SVN': 'svn', 'WAF': 'waf', 'Security': 'security',
      'LAN localization': 'lan_localization', 'Jump for VPN': 'jump_for_vpn', 'VMware': 'vmware', 'BPODAT': 'bpodat',
      'Core Service': 'core_service', 'RTCS': 'rtcs'}
d20 = {"LEWTAN": "lewtan", "Exchange Upgrade POC": "exchange_upgrade_poc", "HRIS": "hris", "WSCP": "wscp",
       "Test": "test", "AES Server": "aes_server", "RTA": "rta", "SOD": "sod", "BUR": "bur", "DRIS": "dris",
       "CARRS": "carrs", "MFT": "mft", "IMAGING": "imaging", "SIEM": "siem", "POC": "poc",
       "Jump Server for DXC Hosting": "jump_server_for_dxc_hosting", "SVN": "svn", "WAF": "waf", "Security": "security",
       "LAN localization": "lan_localization", "Jump for VPN": "jump_for_vpn", "VMware": "vmware", "BPODAT": "bpodat",
       "Core Service": "core_service", "RTCS": "rtcs"}

d3 = {'Backup Device': 'backup_device', 'ECS': 'ecs', 'Storage': 'storage', 'Physical Machine': 'physical_machine',
      'Virtual Machine': 'virtual_machine'}
d30 = {"Backup Device": "backup_device", "ECS": "ecs", "Storage": "storage", "Physical Machine": "physical_machine",
       "Virtual Machine": "virtual_machine"}

d4 = {'WINDOWS': 'windows', 'LINUX': 'linux', 'ESX': 'esx'}
d40 = {"WINDOWS": "windows", "LINUX": "linux", "ESX": "esx"}

d5 = {'Other Linux (64-bit)': 'other_linux_64_bit',
      'Novell SUSE Linux Enterprise 11 (64-bit)': 'novell_suse_linux_enterprise_11_64_bit',
      'Microsoft Windows Server 2003 Standard': 'microsoft_windows_server_2003_standard',
      'Microsoft Windows 7 (64-bit)': 'microsoft_windows_7_64_bit',
      'LINUX RedHat EL 6.7 64bit': 'linux_redhat_el_6.7_64bit',
      'Microsoft Windows Server 2008 R2 (64-bit)': 'microsoft_windows_server_2008_r2_64_bit',
      'Windows 7 x64': 'windows7_x64', 'LINUX RedHat EL 5.8': 'linux_redhat_el_5.8',
      'Microsoft Windows 7 (32-bit)': 'microsoft_windows_7_32_bit',
      'VMware ESXi, 6.0.0, 4192238': 'vmware_esxi_6.0.0_4192238', 'Windows 10': 'windows10', 'Windows 7': 'windows7',
      'Microsoft Windows Server 2012 R2 (64-bit)': 'microsoft_windows_server_2012_r2_64_bit'}
d50 = {"Other Linux (64-bit)": "other_linux_64_bit",
       "Novell SUSE Linux Enterprise 11 (64-bit)": "novell_suse_linux_enterprise_11_64_bit",
       "Microsoft Windows Server 2003 Standard": "microsoft_windows_server_2003_standard",
       "Microsoft Windows 7 (64-bit)": "microsoft_windows_7_64_bit",
       "LINUX RedHat EL 6.7 64bit": "linux_redhat_el_6.7_64bit",
       "Microsoft Windows Server 2008 R2 (64-bit)": "microsoft_windows_server_2008_r2_64_bit",
       "Windows 7 x64": "windows7_x64", "LINUX RedHat EL 5.8": "linux_redhat_el_5.8",
       "Microsoft Windows 7 (32-bit)": "microsoft_windows_7_32_bit",
       "VMware ESXi, 6.0.0, 4192238": "vmware_esxi_6.0.0_4192238", "Windows 10": "windows10", "Windows 7": "windows7",
       "Microsoft Windows Server 2012 R2 (64-bit)": "microsoft_windows_server_2012_r2_64_bit"}

d6 = {'MIDDLEWARE': 'middleware', 'DB': 'db'}
d60 = {"MIDDLEWARE": "middleware", "DB": "db"}

d7 = {'Web zone': 'web_zone', 'Infra zone': 'infra_zone', 'APP/DB zone': 'app_db_zone'}
d70 = {"Web zone": "web_zone", "Infra zone": "infra_zone", "APP/DB zone": "app_db_zone"}

d8 = {'Backup IP': 'backup_ip', 'Mgmt IP': 'mgmt_ip', 'Internet IP (Port)': 'internet_ip_port', 'Biz IP': 'biz_ip',
      'vMotion\\OOB IP': 'vmotion_oob_ip'}
d80 = {"Backup IP": "backup_ip", "Mgmt IP": "mgmt_ip", "Internet IP (Port)": "internet_ip_port", "Biz IP": "biz_ip",
       "vMotion\\OOB IP": "vmotion_oob_ip"}
